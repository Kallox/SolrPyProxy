"""
SolrHandler
SolrHandler is a class that handles Solr queries.
"""

import aiohttp
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

        await self.process(request)

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

        required_fields = ["q", "rows", "start", "fl"]

        missing_fields = []

        for field in required_fields:
            if field not in query:
                missing_fields.append(field)

        if missing_fields:
            return False, f"Missing required fields: {', '.join(missing_fields)}"

        return True, None

    async def process(self, request):
        """
        Process the incoming Solr query request.
        """
        # Implement the logic to process the Solr query

        url = self.generate_url(request)
        response = await self.execute_query(request, url)

        print(response)

    def generate_url(self, request):
        """
        Generate the Solr query URL.
        """
        base_url = request.get("base_url", "http://localhost:8983/solr")
        core = request.get("core", "search")
        qt = request.get("qt", "select")
        return f"{base_url}/{core}/{qt}"

    async def execute_query(self, request, url):
        """
        Execute the Solr query.
        """
        # Implement the logic to execute the Solr query

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=request["query"]) as response:
                if response.status != 200:
                    raise HTTPException(
                        status_code=response.status,
                        detail=f"Error executing Solr query: {response}",
                    )
                return await response.json()

    def set_metadata_mapping(self, metadata_mapping):
        """
        Set the metadata mapping for the Solr query.
        """
        self.metadata_mapping = metadata_mapping
