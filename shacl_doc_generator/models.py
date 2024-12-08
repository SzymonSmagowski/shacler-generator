from dataclasses import dataclass, field
import enum
from typing import Any, List, Union

@dataclass
class Constraint:
    name: str
    value: Any

class PathEnum(enum.Enum):
    predicate = "PredicatePath"
    inverse = "InversePath"
    sequence = "SequencePath"
    alternative = "AlternativePath"
    zero_or_more = "ZeroOrMorePath"
    one_or_more = "OneOrMorePath"
    zero_or_one = "ZeroOrOnePath"

@dataclass
class Path:
    type: PathEnum
    items: List[Union["Path", str]]


@dataclass
class NodeShapeInfo:
    id: str
    constraints: List[Constraint] = field(default_factory=list)

@dataclass
class PropertyShapeInfo:
    id: str
    path: Path
    constraints: List[Constraint] = field(default_factory=list)

@dataclass
class NodeShapeInfo:
    type: str
    constraints: List[Constraint] = field(default_factory=list)
    properties: List[PropertyShapeInfo] = field(default_factory=list)
