from .base import FilterReplace
from .strategies.query_strategy import QueryStrategy
from ..registry import pattern

@pattern([
    "<field:star>", 
    "<field:single>"
])
class ProjectionReplace(FilterReplace):
    def __init__(self):
        filter_dict = self._build_dict()
        super().__init__(QueryStrategy(filter_dict))

    def _build_dict(self):
        return {
            "field:single": [
                {"attr": "is_cte", "value": "False"},
                {"attr": "fields", "value": "name"},
            ],
            "field:star": [
                {"attr": "is_cte", "value": "False"},
                {"attr": "fields", "value": "star"},
            ]
        }