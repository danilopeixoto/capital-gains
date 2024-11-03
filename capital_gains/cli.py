"""
Command-line interface (CLI) module.

This module provides the command-line interface for the application,
allowing users to interact with the calculation system directly
from the terminal.
"""

import sys
import typer

from . import __version__

from .states import PortfolioState
from .calculators import TaxCalculator
from .models import OperationBatchModel


app = typer.Typer()

@app.command()
def main():
    """
    Process a batch of financial operations from standard input.
    """

    for line in sys.stdin.readlines():
        state = PortfolioState()
        calculator = TaxCalculator(state)

        operations = OperationBatchModel.model_validate_json(line)
        results = calculator.process(operations)

        typer.echo(results.model_dump_json())

@app.command(name="version")
def version():
    """
    Show the version of the application and exit.
    """

    typer.echo(__version__)


if __name__ == "__main__":
    app()
