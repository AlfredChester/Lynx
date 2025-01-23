import click
import os
import random
import Lynx.utils.config as config

from cyaron import *
from Lynx import cli
from Lynx.utils.language import cpp
from Lynx.utils.constants import SUPPORTED_OJ

# Warning: This may cause security risks. We should try to replace it.
from importlib import import_module


@cli.command()
@click.argument("problem", type=click.Path())
@click.option(
    "--oj",
    type=click.Choice(SUPPORTED_OJ),
    default="hydro",
    help="The online judge to upload the problem to, used when packing data.",
)
@click.option(
    "--seed",
    type=int,
    required=False,
    help="The random seed to specify (optional).",
)
@click.option(
    "--no-validate",
    is_flag=True,
    default=False,
    help="Not to validate when generating data.",
)
def generate(problem, oj, seed, no_validate):
    """This command generates testcases of a lynx problem."""
    # check if the problem directory exists
    if seed is not None:
        random.seed(seed)  # Write unit tests for setting seed.

    # maybe you forget to specify --no-validator?
    pass
