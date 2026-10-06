from aql_link.filter.filter_dict import Filter

class QueryStrategy:
    def __init__(self, filter_dict):
        self.filter_dict = filter_dict

    def content_replace(self, ctx):
        for k, v in self.filter_dict.items():
            query = self._build_query(ctx, v)
            ctx.content = ctx.content.replace(f"<{k}>", query)

    def _build_query(self, ctx, filter_lst):
        query = Filter().from_source(ctx.queries)
        for item in filter_lst:
            query = query.where(item["attr"], item["value"])
        query = query.first().get_source()
        return query