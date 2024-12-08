import argparse
from pathlib import Path
from shacl_doc_generator.parser import ShaclParser
from shacl_doc_generator.generator import MarkdownGenerator

def main():
    parser = argparse.ArgumentParser(description="SHACLER - SHACL Documentation Generator")
    parser.add_argument("--input", required=True, help="Path to SHACL file or directory containing SHACL files.")
    parser.add_argument("--output", required=False, default="./docs", help="Path to output directory for markdown files.")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    shacl_parser = ShaclParser()
    shapes_all = {}

    if input_path.is_dir():
        for f in input_path.glob("*.ttl"):
            shapes = shacl_parser.parse_file(f)
            for k, v in shapes.items():
                shapes_all[k] = v
    else:
        shapes_all = shacl_parser.parse_file(input_path)

    md_generator = MarkdownGenerator()
    output_file = output_dir / 'shapes.md'
    md_generator.generate_docs(shapes_all, output_file)

if __name__ == "__main__":
    main()
