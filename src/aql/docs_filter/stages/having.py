from .base import BaseReplace
from aql_link.filter.filter_dict import Filter

# replace placeholder <having:single>
class HavingReplace(BaseReplace):
    def content_replace(self, ctx):

        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").where("clauses", "AND").where("clauses", "HAVING").first().get_source()
        ctx.content = ctx.content.replace("<having:op:and>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").where("clauses", "OR").where("clauses", "HAVING").first().get_source()
        ctx.content = ctx.content.replace("<having:op:or>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").where("clauses", "NOT").where("clauses", "HAVING").first().get_source()
        ctx.content = ctx.content.replace("<having:neg>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "*").where("clauses", "HAVING").first().get_source()
        ctx.content = ctx.content.replace("<having:star>", query)
        
        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").where("clauses", "HAVING").first().get_source()
        ctx.content = ctx.content.replace("<having:single>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "True").where("fields", "name").where("clauses", "HAVING").first().get_source()
        ctx.content = ctx.content.replace("<having:cte>", query)