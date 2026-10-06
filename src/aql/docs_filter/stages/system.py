from .base import FilterReplace
from .strategies.system_function_strategy import SystemFunctionStrategy
from .strategies.system_operator_strategy import SystemOperatorStrategy
from .strategies.system_adapter_strategy import SystemAdapterStrategy
from ..registry import pattern

@pattern([
    "<aggregate>",
    "<aggregate:list>",
    "<aggregate:count>",
    "<scalar>",
    "<scalar:list>",
    "<scalar:count>",
    "<table>",
    "<table:list>",
    "<table:count>",
    "<op:list>",
    "<op:count>"
])
class SytemReplace(FilterReplace):
    def __init__(self):
        if "aggregate" in self.words:
            self._aggregate()
        elif "scalar" in self.words:
            self._scalar()
        elif "op" in self.words:
            self._op()
        else:
            self._table()

    def _aggregate(self):
        from ...engine.resolve_source_handlers.identifier_sources.aggregates import AggregateSource
        name = "aggregate"
        lst = AggregateSource().query()
        super().__init__(SystemFunctionStrategy(name, lst))
    
    def _scalar(self):
        from ...engine.resolve_source_handlers.identifier_sources.scalars import ScalarSource
        name ="scalar"
        lst =ScalarSource().query()
        super().__init__(SystemFunctionStrategy( name, lst))

    def _op(self):
        from ...engine.resolve_source_handlers.identifier_sources.operators import OperatorSource
        name = "operator"
        lst = OperatorSource().query()
        super().__init__(SystemOperatorStrategy( name, lst))

    def _table(self):
        from ...link import fn_call
        from ...link.registry import PRINTABLE, FuncType
        name = "table"
        lst = [ item for item in PRINTABLE if item["func_type"] == FuncType.ADAPTER]
        super().__init__(SystemAdapterStrategy(name, lst))