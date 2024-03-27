# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TypeEnum(str, Enum):
    """
    * `db` - Db * `bucket` - Bucket * `db_vector` - Db Vector * `ai` - Ai
    """

    """
    allowed enum values
    """
    DB = "db"
    BUCKET = "bucket"
    DB_VECTOR = "db_vector"
    AI = "ai"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TypeEnum from a JSON string"""
        return cls(json.loads(json_str))
