from aql_link.filter.filter_dict import Filter

class SystemAdapterStrategy:
    def __init__(self, name, fn_list):
        self.name = name
        self.fn_list = fn_list

    def content_replace(self, ctx):
        query_results = self.fn_list
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

        ctx.content = ctx.content.replace(f"<{self.name}:list>", results)
        ctx.content = ctx.content.replace(f"<{self.name}:count>", str(len(query_results)))