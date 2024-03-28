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


class StateEnum(str, Enum):
    """
    * `finished` - finished * `failed` - failed * `Timeout error` - Timeout error * `processing` - processing
    """

    """
    allowed enum values
    """
    FINISHED = 'finished'
    FAILED = 'failed'
    TIMEOUT_ERROR = 'Timeout error'
    PROCESSING = 'processing'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StateEnum from a JSON string"""
        return cls(json.loads(json_str))


