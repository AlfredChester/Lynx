import click
import os
import Lynx.utils.config as config

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
    # check if the problem directory exists
    pass
