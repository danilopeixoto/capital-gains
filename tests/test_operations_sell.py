"""
Test the sell operation module.
"""

import pytest
from decimal import Decimal

from capital_gains.models import OperationModel, OperationType, ResultModel
from capital_gains.operations.sell import SellOperation
from capital_gains.states.portfolio import PortfolioState

@pytest.mark.parametrize(
    "operation, state, expected_state, expected_result",
    [
        (
            OperationModel(operation=OperationType.SELL, quantity=10, unit_cost=Decimal("100")),
            PortfolioState(total_shares=10, average_cost=Decimal("100"), total_loss=Decimal("100")),
            PortfolioState(total_shares=0, average_cost=Decimal("100"), total_loss=Decimal("100")),
            ResultModel(tax=Decimal("0"))
        ),
        (
            OperationModel(operation=OperationType.SELL, quantity=200000, unit_cost=Decimal("500")),
            PortfolioState(total_shares=200000, average_cost=Decimal("200"), total_loss=Decimal("0")),
            PortfolioState(total_shares=0, average_cost=Decimal("200"), total_loss=Decimal("0")),
            ResultModel(tax=Decimal("12000000"))
        ),
        (
            OperationModel(operation=OperationType.SELL, quantity=50, unit_cost=Decimal("30")),
            PortfolioState(total_shares=100, average_cost=Decimal("200"), total_loss=Decimal("1000")),
            PortfolioState(total_shares=50, average_cost=Decimal("200"), total_loss=Decimal("9500")),
            ResultModel(tax=Decimal("0"))
        ),
        (
            OperationModel(operation=OperationType.SELL, quantity=50, unit_cost=Decimal("3000")),
            PortfolioState(total_shares=100, average_cost=Decimal("200"), total_loss=Decimal("1000")),
            PortfolioState(total_shares=50, average_cost=Decimal("200"), total_loss=Decimal("0")),
            ResultModel(tax=Decimal("27800"))
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
    Test processing a sell operation.

    Parameters:
        operation (OperationModel): The operation details.
        state (PortfolioState): The initial state of the portfolio.
        expected_state (PortfolioState): The expected state of the portfolio after processing.
        expected_result (ResultModel): The expected result of processing the operation.

    Raises:
        AssertionError: The results of processing the operations do not match the expected results.
    """

    operation_handler = SellOperation()
    result = operation_handler.process(operation, state)

    assert state.total_shares == expected_state.total_shares
    assert state.average_cost == expected_state.average_cost
    assert state.total_loss == expected_state.total_loss

    assert result.tax == expected_result.tax
