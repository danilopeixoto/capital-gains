"""
Calculator base module.

This module defines the abstract base class for calculators in the
financial application. It provides a framework for processing
financial operations and managing the associated state.
Specific calculator implementations must inherit from this class
and define their own processing logic for different types of operations.
"""

from abc import ABC, abstractmethod
from typing import Dict, List

from ..operations import BaseOperation

from ..states import BaseState
from ..models import OperationBatchModel, OperationType, ResultBatchModel


class BaseCalculator(ABC):
    """
    Abstract base class for financial calculators.

    This class serves as the foundation for all calculators that
    manage operations on financial data. It holds the current
    state of the financial system and a list of operations to
    be processed.
    """

    #: The current state of the financial system.
    state: BaseState

    #: The operation register.
    operation_register: Dict[OperationType, BaseOperation]

    def __init__(self, state: BaseState, operation_register: Dict[OperationType, BaseOperation]):
        """
        Initialize the base calculator with the given state and operations.

        Parameters:
            state (BaseState): The current state of the financial system.
            operation_register (Dict[OperationType, BaseOperation]): The operation register.
        """

        self.state = state
        self.operation_register = operation_register

    @abstractmethod
    def process(self, operations: OperationBatchModel) -> ResultBatchModel:
        """
        Process a batch of operations.

        This abstract method must be implemented by subclasses to
        define the logic for processing a batch of financial
        operations and returning the corresponding results.

        Parameters:
            operations (OperationBatchModel): A model containing a batch of operations to process.

        Returns:
            ResultBatchModel: A model containing the results of the calculations.
        """

        pass
