from .base import BaseReplace
from aql_link.filter.filter_dict import Filter

# replace placeholder <field:single>
class FieldSingleReplace(BaseReplace):
    def content_replace(self, ctx):
        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").first().get_source()
        ctx.content = ctx.content.replace("<field:single>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").where("clauses", "AND").first().get_source()
        ctx.content = ctx.content.replace("<op:and:single>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").where("clauses", "OR").first().get_source()
        ctx.content = ctx.content.replace("<op:or:single>", query)

        query = Filter().from_source(ctx.queries).where("is_cte", "False").where("fields", "name").where("clauses", "NOT").first().get_source()
        ctx.content = ctx.content.replace("<neg:single>", query)