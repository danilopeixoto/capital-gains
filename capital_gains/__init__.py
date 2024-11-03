"""
Package main module.

This module serves as the entry point for the package.
It attempts to retrieve the current version of the package using the
package metadata. If the package is not installed, it handles
the exception gracefully, allowing the application to continue without
version information.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("capital-gains")
except PackageNotFoundError:
    pass
