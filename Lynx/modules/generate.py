import click
import os
import Lynx.utils.config as config

from Lynx import cli
from Lynx.utils.compile import cpp
from Lynx.utils.constants import SUPPORTED_OJ


@cli.command()
@click.argument("problem", type=click.Path())
@click.option(
    "--oj",
    type=click.Choice(SUPPORTED_OJ),
    default="hydro",
    help="The online judge to upload the problem to, used when packing data.",
)
def generate(problem, oj):
    """This command generates testcases of a lynx problem."""
    # check if the problem directory exists
    pass
