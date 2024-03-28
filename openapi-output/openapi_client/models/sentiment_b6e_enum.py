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


class SentimentB6eEnum(str, Enum):
    """
    SentimentB6eEnum
    """

    """
    allowed enum values
    """
    POSITIVE = 'Positive'
    NEGATIVE = 'Negative'
    NEUTRAL = 'Neutral'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SentimentB6eEnum from a JSON string"""
        return cls(json.loads(json_str))


