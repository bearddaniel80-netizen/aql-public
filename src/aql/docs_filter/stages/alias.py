from .base import FilterReplace
from .strategies.query_strategy import QueryStrategy
from ..registry import pattern

@pattern([
    "<alias:single>",
])
class AliasReplace(FilterReplace):
    def __init__(self):
        filter_dict = self._build_dict()
        super().__init__(QueryStrategy(filter_dict))

    def _build_dict(self):
        return {
            "alias:single": [
                {"attr": "is_cte", "value": "False"},
                {"attr": "fields", "value": "TITLE"},
                {"attr": "fields_alias", "value": "generic_alias"},
            ]
        }