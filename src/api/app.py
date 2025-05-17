"""
Module to create a FastAPI application instance with custom configuration.
"""

from fastapi import FastAPI


def create_app(config) -> FastAPI:
    """
    Create a FastAPI application instance with custom configuration.
    """
    app = FastAPI(
        title=config.get("title", "Default Title"),
        description=config.get("description", "Default Description"),
        version=config.get("version", "0.1.0"),
        contact=config.get("contact", {}),
    )
    return app
