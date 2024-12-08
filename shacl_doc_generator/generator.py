from typing import Dict
from shacl_doc_generator.models import NodeShapeInfo, PropertyShapeInfo, Constraint, Path, PathEnum

class MarkdownGenerator:
    def generate_docs(self, shapes: Dict[str, NodeShapeInfo], output_filename: str = "shapes.md"):
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write("# SHACL Shapes Documentation\n\n")
            for shape_id, shape_info in shapes.items():
                f.write(f"## Shape: {shape_id}\n\n")

                if shape_info.constraints:
                    f.write("### NodeShape Constraints\n\n")
                    for c in shape_info.constraints:
                        f.write(f"- **{c.name}:** {c.value}\n")
                    f.write("\n")

                if shape_info.properties:
                    f.write("### Properties\n\n")
                    for pshape in shape_info.properties:
                        f.write(f"#### Property: {pshape.id}\n\n")
                        f.write("**Path:** " + self._format_path(pshape.path) + "\n\n")

                        if pshape.constraints:
                            f.write("**Constraints:**\n")
                            for c in pshape.constraints:
                                f.write(f"- **{c.name}:** {c.value}\n")
                            f.write("\n")

                f.write("---\n\n")

    def _format_path(self, path: Path) -> str:
        """Convert a Path object into a human-readable string representation."""
        # Different formatting depending on path type
        if path.type == PathEnum.predicate:
            # items should contain a single string (the URI)
            return path.items[0] if path.items else "???"

        elif path.type == PathEnum.inverse:
            # inverse has one inner path
            inner = self._format_path(path.items[0]) if path.items else "???"
            return f"^{inner}"

        elif path.type == PathEnum.sequence:
            # sequence has multiple items, each item could be a string or another Path
            parts = [self._format_path_item(it) for it in path.items]
            return "/".join(parts)

        elif path.type == PathEnum.alternative:
            # alternative paths separated by '|'
            parts = [self._format_path_item(it) for it in path.items]
            return "|".join(parts)

        elif path.type == PathEnum.zero_or_more:
            inner = self._format_path_item(path.items[0]) if path.items else "???"
            return f"{inner}*"

        elif path.type == PathEnum.one_or_more:
            inner = self._format_path_item(path.items[0]) if path.items else "???"
            return f"{inner}+"

        elif path.type == PathEnum.zero_or_one:
            inner = self._format_path_item(path.items[0]) if path.items else "???"
            return f"{inner}?"

        else:
            # Unknown path type
            return "???"

    def _format_path_item(self, item):
        """Format a single path item which can be either a string (predicate) or a Path."""
        if isinstance(item, str):
            return item
        elif isinstance(item, Path):
            return f"({self._format_path(item)})"
        else:
            return "???"
