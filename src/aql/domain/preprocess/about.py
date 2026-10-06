from pathlib import Path

from ...preprocess.factory import Preprocessor
from ...preprocess.about.types import AboutType
from ...preprocess.about.registry import ABOUT_REGISTRY
from ...preprocess.about import pipeline
from ...preprocess.models import SourceLoader, ImportGraph

def main(filename: str, category: AboutType):
    path = Path.cwd() / filename
    source_loader = SourceLoader()
    import_graph = ImportGraph(root=ImportNode(path))
    preprocess_ctx = Preprocessor(source_loader).process(path)
    fn = ABOUT_REGISTRY[category]
    if not fn:
        raise Exception(f"About type {category} no found.")
    fn_cls = fn()
    return fn_cls.process(source_loader)