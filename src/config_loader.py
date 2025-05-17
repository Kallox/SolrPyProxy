"""
Module to load configuration files for the application.
"""

import yaml


def load_config(path: str) -> dict:
    """
    Load configuration from a YAML file.

    :param path: File path to the YAML configuration file.
    :type path: str
    :return: Dictionary containing the configuration settings.
    :rtype: dict
    """
    with open(path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    return config
