from aql_link.filter.filter_dict import Filter

class SystemOperatorStrategy:
    def __init__(self, name, fn_list):
        self.name = name
        self.fn_list = fn_list

    def content_replace(self, ctx):
        query_results = self.fn_list
        results = ""
        template_str = f"## <name>\n### Basic syntax\n```sql\n<query>\n```\n---\n\n"
        for q in query_results:
            name = q["name"]
            result = template_str.replace("<name>", name)
            tmp_query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").where("operation", name).first().get_source()
            result = result.replace("<query>", tmp_query)
            results = results + result

        ctx.content = ctx.content.replace(f"<{self.name}:list>", results)
        ctx.content = ctx.content.replace(f"<{self.name}:count>", str(len(query_results)))