from .base import FilterReplace
from .strategies.query_strategy import QueryStrategy
from ..registry import pattern

@pattern([
    "<cte:star>", 
    "<cte:single>"
    "<group:star>", 
    "<group:single>",
    "<group:cte>",
    "<having:star>", 
    "<having:single>",
    "<having:cte>",
    "<order:star>", 
    "<order:single>",
    "<order:cte>",
])
class ClauseReplace(FilterReplace):
    def __init__(self):
        filter_dict = self._build_dict()
        super().__init__(QueryStrategy(filter_dict))

    def _build_dict(self):
        return {
            "cte:single": [
                {"attr": "is_cte", "value": "True"},
                {"attr": "fields", "value": "name"},
            ],
            "cte:star": [
                {"attr": "is_cte", "value": "True"},
                {"attr": "fields", "value": "*"},
            ],
            "group:single": [
                {"attr": "is_cte", "value": "False"},
                {"attr": "fields", "value": "name"},
                {"attr": "clauses", "value": "GROUP BY"},
            ],
            "group:star": [
                {"attr": "is_cte", "value": "False"},
                {"attr": "fields", "value": "*"},
                {"attr": "clauses", "value": "GROUP BY"},
            ],
            "group:cte": [
                {"attr": "is_cte", "value": "True"},
                {"attr": "fields", "value": "name"},
                {"attr": "clauses", "value": "GROUP BY"},
            ],
            "having:single": [
                {"attr": "is_cte", "value": "False"},
                {"attr": "fields", "value": "name"},
                {"attr": "clauses", "value": "HAVING"},
            ],
            "having:star": [
                {"attr": "is_cte", "value": "False"},
                {"attr": "fields", "value": "*"},
                {"attr": "clauses", "value": "HAVING"},
            ],
            "having:cte": [
                {"attr": "is_cte", "value": "True"},
                {"attr": "fields", "value": "name"},
                {"attr": "clauses", "value": "HAVING"},
            ],
            "order:single": [
                {"attr": "is_cte", "value": "False"},
                {"attr": "fields", "value": "name"},
                {"attr": "clauses", "value": "ORDER"},
            ],
            "order:star": [
                {"attr": "is_cte", "value": "False"},
                {"attr": "fields", "value": "*"},
                {"attr": "clauses", "value": "ORDER"},
            ],
            "order:cte": [
                {"attr": "is_cte", "value": "True"},
                {"attr": "fields", "value": "name"},
                {"attr": "clauses", "value": "ORDER"},
            ]
        }