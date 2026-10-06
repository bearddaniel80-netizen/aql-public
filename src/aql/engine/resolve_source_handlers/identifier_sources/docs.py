from ....schema.describe import DescribeStage
from ....schema.show import ShowStage
from ....schema.runner import Pipeline
from ..registry_identifier import register_source
from .base import IdentifierSource

@register_source(name="docs")
class DocsSource(IdentifierSource):
    def describe(self, engine_context, inspector):
        from ....docs.factory import DocumentationFactory
        from ....docs.model import QueryClassification
        all_queries = []
        query_results = DocumentationFactory().create().queries_classification

        for k, v in query_results.items():
            queries = [q.to_dict() for q in v]
            all_queries.extend(queries)

        data = all_queries
        pipeline = Pipeline([
            DescribeStage(engine_context, inspector, QueryClassification)
        ])
        return pipeline.run(data)
    
    def query(self):
        from ....docs.factory import DocumentationFactory
        from ....docs.model import QueryClassification
        all_queries = []
        query_results = DocumentationFactory().create().queries_classification

        for k, v in query_results.items():
            queries = [q.to_dict() for q in v]
            all_queries.extend(queries)

        return all_queries

    def show(self):
        from ....docs.factory import DocumentationFactory
        from ....docs.model import QueryClassification
        all_queries = []
        query_results = DocumentationFactory().create().queries_classification

        for k, v in query_results.items():
            queries = [q.to_dict() for q in v]
            all_queries.extend(queries)

        data = all_queries

        pipeline = Pipeline([
            ShowStage(data),
        ])

        return pipeline.run(data)