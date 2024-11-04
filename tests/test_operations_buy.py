"""
Test the buy operation module.
"""

import pytest
from decimal import Decimal

from capital_gains.models import OperationModel, OperationType, ResultModel
from capital_gains.operations.buy import BuyOperation
from capital_gains.states.portfolio import PortfolioState

@pytest.mark.parametrize(
    "operation, state, expected_state, expected_result",
    [
        (
            OperationModel(operation=OperationType.BUY, quantity=10, unit_cost=Decimal("100")),
            PortfolioState(total_shares=0, average_cost=Decimal("0")),
            PortfolioState(total_shares=10, average_cost=Decimal("100")),
            ResultModel(tax=Decimal("0"))
        ),
        (
            OperationModel(operation=OperationType.BUY, quantity=5, unit_cost=Decimal("200")),
            PortfolioState(total_shares=10, average_cost=Decimal("100")),
            PortfolioState(total_shares=15, average_cost=Decimal("100") + Decimal("100") / Decimal("3")),
            ResultModel(tax=Decimal("0"))
        ),
    ]
)
def test_process_operation(
    operation: OperationModel,
    state: PortfolioState,
    expected_state: PortfolioState,
    expected_result: ResultModel
):
    """
    Test processing a buy operation.

    Parameters:
        operation (OperationModel): The operation details.
        state (PortfolioState): The initial state of the portfolio.
        expected_state (PortfolioState): The expected state of the portfolio after processing.
        expected_result (ResultModel): The expected result of processing the operation.

    Raises:
        AssertionError: The results of processing the operations do not match the expected results.
    """

    operation_handler = BuyOperation()
    result = operation_handler.process(operation, state)

    assert state.total_shares == expected_state.total_shares
    assert state.average_cost == expected_state.average_cost
    
    assert result.tax == expected_result.tax
