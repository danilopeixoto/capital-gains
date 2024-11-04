"""
Tax calculator module.

This module provides the `TaxCalculator` class, which is responsible for calculating
tax obligations based on financial operations related to buying and selling assets.
It uses specific strategies for each type of operation and maintains the state of a
financial portfolio throughout the calculations.
"""

from typing import Generator, List

from ..models import OperationModel, OperationType, ResultModel
from ..operations import BuyOperation, SellOperation
from ..states import PortfolioState
from .base import BaseCalculator


class TaxCalculator(BaseCalculator[PortfolioState]):
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
            {OperationType.BUY: BuyOperation(), OperationType.SELL: SellOperation()},
        )

    def process(
        self, operations: List[OperationModel]
    ) -> Generator[ResultModel, None, None]:
        """
        Process a batch of operations and calculate taxes.

        Parameters:
            operations (List[OperationModel]): A batch of operations to process.

        Returns:
            Generator[ResultModel, None, None]:
                A generator yielding the results of the calculations.
        """

        for operation in operations:
            operation_handler = self.operation_register[operation.operation]
            yield operation_handler.process(operation, self.state)
