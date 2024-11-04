"""
Buy operation module.

This module defines the `BuyOperation` class, which represents the
process of purchasing assets within the financial system. It extends
the `BaseOperation` class and implements the logic required to
process buy transactions while updating the portfolio state.
"""

from decimal import Decimal

from ..models import OperationModel, ResultModel
from ..states import PortfolioState
from .base import BaseOperation


class BuyOperation(BaseOperation[PortfolioState]):
    """
    Class representing a buy operation.

    This class implements the logic for executing a buy transaction,
    updating the portfolio's total shares and average cost based on
    the provided operation details.
    """

    def process(self, operation: OperationModel, state: PortfolioState) -> ResultModel:
        """
        Process a buy operation.

        This method updates the portfolio state with the new total shares
        and average cost, and returns the tax result of the operation.

        Parameters:
            operation (OperationModel): The operation details.
            state (PortfolioState): The current state of the portfolio.

        Returns:
            ResultModel: The result of processing the operation.
        """

        total_cost = (state.total_shares * state.average_cost) + (
            operation.quantity * operation.unit_cost
        )

        # Increase the total shares in the portfolio by the quantity bought.
        state.total_shares += operation.quantity

        # Calculate the average cost per share.
        state.average_cost = total_cost / state.total_shares

        # No tax for buy operations.
        return ResultModel(tax=Decimal("0"))
