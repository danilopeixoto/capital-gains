import os

from typer import Typer
from typer.testing import CliRunner

import pytest


pytest.mark.parametrize(
    "input_filename, output_filename",
    [
        ("input.0.jsonl", "output.0.jsonl"),
        ("input.1.jsonl", "output.1.jsonl"),
        ("input.2.jsonl", "output.2.jsonl"),
        ("input.3.jsonl", "output.3.jsonl"),
        ("input.4.jsonl", "output.4.jsonl"),
        ("input.5.jsonl", "output.5.jsonl"),
        ("input.6.jsonl", "output.6.jsonl"),
        ("input.7.jsonl", "output.7.jsonl"),
        ("input.8.jsonl", "output.8.jsonl"),
        ("input.9.jsonl", "output.9.jsonl")
    ]
)
def test_use_cases(
    input_filename: str,
    output_filename: str,
    data_path: str,
    app: Typer,
    runner: CliRunner
):
    """
    Test CLI application with various input-output use cases.

    This function runs the CLI application using different input files
    and compares the generated output with expected output files.

    Parameters:
        input_filename (str): The name of the input JSONL file to test.
        output_filename (str): The name of the expected output JSONL file.
        data_path (str): The path to the directory containing the input and output files.
        app (Typer): The CLI application instance used for testing.
        runner (CliRunner): The CLI testing runner for invoking commands.

    Asserts:
        The output produced by the CLI application matches the expected output.
    """

    input_filepath = os.path.join(data_path, input_filename)
    output_filepath = os.path.join(data_path, output_filename)

    with open(input_filepath, "r", encoding="utf-8") as input_file:
        input_data = input_file.read()

    with open(output_filepath, "r", encoding="utf-8") as output_file:
        expected_output_data = output_file.read()

    result = runner.invoke(app, input=input_data)
    output_data = result.stdout

    assert output_data == expected_output_data
