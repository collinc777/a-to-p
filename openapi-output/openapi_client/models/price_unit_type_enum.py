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


class PriceUnitTypeEnum(str, Enum):
    """
    * `file` - File * `image` - Image * `page` - Page * `size` - Size * `request` - Request * `seconde` - Second * `minute` - Minute * `free` - Free * `hour` - Hour * `char` - Characters * `token` - Token * `exec_time` - Execution Time * `unknown` - Unknown
    """

    """
    allowed enum values
    """
    FILE = 'file'
    IMAGE = 'image'
    PAGE = 'page'
    SIZE = 'size'
    REQUEST = 'request'
    SECONDE = 'seconde'
    MINUTE = 'minute'
    FREE = 'free'
    HOUR = 'hour'
    CHAR = 'char'
    TOKEN = 'token'
    EXEC_TIME = 'exec_time'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PriceUnitTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


