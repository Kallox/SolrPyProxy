"""
Module to load routes from a YAML file and create FastAPI routes dynamically.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.api.schemas import SimpleMessage

RESPONSE_MODELS = {
    "SimpleMessage": SimpleMessage,
}


def create_handler(response_message: str, handler_type: str = "PlainText"):
    """
    Create a handler function that returns a JSON response with the given message.
    """

    def plain_text_handler():
        """
        Handler for plain text responses.
        """
        return JSONResponse({"message": response_message + " (PlainText)"})

    def solr_query_handler():
        """
        Handler for SolrQuery responses.
        """
        return JSONResponse({"message": response_message + " (solrQuery)"})

    if handler_type == "SolrQuery":
        return solr_query_handler

    return plain_text_handler


def load_routes(app: FastAPI, routes: list):
    """
    Load routes from a list and create FastAPI routes dynamically.
    """

    for route in routes:
        path = route["path"]
        method = route["method"].lower()
        description = route["description"]
        tags = route.get("tags", [])
        response = route.get("response", None)
        response_model = route.get("response_model", SimpleMessage)
        handler_type = route.get("type", "PlainText")

        handler = create_handler(response, handler_type)

        app.add_api_route(
            path=path,
            endpoint=handler,
            methods=[method.upper()],
            summary=description,
            tags=tags,
            response_model=RESPONSE_MODELS.get(response_model, SimpleMessage),
        )
