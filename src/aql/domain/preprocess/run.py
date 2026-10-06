from pathlib import Path

from ...preprocess.factory import Preprocessor
from ...preprocess.models import SourceLoader

def main(filename: str):
    path = Path.cwd() / filename
    source_loader = SourceLoader()
    preprocess_ctx = Preprocessor(source_loader).process(path)
    return " ".join(preprocess_ctx.source)