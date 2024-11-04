"""
Command-line interface (CLI) module.

This module provides the command-line interface for the application,
allowing users to interact with the calculation system directly
from the terminal.
"""

import sys
from typing import List

import typer
from pydantic import TypeAdapter

from . import __version__
from .calculators import TaxCalculator
from .models import OperationModel, ResultModel
from .states import PortfolioState

app = typer.Typer(add_completion=False)


@app.callback(invoke_without_command=True)
def main(context: typer.Context):
    """
    Process a batch of financial operations from standard input.

    Example: capital-gains < input.jsonl > output.jsonl
    """

    if context.invoked_subcommand is not None:
        return

    for json_operations in sys.stdin:
        # Reset the state and calculator for each line of input.
        state = PortfolioState()
        calculator = TaxCalculator(state)

        operations = TypeAdapter(List[OperationModel]).validate_json(json_operations)
        results = list(calculator.process(operations))

        typer.echo(TypeAdapter(List[ResultModel]).dump_json(results))


@app.command()
def version():
    """
    Show the version of the application and exit.
    """

    typer.echo(__version__)


if __name__ == "__main__":
    app()
