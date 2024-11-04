"""
Test the portfolio state.
"""

from decimal import Decimal
from typing import List, Tuple
import pytest
from capital_gains.states.portfolio import PortfolioState


def test_initial_state():
    """
    Test the initial state of the portfolio.

    Raises:
        AssertionError: The initial state of the portfolio is not empty.
    """

    portfolio = PortfolioState()

    assert portfolio.total_shares == 0
    assert portfolio.average_cost == 0
    assert portfolio.total_loss == 0

@pytest.mark.parametrize(
    "args",
    [
        (0, Decimal("0"), Decimal("0")),
        (100, Decimal("10"), Decimal("1000")),
        (500, Decimal("25"), Decimal("5000"))
    ],
)
def test_state_initialization(args: Tuple[int, Decimal, Decimal]):
    """
    Test the initialization of the portfolio state.

    Parameters:
        args (Tuple[int, Decimal, Decimal]):
            The arguments to pass to the portfolio state constructor.

    Raises:
        AssertionError: The state of the portfolio does not match the expected values.
    """

    portfolio = PortfolioState(*args)

    assert portfolio.total_shares == args[0]
    assert portfolio.average_cost == args[1]
    assert portfolio.total_loss == args[2]
