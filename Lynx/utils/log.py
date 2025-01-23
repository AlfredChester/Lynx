import click
from Lynx.utils.constants import VERBOSE


def error(message: str) -> None:
    """Print an error message."""
    click.echo(click.style(f"ERROR: {message}", fg="red"))


def error_and_exit(message: str, code: int = 1) -> None:
    """Print an error message and exit."""
    error(message)
    raise click.exceptions.Exit(code)


def debug(message: str) -> None:
    """Print a debug message."""
    if VERBOSE:
        click.echo(click.style(f"DEBUG: {message}", fg="blue"))
