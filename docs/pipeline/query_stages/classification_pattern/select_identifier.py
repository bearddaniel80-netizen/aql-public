from .base import ParserPattern
from ..registry_classification import pattern
from ....model import QueryClassification
from .....language.ast.function_call import FunctionCall

@pattern([
    FunctionCall,
])
class SelectIdentifier(ParserPattern):
    def build(self, classifier: QueryClassification):
        identifier = self.window[0]
        if identifier.alias:
            classifier.fields_alias.append(identifier.alias)