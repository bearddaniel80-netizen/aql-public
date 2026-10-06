from .base import FilterReplace
from .strategies.source_strategy import SourceStrategy
from ..registry import pattern

@pattern(markers=["<source:upper>", "<source>"])
class SourceReplace(FilterReplace):
    
    def __init__(self):
        super().__init__(SourceStrategy())
