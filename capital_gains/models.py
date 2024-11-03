"""
Models module.

This module defines the data models used in the application for
representing financial operations and calculations. Each model is
built with data validation and serialization, providing a robust
foundation for handling structured data within the system.
"""

from decimal import Decimal
from enum import Enum
from typing import List
from pydantic import BaseModel, condecimal


class OperationType(str, Enum):
    """
    Enumeration for financial operation types.
    """

    BUY = "buy"
    SELL = "sell"

class OperationModel(BaseModel):
    """
    Model representing a financial operation.
    """

    #: The type of operation.
    operation: OperationType

    #: The quantity of shares traded in the operation.
    quantity: int

    #: The unit price of the stock in currency with two decimal places.
    unit_cost: Decimal = condecimal(max_digits=10, decimal_places=2, alias="unit-cost")

class ResultModel(BaseModel):
    """
    Model representing a calculation result.
    """

    #: Results of a tax calculation.
    tax: Decimal = condecimal(max_digits=10, decimal_places=2)


class OperationBatchModel(BaseModel):
    """
    Model representing a batch of financial operations.
    """

    #: A list of financial operations.
    batch: List[OperationModel]


class ResultBatchModel(BaseModel):
    """
    Model representing a batch of calculation results.
    """

    #: A list of calculation results.
    batch: List[ResultModel]
