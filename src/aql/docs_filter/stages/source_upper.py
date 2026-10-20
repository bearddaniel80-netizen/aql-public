from .base import BaseReplace

from ..registry import pattern

@pattern([
    "<source:upper>"
])
class SourceUpperReplace(BaseReplace):
    def content_replace(self, ctx):
        ctx.content = ctx.content.replace("<source:upper>", ctx.name.upper())