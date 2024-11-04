"""
Calculators module.

This module defines the core functionalities related to financial
calculations, including tax computations based on operations
performed within the investment system. It imports the base calculator
class, `BaseCalculator`, which provides a common interface for
calculators, and the `TaxCalculator`, which implements the specific
logic for calculating taxes based on financial operations and
portfolio state.
"""

from .base import BaseCalculator
from .tax import TaxCalculator
