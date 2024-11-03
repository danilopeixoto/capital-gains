"""
Portfolio state module.

This module defines the `PortfolioState` class, which represents a financial
portfolio in the system. It extends the base `BaseState` class, allowing
for specific state management related to investment holdings and performance.
"""

from decimal import Decimal

from .base import BaseState

class PortfolioState(BaseState):
    """
    Represents a financial portfolio in the investment system.

    This class is designed to manage and track various attributes related
    to a financial portfolio, including the total number of shares,
    the average cost per share, and the total loss over time.
    """

    #: The total number of shares.
    total_shares: int

    #: The average cost per share.
    average_cost: Decimal

    #: The total loss incurred over time.
    total_loss: Decimal


    def __init__(self):
        """
        Initialize a new instance of the portfolio state class.

        This constructor sets the initial values for total shares, average
        cost, and total loss to zero, indicating an empty portfolio at
        the time of creation.
        """

        self.total_shares = 0
        self.average_cost = 0
        self.total_loss = 0
