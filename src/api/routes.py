"""
Module to load routes from a YAML file and create FastAPI routes dynamically.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse


def create_handler(response_message: str):
    """
    Create a handler function that returns a JSON response with the given message.
    """

    def handler():
        return JSONResponse({"message": response_message})

    return handler


def load_routes(app: FastAPI, routes: list):
    """
    Load routes from a list and create FastAPI routes dynamically.
    """

    for route in routes:
        path = route["path"]
        method = route["method"].lower()
        description = route["description"]
        tags = route.get("tags", [])

        handler = create_handler(description)

        app.add_api_route(
            path=path,
            endpoint=handler,
            methods=[method.upper()],
            summary=description,
            tags=tags,
        )
