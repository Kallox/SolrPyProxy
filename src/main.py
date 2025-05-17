"""
Entry point for the application.
"""

import uvicorn

from src.api.app import create_app
from src.config_loader import load_config


def main():
    """
    Main function to run the application.
    """
    config = load_config("./config/config.yaml")
    api = create_app(config)
    uvicorn.run(api, host="127.0.0.1", port=8000)
