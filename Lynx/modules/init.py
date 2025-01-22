import click
from Lynx import cli
from Lynx.utils.compile import cpp


@cli.command()
@click.argument("problem", type=click.Path())
@click.option(
    "--language",
    default="c++14",
    help="The language used when generating data",
    type=click.Choice(cpp.allowed_standards),
)
def init(problem, language):
    """This command initializes a lynx problem directory"""
    print(type(problem), language)
    pass
