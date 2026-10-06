class BaseReplace:

    def content_replace(self, ctx):
        pass
        
class FilterReplace(BaseReplace):
    markers = ()
    words = []

    def __init__(self, instance):
        self.instance = instance

    def has_marker(self, content):
        self.words = []
        is_marked = False
        for marker in self.markers:
            if marker in content:
                self.words.append(marker)
                is_marked = True

        return is_marked

    def content_replace(self, ctx):
        self.instance.content_replace(ctx)