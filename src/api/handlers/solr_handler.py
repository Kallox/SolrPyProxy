"""
SolrHandler
SolrHandler is a class that handles Solr queries.
"""

from fastapi import HTTPException

from src.api.handlers.base_handler import BaseHandler
from src.api.handlers.handler_registry import register_handler


@register_handler("solr")
class SolrHandler(BaseHandler):
    """
    Handler for Solr queries.
    """

    metadata_mapping: dict = {}

    async def handle(self, request):
        """
        Handle the incoming Solr query request.
        """
        # Implement the logic to handle the Solr query

        is_valid, error_message = self.validate(request)
        if not is_valid:
            raise HTTPException(status_code=400, detail=error_message)

        raise HTTPException(
            status_code=500, detail="Solr query handling not implemented"
        )

    def validate(self, request):
        """
        Validate the incoming Solr query request.
        """
        # Implement the logic to validate the Solr query
        query = request.get("query", None)
        if not query:
            raise HTTPException(status_code=400, detail="Query parameter is required")

        required_fields = ["q", "qt", "rows", "start", "fl", "sort"]

        missing_fields = []

        for field in required_fields:
            if field not in query:
                missing_fields.append(field)

        if missing_fields:
            return False, f"Missing required fields: {', '.join(missing_fields)}"

        return True, None

    def process(self, request):
        """
        Process the incoming Solr query request.
        """
        # Implement the logic to process the Solr query

    def set_metadata_mapping(self, metadata_mapping):
        """
        Set the metadata mapping for the Solr query.
        """
        self.metadata_mapping = metadata_mapping
