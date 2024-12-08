from pathlib import Path
from typing import Dict, Any, List, Union
from rdflib import Graph, Namespace, URIRef, BNode, Literal
from rdflib.namespace import RDF, RDFS
from shacl_doc_generator.models import NodeShapeInfo, PropertyShapeInfo, Constraint, Path, PathEnum

SH = Namespace("http://www.w3.org/ns/shacl#")

class ShaclParser:
    def __init__(self):
        self.shapes: Dict[str, NodeShapeInfo] = {}

    def parse_file(self, file_path: Path) -> Dict[str, NodeShapeInfo]:
        g = Graph()
        print(f"Parsing file: {file_path}")
        g.parse(file_path, format="turtle")

        node_shapes = list(g.subjects(RDF.type, SH.NodeShape))

        for node in node_shapes:
            shape_info = self.extract_node_shape_info(g, node)
            self.shapes[str(node)] = shape_info

        return self.shapes

    def extract_node_shape_info(self, g: Graph, node: URIRef) -> NodeShapeInfo:
        node_constraints = self.extract_constraints(g, node)
        node_properties = self.extract_properties(g, node)

        node_shape = NodeShapeInfo(
            type='NodeShape',
            constraints=node_constraints,
            properties=node_properties
        )

        return node_shape

    def extract_constraints(self, g: Graph, node: URIRef) -> List[Constraint]:
        constraints = []
        for p, o in g.predicate_objects(node):
            if str(p).startswith(str(SH)) and p not in (SH.property, SH.path):
                c_key = self._get_property_label(g, p)
                c_val = self._extract_bnode_shape(g, o) if isinstance(o, BNode) else str(o)
                constraints.append(Constraint(name=c_key, value=c_val))
        return constraints

    def extract_properties(self, g: Graph, node: URIRef) -> List[PropertyShapeInfo]:
        properties = []
        for o in g.objects(node, SH.property):
            prop_info = self.extract_property_shape_info(g, o)
            properties.append(prop_info)
        return properties

    def extract_property_shape_info(self, g: Graph, pshape: URIRef) -> PropertyShapeInfo:
        path_node = g.value(pshape, SH.path)
        path = self._parse_path(g, path_node)

        return PropertyShapeInfo(
            id=str(pshape),
            path=path,
            constraints=self.extract_constraints(g, pshape)
        )

    def _get_property_label(self, g: Graph, prop: URIRef) -> str:
        label = g.value(prop, RDFS.label)
        if label:
            return str(label)
        else:
            return g.namespace_manager.normalizeUri(prop)

    def _extract_list(self, g: Graph, bnode: BNode) -> List[Any]:
        elements = []
        head = bnode
        while head and head != RDF.nil:
            first = g.value(head, RDF.first)
            if first:
                elements.append(first)
            head = g.value(head, RDF.rest)
        return elements

    def _extract_bnode_shape(self, g: Graph, bnode: BNode) -> Dict[str, Any]:
        bnode_info = {}
        for p, o in g.predicate_objects(bnode):
            if str(p).startswith(str(SH)):
                c_key = self._get_property_label(g, p)
                bnode_info[c_key] = o 
        return bnode_info

    def _parse_path(self, g: Graph, node: Union[URIRef, BNode]) -> Path:
        """Parse a path node (URIRef or BNode) into a Path object."""
        if isinstance(node, URIRef):
            return Path(type=PathEnum.predicate, items=[str(node)])

        # Check inversePath
        inverse = g.value(node, SH.inversePath)
        if inverse is not None:
            # inverse must be a well-formed path
            inner_path = self._parse_path(g, inverse)
            return Path(type=PathEnum.inverse, items=[inner_path])

        # Check alternativePath
        alt_list = g.value(node, SH.alternativePath)
        if alt_list is not None:
            # alt_list is a SHACL list of paths
            members = self._parse_path_list(g, alt_list)
            return Path(type=PathEnum.alternative, items=members)

        # Check zeroOrMorePath
        zero_or_more = g.value(node, SH.zeroOrMorePath)
        if zero_or_more is not None:
            inner_path = self._parse_path(g, zero_or_more)
            return Path(type=PathEnum.zero_or_more, items=[inner_path])

        # Check oneOrMorePath
        one_or_more = g.value(node, SH.oneOrMorePath)
        if one_or_more is not None:
            inner_path = self._parse_path(g, one_or_more)
            return Path(type=PathEnum.one_or_more, items=[inner_path])

        # Check zeroOrOnePath
        zero_or_one = g.value(node, SH.zeroOrOnePath)
        if zero_or_one is not None:
            inner_path = self._parse_path(g, zero_or_one)
            return Path(type=PathEnum.zero_or_one, items=[inner_path])

        if self._is_shacl_list(g, node):
            members = self._parse_path_list(g, node)
            if len(members) < 2:
                raise ValueError("Sequence path must have at least two elements.")
            return Path(type=PathEnum.sequence, items=members)

        # If we reach here, it's not a recognized path form
        raise ValueError(f"Unrecognized path structure at node {node}")

    def _is_shacl_list(self, g: Graph, node: BNode) -> bool:
        if node == RDF.nil:
            return True
        # must have exactly one rdf:first and one rdf:rest
        first = g.value(node, RDF.first)
        rest = g.value(node, RDF.rest)
        return first is not None and rest is not None

    def _parse_path_list(self, g: Graph, list_node: BNode) -> List[Union[Path, str]]:
        """Parse a SHACL list of paths into a list of Path or string (for predicate)."""
        elements = []
        head = list_node
        while head and head != RDF.nil:
            first = g.value(head, RDF.first)
            if first is None:
                raise ValueError(f"Malformed list: {head} has no rdf:first")
            # parse first as a path element
            elements.append(self._parse_path_element(g, first))
            head = g.value(head, RDF.rest)
        return elements

    def _parse_path_element(self, g: Graph, element):
        """Parse a single path element, which can be a URIRef (predicate) or a complex BNode path."""
        if isinstance(element, URIRef):
            return str(element)
        elif isinstance(element, BNode):
            return self._parse_path(g, element)
        else:
            raise ValueError(f"Path element {element} is neither URIRef nor BNode.")
