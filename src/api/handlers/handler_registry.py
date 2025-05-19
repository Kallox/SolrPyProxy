"""
Handler Registry
This module serves as a registry for all handlers in the application.
"""

HANDLER_REGISTRY = {}


def register_handler(handler):
    """
    Register a handler in the HANDLER_REGISTRY.
    """

    def decorator(cls):
        print("Registering handler:", handler)
        HANDLER_REGISTRY[handler] = cls
        return cls

    return decorator
