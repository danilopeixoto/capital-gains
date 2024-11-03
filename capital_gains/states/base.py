"""
Base state module.

This module defines the abstract class for representing and managing
states within the system. It provides the class `BaseState`, which can
be extended to create specific state implementations that encapsulate
the behavior and properties of different states in the application.
"""

from abc import ABC


class BaseState(ABC):
    """
    Abstract base class for representing a state in the system.

    This class serves as a foundational building block for more specific
    state implementations. It can be extended to define various types of
    states that the system may encounter.
    """

    pass
