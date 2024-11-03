"""
Tax calculator module.

This module provides the `TaxCalculator` class, which is responsible for calculating
tax obligations based on financial operations related to buying and selling assets.
It uses specific strategies for each type of operation and maintains the state of a
financial portfolio throughout the calculations.
"""

from ..models import (
    OperationType,
    OperationModel,
    ResultModel,
    OperationBatchModel,
    ResultBatchModel
)
from .base import BaseCalculator
from ..states import PortfolioState
from ..operations import BuyOperation, SellOperation


class TaxCalculator(BaseCalculator):
    """
    A calculator for determining tax obligations based on financial operations.

    This class processes batches of operations and maintains a portfolio state.
    It applies defined strategies for processing buy and sell operations.
    """

    def __init__(self, state: PortfolioState):
        """
        Initialize the tax calculator with a specific portfolio state.

        This also registers the required operations for tax calculations:

        - `BuyOperation`
        - `SellOperation`

        Parameters:
            state (PortfolioState): The initial state of the portfolio to be used in calculations.
        """

        super().__init__(
            state,
            {
                OperationType.BUY: BuyOperation(),
                OperationType.SELL: SellOperation()
            }
        )

    def calculate_tax(self, operation: OperationModel) -> ResultModel:
        """
        Calculate the tax for a specific financial operation.

        This method retrieves the appropriate handler based on the type of operation
        and delegates the processing of the tax calculation to that handler.

        Parameters:
            operation (OperationModel): The operation details.

        Returns:
            ResultModel: The result of processing the operation.
        """

        operation_handler = self.operation_register[operation.operation]
        return operation_handler.process(operation, self.state)

    def process(self, operations: OperationBatchModel) -> ResultBatchModel:
        """
        Process a batch of operations and calculate taxes.

        Parameters:
            operations (OperationBatchModel): A model containing a batch of operations to process.

        Returns:
            ResultBatchModel: A model containing the results of the calculations.
        """

        results = [
            self.calculate_tax(operation)
            for operation in operations.batch
        ]

        return ResultBatchModel(results=results)
