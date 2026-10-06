from dataclasses import dataclass, field

@dataclass
class FilterContext:
    name: str = ""
    content: str = ""
    destination: str = ""
    queries: list[str] = field(default_factory=list)