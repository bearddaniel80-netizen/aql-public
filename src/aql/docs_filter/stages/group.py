from .base import BaseReplace
from aql_link.filter.filter_dict import Filter

# replace placeholder <group:single>
class GroupByReplace(BaseReplace):
    def content_replace(self, ctx):

        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "*").where("clauses", "GROUP BY").first().get_source()
        ctx.content = ctx.content.replace("<group:star>", query)
        
        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").where("clauses", "GROUP BY").first().get_source()
        ctx.content = ctx.content.replace("<group:single>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "True").where("fields", "name").where("clauses", "GROUP BY").first().get_source()
        ctx.content = ctx.content.replace("<group:cte>", query)