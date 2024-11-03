"""
Operations module.

This module defines various types of financial operations that can be
performed within the calculation system. It includes base classes and
specific implementations for different operation types, such as buying
and selling assets.

"""

from .base import BaseOperation
from .buy import BuyOperation
from .sell import SellOperation
