class ProjectionStrategy:
    def __init__(self, name_list, filter_base):
        self.name_list = name_list
        self.filter_base = filter_base

    def content_replace(self, ctx):
        for name in self.name_list:
            query = self.filter_base.from_source(ctx.queries).where("is_cte", "False").where("fields", f"{name}").first().get_source()
            ctx.content = ctx.content.replace(f"<field:{name}>", query)
            query = self.filter_base.from_source(ctx.queries).where("is_cte", "True").where("fields", f"{name}").first().get_source()
            ctx.content = ctx.content.replace(f"<cte:{name}>", query)