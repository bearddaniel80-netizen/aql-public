from .base import BaseReplace
from aql_link.filter.filter_dict import Filter
from ...engine.resolve_source_handlers.identifier_sources.aggregates import AggregateSource

# replace placeholder <order:single>
class AggregatesReplace(BaseReplace):
    def content_replace(self, ctx):

        query_results = AggregateSource().query()
        results = ""
        template_str = "## <name>\n"
        template_str += "*Description:* <desc>\n"
        template_str += "*Takes:* <input>\n"
        template_str += "*Returns:* <return>\n"
        template_str += "### Basic syntax\n```sql\n<query>\n```\n---\n\n"
        for q in query_results:
            name = q["name"]
            result = template_str.replace("<name>", name)
            result = result.replace("<desc>", q["description"])
            result = result.replace("<input>", ", ".join(q["input_type"]))
            result = result.replace("<return>", q["return_type"])
            tmp_query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").where("feature", name).first().get_source()
            result = result.replace("<query>", tmp_query)
            results = results + result

        ctx.content = ctx.content.replace("<aggregate:list>", results)
        ctx.content = ctx.content.replace("<aggregate:count>", str(len(query_results)))