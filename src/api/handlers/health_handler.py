"""
HealthHandler
This module contains the HealthHandler class, which is responsible for handling health check requests.
"""

from src.api.handlers.base_handler import BaseHandler
from src.api.handlers.handler_registry import register_handler


@register_handler("health")
class HealthHandler(BaseHandler):
    """
    Handler for health check requests.
    This handler is responsible for checking the health of the application and returning a response.
    """

    async def handle(self, request):
        """
        Handle the incoming health check request.
        """

        if not self.validate(request):
            return {"message": "Invalid request"}

        response = self.process(request)

        return response

    def validate(self, request):
        """
        Validate the incoming health check request.
        """

        # Check if the requests contains the required fields
        if "message" in request:
            # Check if the message is a string
            if not isinstance(request["message"], str):
                return False
            # Check if the message is not empty
            if not request["message"]:
                return False
            return True

        return False

    def process(self, request):
        """
        Process the incoming health check request.
        """
        # Get the message from the request
        message = request.get("message")

        return {"message": message}
