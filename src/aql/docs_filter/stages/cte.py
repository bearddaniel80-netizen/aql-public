from .base import BaseReplace
from aql_link.filter.filter_dict import Filter

# replace placeholder <cte>
class CteReplace(BaseReplace):
    def content_replace(self, ctx):
        query = Filter().from_source(ctx.queries).where("is_cte", "True").where("fields", "*").first().get_source()
        ctx.content = ctx.content.replace("<cte:star>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "True").where("fields", "name").first().get_source()
        ctx.content = ctx.content.replace("<cte:single>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "True").where("fields", "name").where("clauses", "AND").first().get_source()
        ctx.content = ctx.content.replace("<cte:op:and>", query)
        
        query = Filter().from_source(ctx.queries).where("is_cte", "True").where("fields", "name").where("clauses", "OR").first().get_source()
        ctx.content = ctx.content.replace("<cte:op:or>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "True").where("fields", "name").where("clauses", "NOT").first().get_source()
        ctx.content = ctx.content.replace("<cte:neg>", query)