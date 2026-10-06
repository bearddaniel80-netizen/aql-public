from .base import Stage
from ..query_exec_context import ExecutionContext

class OrderByStage(Stage):

    def execute(self, context):

        query = context.query

        if not query.order_by:
            return context

        context.rows = sorted(
            context.rows,
            key=self.build_key(query.order_by[0].field, context),
            reverse=query.order_by[0].descending
        )

        return context

    def build_key(self, field, context):
        def key(row):
            value = context.engine_context.evaluator.evaluate(field, row)
            
            return (
                value is None,
                value
            )

        return key