"""
Base handler class for all handlers.
This module defines the BaseHandler class, which serves as an abstract base class for
all handlers in the application.
It provides a common interface for handling, validating, and processing requests.
"""

from abc import ABC, abstractmethod


class BaseHandler(ABC):
    """
    Abstract base class for all handlers.
    """

    @abstractmethod
    async def handle(self, request):
        """
        Handle the incoming request.
        """

    @abstractmethod
    def validate(self, request):
        """
        Validate the incoming request.
        """

    @abstractmethod
    def process(self, request):
        """
        Process the incoming request.
        """
