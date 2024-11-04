"""
Calculator base module.

This module defines the abstract base class for calculators in the
financial application. It provides a framework for processing
financial operations and managing the associated state.
Specific calculator implementations must inherit from this class
and define their own processing logic for different types of operations.
"""

from abc import ABC, abstractmethod
from typing import Dict, Generator, Generic, List, TypeVar

from ..models import OperationModel, OperationType, ResultModel
from ..operations import BaseOperation

StateTypeT = TypeVar("StateTypeT")


class BaseCalculator(ABC, Generic[StateTypeT]):
    """
    Abstract base class for financial calculators.

    This class serves as the foundation for all calculators that
    manage operations on financial data. It holds the current
    state of the financial system and a list of compatible operations to
    be processed.
    """

    #: The current state of the financial system.
    state: StateTypeT

    #: The operation register.
    operation_register: Dict[OperationType, BaseOperation[StateTypeT]]

    def __init__(
        self,
        state: StateTypeT,
        operation_register: Dict[OperationType, BaseOperation[StateTypeT]],
    ):
        """
        Initialize the base calculator with the given state and operations.

        Parameters:
            state (StateTypeT): The current state of the financial system.
            operation_register (Dict[OperationType, BaseOperation[StateTypeT]]):
                The operation register.
        """

        self.state = state
        self.operation_register = operation_register

    @abstractmethod
    def process(
        self, operations: List[OperationModel]
    ) -> Generator[ResultModel, None, None]:
        """
        Process a batch of operations.

        This abstract method must be implemented by subclasses to
        define the logic for processing a batch of financial
        operations and yielding the corresponding results.

        Parameters:
            operations (List[OperationModel]): A batch of operations to process.

        Returns:
            Generator[ResultModel, None, None]:
                A generator yielding the results of the calculations.
        """
