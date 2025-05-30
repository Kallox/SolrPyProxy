"""
Schemas for API requests and responses.
"""

from typing import Any, Dict, Tuple, Type, cast, List

from pydantic import BaseModel, create_model

RESPONSE_MODELS = {}


class SimpleMessage(BaseModel):
    """
    Response model for a simple message.
    """

    message: str


TYPE_MAP = {
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
    "list": list,
    "dict": dict,
}


def generate_response_model(mapping_config: dict):
    """
    Generate a Pydantic model class dynamically using the provided mapping configuration.
    """

    for model_name, field_mapping in mapping_config.items():
        fields: Dict[str, Tuple[Type[Any], Any]] = {}
        for _, field in field_mapping.items():
            name = field.get("name")
            type_ = field.get("type")
            required = field.get("required", False)

            default_value = ... if required else None

            field_type = TYPE_MAP.get(type_, str)

            fields[name] = (field_type, default_value)

        # Create a new Pydantic model class
        model_class = create_model(model_name, **cast(dict, fields))
        RESPONSE_MODELS[model_name] = List[model_class]
