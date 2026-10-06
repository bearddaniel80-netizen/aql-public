from .base import BaseReplace
from aql_link.filter.filter_dict import Filter
from ...engine.resolve_source_handlers.identifier_sources.operators import OperatorSource

# replace placeholder <order:single>
class BinaryOpReplace(BaseReplace):
    def content_replace(self, ctx):
        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").where("clauses", "NOT").where("operation", "BETWEEN").first().get_source()
        ctx.content = ctx.content.replace("<neg:between>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").where("clauses", "NOT").where("operation", "IN").first().get_source()
        ctx.content = ctx.content.replace("<neg:in>", query)

        query_results = OperatorSource().query()
        results = ""
        template_str = f"## <name>\n### Basic syntax\n```sql\n<query>\n```\n---\n\n"
        for q in query_results:
            name = q["name"]
            result = template_str.replace("<name>", name)
            tmp_query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").where("operation", name).first().get_source()
            result = result.replace("<query>", tmp_query)
            results = results + result

        ctx.content = ctx.content.replace("<op:list>", results)
        ctx.content = ctx.content.replace("<op:count>", str(len(query_results)))