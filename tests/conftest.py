"""
Test configuration module.
"""

import os

import pytest
from typer import Typer
from typer.testing import CliRunner

from capital_gains.cli import app


@pytest.fixture
def data_path() -> str:
    """
    Provides the path to the directory containing data for testing.

    Returns:
        str: The path to the test data directory.
    """

    return os.path.join(os.path.dirname(__file__), "data")


@pytest.fixture
def cli_app() -> Typer:
    """
    Provides the Typer application instance for testing.

    Returns:
        Typer: The application instance for executing tests.
    """

    return app


@pytest.fixture
def cli_runner() -> CliRunner:
    """
    Provides a CLI testing runner for executing command-line interface
    commands during tests.

    Returns:
        CliRunner: An instance of runner for testing CLI commands.
    """

    return CliRunner()
