import click
import os
import Lynx.utils.config as config

from Lynx import cli
from Lynx.utils.language import cpp


@cli.command()
@click.argument("problem", type=click.Path())
@click.argument("program1", type=click.File("r"))
@click.argument("program2", type=click.File("r"), required=False)
@click.option(
    "--testcase", type=int, default=0, help="The index of the testcase to compare."
)
# checker will be supported in the future when cyaron implements it.
# @click.option(
#     "--checker",
#     is_flag=True,
#     default=False,
#     help="Use checker (special judge).",
# )
def compare(problem, program1, program2, testcase):
    """This command compares two programs using a lynx problem description.

    PROBLEM is the lynx problem directory.

    PROGRAM1 is the program to compare with.

    PROGRAM2 is the second program to compare with, it is set to the standard solution to the problem by default.
    """
    pass
