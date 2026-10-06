from aql_link.filter.filter_dict import Filter

class SystemFunctionStrategy:
    def __init__(self, name, fn_list):
        self.name = name
        self.fn_list = fn_list

    def content_replace(self, ctx):
        query_results = self.fn_list
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
            tmp_query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", name).first().get_source()
            result = result.replace("<query>", tmp_query)
            results = results + result

        ctx.content = ctx.content.replace(f"<{self.name}:list>", results)
        ctx.content = ctx.content.replace(f"<{self.name}:count>", str(len(query_results)))