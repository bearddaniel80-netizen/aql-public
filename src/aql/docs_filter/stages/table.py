from .base import BaseReplace
from aql_link.filter.filter_dict import Filter
from ...link import fn_call
from ...link.registry import PRINTABLE, FuncType

# replace placeholder <order:single>
class FunctionsReplace(BaseReplace):
    def content_replace(self, ctx):

        query_results = [ item for item in PRINTABLE if item["func_type"] == FuncType.ADAPTER]
        results = ""
        template_str = "## <name>\n"
        template_str += "*Description:* <desc>\n"
        template_str += "*Enabled:* <enabled>\n---\n\n"
        for q in query_results:
            name = q["name"]
            result = template_str.replace("<name>", name)
            result = result.replace("<desc>", q["description"])
            result = result.replace("<enabled>", q["enabled"])
            results = results + result

        ctx.content = ctx.content.replace("<table:list>", results)
        ctx.content = ctx.content.replace("<table:count>", str(len(query_results)))