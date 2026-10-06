class SourceStrategy:

    def content_replace(self, ctx):
        ctx.content = ctx.content.replace("<source:upper>", ctx.name.upper())
        ctx.content = ctx.content.replace("<source>", ctx.name)