from .base import FilterReplace
from .strategies.query_strategy import QueryStrategy
from ..registry import pattern

@pattern([
    "<cte:neg>",
    "<cte:op:and>",
    "<cte:op:or>",
    "<having:neg>",
    "<having:op:and>",
    "<having:op:or>",
    "<neg:between>",
    "<neg:in>",
    "<order:neg>",
    "<order:op:and>",
    "<order:op:or>"
])
class PredicateReplace(FilterReplace):
    def __init__(self):
        filter_dict = self._build_dict()
        super().__init__(QueryStrategy(filter_dict))

    def _build_dict(self):
        return {
            "cte:neg": [
                {"attr": "is_cte", "value": "True"},
                {"attr": "fields", "value": "name"},
                {"attr": "clauses", "value": "NOT"},
            ],
            "cte:op:and": [
                {"attr": "is_cte", "value": "True"},
                {"attr": "fields", "value": "name"},
                {"attr": "clauses", "value": "AND"},
            ],
            "cte:op:or": [
                {"attr": "is_cte", "value": "True"},
                {"attr": "fields", "value": "name"},
                {"attr": "clauses", "value": "OR"},
            ],
            "having:neg": [
                {"attr": "is_cte", "value": "False"},
                {"attr": "fields", "value": "name"},
                {"attr": "clauses", "value": "HAVING"},
                {"attr": "clauses", "value": "NOT"},
            ],
            "having:op:and": [
                {"attr": "is_cte", "value": "False"},
                {"attr": "fields", "value": "name"},
                {"attr": "clauses", "value": "HAVING"},
                {"attr": "clauses", "value": "AND"},
            ],
            "having:op:or": [
                {"attr": "is_cte", "value": "False"},
                {"attr": "fields", "value": "name"},
                {"attr": "clauses", "value": "HAVING"},
                {"attr": "clauses", "value": "OR"},
            ],
            "neg:between": [
                {"attr": "is_cte", "value": "False"},
                {"attr": "fields", "value": "name"},
                {"attr": "clauses", "value": "BETWEEN"},
                {"attr": "clauses", "value": "NOT"},
            ],
            "neg:in": [
                {"attr": "is_cte", "value": "False"},
                {"attr": "fields", "value": "name"},
                {"attr": "clauses", "value": "IN"},
                {"attr": "clauses", "value": "NOT"},
            ],
            "order:neg": [
                {"attr": "is_cte", "value": "False"},
                {"attr": "fields", "value": "name"},
                {"attr": "clauses", "value": "ORDER"},
                {"attr": "clauses", "value": "NOT"},
            ],
            "order:op:and": [
                {"attr": "is_cte", "value": "False"},
                {"attr": "fields", "value": "name"},
                {"attr": "clauses", "value": "ORDER"},
                {"attr": "clauses", "value": "AND"},
            ],
            "order:op:or": [
                {"attr": "is_cte", "value": "False"},
                {"attr": "fields", "value": "name"},
                {"attr": "clauses", "value": "ORDER"},
                {"attr": "clauses", "value": "OR"},
            ]
        }