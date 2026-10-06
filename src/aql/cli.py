import typer
from rich import print_json
from pathlib import Path

from .preprocess.about.types import AboutType
from .domain.query import query_results
from .domain.preprocess.about import main as about_main
from .domain.preprocess.run import main as run_main

app = typer.Typer(help="AQL query everything.")

@app.command(help="Get metadata on script files")
def about(
    filename: str = typer.Argument(
        ...,
        help="AQL file name or path info",
    ),
    category: AboutType = typer.Option(
        AboutType.SOURCE,
        "--category",
        help="Output category"
    ),
):
    # typer.echo(f"About: {filename}")
    result = about_main(filename, category)
    print_json(data=result)

@app.command(help="Create documentation from source")
def docs():
    # typer.echo("Writing docs")
    from .docs_filter.documentation_filter import DocumentationFilter
    from .docs.factory import DocumentationFactory

    _filter = DocumentationFilter()
    query_results = DocumentationFactory().create().queries_classification

    for k, v in query_results.items():
        queries = [q.to_dict() for q in v]
        _filter.source(k, queries)
        if k == "json":
            _filter.all_features(queries)

@app.command(help="Single line queries")
def query(
    q: str = typer.Argument(
        ...,
        help="AQL query string",
    )
):
    # typer.echo(f"Query: {q}")
    query_results(q)

@app.command(help="Run a aql script file")
def run(
    filename: str = typer.Argument(
        ...,
        help="AQL file name or path",
    )
):
    # typer.echo(f"Run: {filename}")

    data = run_main(filename)
    query_results(data)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context, script: Path | None = None):
    # print(f"{script} as a linux shell script.")
    if script:
        run(script)