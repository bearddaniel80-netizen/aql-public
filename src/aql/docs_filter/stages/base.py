class BaseReplace:

    markers = ()
    words = []
    def content_replace(self, ctx):
        pass

    def has_marker(self, content):
        self.words = []
        is_marked = False
        for marker in self.markers:
            if marker in content:
                self.words.append(marker)
                is_marked = True

        return is_marked
        
class FilterReplace(BaseReplace):

    def __init__(self, instance):
        self.instance = instance


    def content_replace(self, ctx):
        self.instance.content_replace(ctx)