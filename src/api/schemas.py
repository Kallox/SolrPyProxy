"""
Schemas for API requests and responses.
"""

from pydantic import BaseModel


class SimpleMessage(BaseModel):
    """
    Response model for a simple message.
    """

    message: str
