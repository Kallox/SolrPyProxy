"""
This module is responsible for dynamically loading all handler modules
"""

import importlib
import pkgutil

from src.api import handlers


def load_all_handlers():
    """
    Load all handler modules dynamically.
    """
    for _, module_name, _ in pkgutil.iter_modules(handlers.__path__):
        importlib.import_module(f"src.api.handlers.{module_name}")
