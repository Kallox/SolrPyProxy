"""
Module to load routes from a YAML file and create FastAPI routes dynamically.
"""

from fastapi import FastAPI

from src.api.handlers.handler_registry import HANDLER_REGISTRY
from src.api.handlers.load_handlers import load_all_handlers
from src.api.schemas import RESPONSE_MODELS, SimpleMessage, generate_response_model


def create_endpoint(handler_instance, config_request_dict):
    """
    Create an endpoint function that will handle the request using the provided handler instance.
    """

    async def endpoint():
        return await handler_instance.handle(config_request_dict)

    return endpoint


def load_routes(app: FastAPI, routes: list, metadata_mapping: dict):
    """
    Load routes from a list and create FastAPI routes dynamically.
    """

    load_all_handlers()

    # Generate response models based on metadata mapping
    generate_response_model(metadata_mapping)

    for route in routes:
        path = route["path"]
        method = route["method"].lower()
        description = route["description"]
        tags = route.get("tags", [])
        response_model = route.get("response_model", SimpleMessage)
        request = route.get("request", {})
        handler_type = route.get("handler", "PlainText")

        handler = HANDLER_REGISTRY.get(handler_type, None)

        if handler is None:
            print(f"Handler not found for type: {handler_type}")
            continue

        app.add_api_route(
            path=path,
            endpoint=create_endpoint(handler(), request),
            methods=[method.upper()],
            summary=description,
            tags=tags,
            response_model=RESPONSE_MODELS.get(response_model, SimpleMessage),
        )
