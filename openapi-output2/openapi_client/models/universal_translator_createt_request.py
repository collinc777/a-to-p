# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Set
from typing_extensions import Self


class UniversalTranslatorCreatetRequest(BaseModel):
    """
    UniversalTranslatorCreatetRequest
    """  # noqa: E501

    source_language: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=10)]
    ] = Field(
        default=None,
        description="The language code from which the text will be translated",
    )
    target_language: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=10)]
    ] = Field(
        default=None,
        description="The language code in which the text will be translated",
    )
    project_name: Annotated[str, Field(min_length=1, strict=True, max_length=200)] = (
        Field(description="The project name")
    )
    fall_back_providers: Optional[
        List[Annotated[str, Field(min_length=1, strict=True, max_length=30)]]
    ] = None
    provider: Annotated[str, Field(min_length=1, strict=True, max_length=50)]
    __properties: ClassVar[List[str]] = [
        "source_language",
        "target_language",
        "project_name",
        "fall_back_providers",
        "provider",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UniversalTranslatorCreatetRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if source_language (nullable) is None
        # and model_fields_set contains the field
        if self.source_language is None and "source_language" in self.model_fields_set:
            _dict["source_language"] = None

        # set to None if target_language (nullable) is None
        # and model_fields_set contains the field
        if self.target_language is None and "target_language" in self.model_fields_set:
            _dict["target_language"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UniversalTranslatorCreatetRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "source_language": obj.get("source_language"),
                "target_language": obj.get("target_language"),
                "project_name": obj.get("project_name"),
                "fall_back_providers": obj.get("fall_back_providers"),
                "provider": obj.get("provider"),
            }
        )
        return _obj
