from pathlib import Path
from aql_link.writter.artifacts.file import FileArtifact
from .model import DOCUMENTATION, DestinationType
from .context import FilterContext
from .registry import STAGE_REGISTRY
from . import stages

class DocumentationFilter:
    def source(self, name, queries):
        ctx = FilterContext(name=name,destination=DestinationType.SOURCES,queries=queries)
        
        artifact=self._render(ctx, "source")
        
        self._write(ctx.destination, artifact)

    def all_features(self, queries):
        for key in DOCUMENTATION.keys():
            self.feature(key, queries)

    def feature(self, name, queries):
        config = DOCUMENTATION[name]

        ctx = FilterContext(
            name=name,
            destination=config["destination"],
            queries=queries,
        )

        ctx.content = self._load_template(config["template"])

        for stage in STAGE_REGISTRY:
            if stage.has_marker(ctx.content):
                stage.content_replace(ctx)

        self._write(
            ctx.destination,
            FileArtifact(
                output_file=f"{name}.md",
                content=ctx.content,
            )
        )
        
    def _load_template(self, name: str) -> str:
        path = Path.cwd() / "doc_templates" / name
        return path.read_text(encoding="utf-8")
    
    def _render(self, ctx, template_name):
        ctx.content = self._load_template(template_name)

        for stage in STAGE_REGISTRY:
            if stage.has_marker(ctx.content):
                stage.content_replace(ctx)

        return FileArtifact(
            output_file=f"{ctx.name}.md",
            content=ctx.content,
        )

    def _write(
        self,
        destination,
        artifact,
    ):

        file_path = Path.cwd() / destination

        file_path.mkdir(parents=True, exist_ok=True)

        file_path = file_path.joinpath(artifact.output_file)

        if artifact.binary:

            file_path.write_bytes(
                artifact.content
            )

        else:

            file_path.write_text(
                artifact.content,
                encoding="utf-8",
            )

