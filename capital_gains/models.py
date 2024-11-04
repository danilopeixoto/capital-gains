"""
Models module.

This module defines the data models used in the application for
representing financial operations and calculations. Each model is
built with data validation and serialization, providing a robust
foundation for handling structured data within the system.
"""

from decimal import ROUND_HALF_UP, Decimal
from enum import Enum

from pydantic import BaseModel, Field, model_validator


class OperationType(str, Enum):
    """
    Enumeration for financial operation types.
    """

    BUY = "buy"
    SELL = "sell"


class BaseDecimalModel(BaseModel):
    """
    Base model for handling decimal attributes with automatic rounding.
    """

    class Config:
        """
        Model configuration settings.
        """

        #: Custom JSON encoder to prevent Decimal values from being serialized as strings.
        json_encoders = {
            Decimal: lambda x: float(x)  # pylint: disable=unnecessary-lambda
        }

        #: Populate model attributes by name.
        populate_by_name = True

    @model_validator(mode="after")
    def validate_and_round_decimal_values(self) -> "BaseDecimalModel":
        """
        Validate and round all decimal values in the model.

        This method ensures that all decimal values are rounded to two
        decimal places using the `ROUND_HALF_UP` rounding strategy.

        Returns:
            BaseDecimalModel: The validated and rounded model.
        """

        for name, value in self:
            if isinstance(value, Decimal):
                # Round financial values to two decimal places.
                setattr(
                    self, name, value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                )

        return self


class OperationModel(BaseDecimalModel):
    """
    Model representing a financial operation.
    """

    #: The type of operation.
    operation: OperationType

    #: The quantity of shares traded in the operation.
    quantity: int

    #: The unit price of the stock.
    unit_cost: Decimal = Field(..., alias="unit-cost")


class ResultModel(BaseDecimalModel):
    """
    Model representing a calculation result.
    """

    #: Results of a tax calculation.
    tax: Decimal
