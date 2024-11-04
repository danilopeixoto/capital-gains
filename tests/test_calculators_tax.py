"""
Test the tax calculator module.
"""

from decimal import Decimal
from typing import List
from unittest.mock import MagicMock

import pytest

from capital_gains.calculators.tax import TaxCalculator
from capital_gains.models import OperationModel, OperationType, ResultModel
from capital_gains.states.portfolio import PortfolioState


@pytest.mark.parametrize(
    "operation_types, expected_tax_results",
    [
        ([], []),
        ([OperationType.BUY], [Decimal("0")]),
        ([OperationType.BUY, OperationType.SELL], [Decimal("0"), Decimal("1")]),
        ([OperationType.SELL, OperationType.BUY], [Decimal("1"), Decimal("0")]),
        (
            [OperationType.BUY, OperationType.SELL, OperationType.BUY],
            [Decimal("0"), Decimal("1"), Decimal("0")],
        ),
    ],
)
def test_process_operations(
    operation_types: List[OperationType], expected_tax_results: List[Decimal]
):
    """
    Test processing a batch of operations with the tax calculator.

    Parameters:
        operation_types (list[OperationType]): A batch of operation types to process.
        expected_tax_results (list[Decimal]): A list of simplified tax results.

    Raises:
        AssertionError: The results of processing the operations do not match the expected results.
    """

    buy_result = ResultModel(tax=Decimal("0"))
    sell_result = ResultModel(tax=Decimal("1"))

    state = PortfolioState()

    calculator = TaxCalculator(state)
    calculator.operation_register[OperationType.BUY].process = MagicMock(  # type: ignore
        return_value=buy_result
    )
    calculator.operation_register[OperationType.SELL].process = MagicMock(  # type: ignore
        return_value=sell_result
    )

    operations = [
        OperationModel(operation=operation_type, quantity=10, unit_cost=Decimal("10"))
        for operation_type in operation_types
    ]

    tax_results = [result.tax for result in calculator.process(operations)]

    assert tax_results == expected_tax_results
