from .base import BaseReplace
from aql_link.filter.filter_dict import Filter

# replace placeholder <order:single>
class OrderByReplace(BaseReplace):
    def content_replace(self, ctx):
        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").where("clauses", "AND").where("clauses", "ORDER").first().get_source()
        ctx.content = ctx.content.replace("<order:op:and>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").where("clauses", "OR").where("clauses", "ORDER").first().get_source()
        ctx.content = ctx.content.replace("<order:op:or>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").where("clauses", "NOT").where("clauses", "ORDER").first().get_source()
        ctx.content = ctx.content.replace("<order:neg>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "*").where("clauses", "ORDER").first().get_source()
        ctx.content = ctx.content.replace("<order:star>", query)
        
        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").where("clauses", "ORDER").first().get_source()
        ctx.content = ctx.content.replace("<order:single>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "True").where("fields", "name").where("clauses", "ORDER").first().get_source()
        ctx.content = ctx.content.replace("<order:cte>", query)