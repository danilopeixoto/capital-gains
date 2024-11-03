"""
Base operation module.

This module defines the abstract base class for all financial operations
within the calculation system. It provides a common interface for
specific operation implementations, ensuring that all operations can be
processed uniformly.
"""

from abc import ABC, abstractmethod

from ..states import BaseState
from ..models import OperationModel, ResultModel


class BaseOperation(ABC):
    """
    Abstract base class for financial operations.

    This class defines the structure that all specific operation classes
    (e.g., `BuyOperation`, `SellOperation`) must implement. It ensures that
    each operation can be processed in a consistent manner, regardless
    of the operation type.
    """

    @abstractmethod
    def process(self, operation: OperationModel, state: BaseState) -> ResultModel:
        """
        Process a financial operation.

        This method must be implemented by subclasses to define how to
        execute a specific operation type and update the given state.

        Parameters:
            operation (OperationModel): The operation details.
            state (BaseState): The current state of the calculation.

        Returns:
            ResultModel: The result of processing the operation.
        """

        pass
