# handler_loader.py
import importlib
import pkgutil

import src.api.handlers as handlers


def load_all_handlers():
    for _, module_name, _ in pkgutil.iter_modules(handlers.__path__):
        importlib.import_module(f"src.api.handlers.{module_name}")
