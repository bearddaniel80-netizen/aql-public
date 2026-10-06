from dataclasses import dataclass, field
from enum import Enum

class DestinationType(str, Enum):
    EXAMPLE = "examples"
    SCRIPT = "scripts"
    SOURCES = "sources"

@dataclass
class System:
    ID: int = -1
    title: str = ""
    description: str = ""
    clauses: list[str] = field(default_factory=list)
    template: str = ""
    destination: DestinationType = DestinationType.EXAMPLE

    def to_dict(self):
        return {
            "ID": self.ID,
            "title": self.title,
            "description": self.description,
            "template": self.template,
            "destination": self.destination.value,
            "clauses": self.clauses
        }
DOCUMENTATION = {
    "aggregates": System(
        title="Aggregate Functions",
        description="Acts on entire rows.",
        clauses=["GROUP BY", "HAVING", "ORDER BY"],
        template="example_aggregates",
        destination=DestinationType.EXAMPLE,
    ),
    "alias": System(
        title="Field alias",
        description="Simplify naming of fields",
        clauses=["SELECT", "GROUP BY", "HAVING", "ORDER BY"],
        template="example_alias",
        destination=DestinationType.EXAMPLE,
    ),
    "binaryop": System(
        title="Operators",
        description="Let's you filter based on conditions",
        template="example_binary",
        clauses=["WHERE", "HAVING", "ORDER BY"],
        destination=DestinationType.EXAMPLE,
    ),
    "comments": System(
        title="Script comments",
        description="Either for clarification or documentation",
        template="script_comment",
        destination=DestinationType.SCRIPT,
    ),
    "common_table_expression": System(
        title="Common table expression",
        description="Replaces temp table, allows for refactoring",
        clauses=["SELECT", "FROM", "WHERE", "GROUP BY", "HAVING", "ORDER BY"],
        template="example_cte",
        destination=DestinationType.EXAMPLE,
    ),
    "declare": System(
        title="Script macro",
        description="Allows for substitutions of expressions", 
        clauses=["WITH", "SELECT", "FROM", "WHERE", "GROUP BY", "HAVING", "ORDER BY"],
        template="script_declare",
        destination=DestinationType.SCRIPT,
    ),
    "groupby": System(
        title="GROUP BY clause",
        description="Used on fields inside aggregate functions",
        clauses=["SELECT", "GROUP BY", "HAVING", "ORDER BY"],
        template="example_group",
        destination=DestinationType.EXAMPLE,
    ),
    "having": System(
        title="HAVING clause",
        description="Used on fields inside aggregate functions",
        clauses=["GROUP BY", "HAVING", "ORDER BY"],
        template="example_having",
        destination=DestinationType.EXAMPLE,
    ),
    "logic": System(
        title="Logic operator",
        description="Combines two or more expressions",
        template="example_logic",
        destination=DestinationType.EXAMPLE,
    ),
    "negate": System(
        title="Negate operator",
        description="Reverse logic of expression",
        template="example_negation",
        destination=DestinationType.EXAMPLE,
    ),
    "orderby": System(
        title="ORDER BY clause",
        description="Orders results asending or descending",
        clauses=["ORDER BY"],
        template="example_order",
        destination=DestinationType.EXAMPLE,
    ),
    "projection": System(
        title="Process of selecting fields",
        description="Select all or some fields",
        clauses=["SELECT"],
        template="example_projections",
        destination=DestinationType.EXAMPLE,
    ),
    "scalars": System(
        title="Scalar functions",
        description="Acts on a single field",
        clauses=["SELECT"],
        template="example_scalars",
        destination=DestinationType.EXAMPLE,
    ),
    "system_docs": System(
        title="Queries",
        description="Allows one to see all possible queries",
        clauses=["FROM"],
        template="example_system_docs",
        destination=DestinationType.EXAMPLE,
    ),
    "system_source": System(
        title="Stdin source",
        description="Uses unix commands and pipes as source",
        clauses=["FROM"],
        template="example_system_source",
        destination=DestinationType.EXAMPLE,
    ),
    "table_function": System(
        title="Table source",
        description="Reads a file or a stream",
        clauses=["FROM"],
        template="example_table_function",
        destination=DestinationType.EXAMPLE,
    ),
    "using": System(
        title="Script import",
        description="In memory, creates one continous file",
        template="script_using",
        destination=DestinationType.SCRIPT,
    ),

}