from .base import BaseReplace
from aql_link.filter.filter_dict import Filter
from ..registry import pattern

@pattern([
    "<field:star>", 
    "<op:and:star>",
    "<op:or:star>",
    "<neg:star>"
])
class FieldStarReplace(BaseReplace):
    def content_replace(self, ctx):
        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "*").first().get_source()
        ctx.content = ctx.content.replace("<field:star>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "*").where("clauses", "AND").first().get_source()
        ctx.content = ctx.content.replace("<op:and:star>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "*").where("clauses", "OR").first().get_source()
        ctx.content = ctx.content.replace("<op:or:star>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "*").where("clauses", "NOT").first().get_source()
        ctx.content = ctx.content.replace("<neg:star>", query)