from ....schema.describe import DescribeStage
from ....schema.show import ShowStage
from ....schema.runner import Pipeline
from ..registry_identifier import register_source
from .base import IdentifierSource

@register_source(name="docs_filter")
class DocsFilterSource(IdentifierSource):
    def describe(self, engine_context, inspector):
        from ....docs_filter.model import System

        data = self._build_data()
        
        pipeline = Pipeline([
            DescribeStage(engine_context, inspector, System)
        ])
        return pipeline.run(data)
    
    def query(self):
        return self._build_data()

    def show(self):
        data = self._build_data()

        pipeline = Pipeline([
            ShowStage(data),
        ])

        return pipeline.run(data)

    def _build_data(self):
        from ....docs_filter.model import DOCUMENTATION
        return [ item.to_dict() for item in DOCUMENTATION.values()]
