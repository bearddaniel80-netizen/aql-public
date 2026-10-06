STAGE_REGISTRY = []

def pattern(markers):
    def decorator(cls):
        STAGE_REGISTRY.append(cls())
        cls.markers = markers
        return cls
    return decorator