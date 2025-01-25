import click
import os
import Lynx.utils.config as config

from Lynx import cli
from Lynx.utils.log import *
from Lynx.utils.language import cpp
from Lynx.utils.constants import CPP_STANDARDS, CHECKERS, VALIDATORS


@cli.command()
@click.argument("problem", type=click.Path())
@click.option(  # language
    "--language",
    default="c++14",
    help="The language (standard) used when generating data.",
    type=click.Choice(CPP_STANDARDS),
)
@click.option(  # checker
    "--checker",
    type=click.Choice(CHECKERS),
    default="custom",
    help="Use a checker (special judge). You can specify the checker provided by testlib or use your customized checker by default.",
)
@click.option(  # validator
    "--validator",
    type=click.Choice(VALIDATORS),
    default="custom",
    help="Use a validator. You can also use the validator provided by testlib in a similar way as the checker.",
)
@click.option("--testcase", type=int, default=20, help="The number of testcases.")
@click.option(
    "--time-limit",
    type=int,
    default=1000,
    help="The time limit of the problem, uses ms as unit.",
)
@click.option(
    "--memory-limit",
    type=int,
    default=512,
    help="The memory limit of the problem, uses MB as unit.",
)
# no checker
@click.option(
    "--no-checker",
    is_flag=True,
    default=False,
    help="Do not use a checker (special judge).",
)
def init(
    problem,
    language,
    checker,
    validator,
    testcase,
    time_limit,
    memory_limit,
    no_checker,
):
    """This command initializes a lynx problem directory."""
    # Turn the problem path into an absolute path
    if not os.path.isabs(problem):
        problem = os.path.join(os.getcwd(), problem)
    debug(f"problem route is {problem}")
    if os.path.exists(problem):
        error_and_exit(f"Problem directory {problem} already exists.")
    if language in CPP_STANDARDS:
        cpp.init_problem(
            problem,
            language,
            checker,
            validator,
            testcase,
            time_limit,
            memory_limit,
            no_checker,
        )
    else:  # Other languages will be supported in the future
        assert False  # This should never happen
