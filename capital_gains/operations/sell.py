"""
Sell operation module.

This module defines the `SellOperation` class, which represents the
process of selling assets within the financial system. It extends
the `BaseOperation` class and implements the logic required to
process sell transactions while updating the portfolio state.
"""

from decimal import Decimal
from .base import BaseOperation
from ..models import OperationModel, ResultModel
from ..states import PortfolioState


class SellOperation(BaseOperation):
    """
    Class representing a sell operation.

    This class implements the logic for executing a sell transaction,
    updating the portfolio's total shares, calculating profits or losses,
    and determining the applicable tax based on the sale.
    """

    #: The threshold for exempting a sale value from taxation.
    exempt_tax_sale_threshold: Decimal = 20000

    #: The percentage rate at which tax is applied to profits.
    tax_percentage: Decimal = 0.2

    def process(self, operation: OperationModel, state: PortfolioState) -> ResultModel:
        """
        Process a sell operation.

        This method updates the portfolio based on the sale of shares,
        calculates profit or loss, and determines the tax owed, if any.

        Parameters:
            operation (OperationModel): The operation details.
            state (PortfolioState): The current state of the portfolio.

        Returns:
            ResultModel: The result of processing the operation.
        """

        # Decrease the total shares in the portfolio by the quantity sold.
        state.total_shares -= operation.quantity

        # Calculate the sale value based on operation details.
        sale_value = operation.quantity * operation.unit_cost

        # Calculate the cost value based on average cost to verify profit or loss.
        cost_value = operation.quantity * state.average_cost

        # Calculate the profit or loss from the sale value.
        profit = sale_value - cost_value

        # If there is no profit or a loss, apply the loss to total loss and return no tax.
        if profit <= 0:
            # This loss will be reduced from subsequent profits.
            state.total_loss -= profit

            return ResultModel(tax=0)

        # If the total sale value is less than or equal to the exempt threshold, return no tax.
        if sale_value <= self.exempt_tax_sale_threshold:
            return ResultModel(tax=0)

        # Calculate taxable profit after accounting for previous losses, and
        # update total loss, reducing it by the profit realized from this sale.
        taxable_profit = max(0, profit - state.total_loss)
        state.total_loss = max(0, state.total_loss - profit)

        # If there is taxable profit, calculate the tax owed using tax percentage rate and return it.
        if taxable_profit > 0:
            return ResultModel(tax=taxable_profit * self.tax_percentage)

        # Otherwise return no tax.
        return ResultModel(tax=0)
