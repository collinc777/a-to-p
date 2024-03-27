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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from openapi_client.models.resume_location import ResumeLocation
from typing import Optional, Set
from typing_extensions import Self


class ResumeWorkExpEntry(BaseModel):
    """
    ResumeWorkExpEntry
    """  # noqa: E501

    title: StrictStr
    start_date: StrictStr
    end_date: StrictStr
    company: StrictStr
    location: ResumeLocation
    description: StrictStr
    industry: StrictStr
    __properties: ClassVar[List[str]] = [
        "title",
        "start_date",
        "end_date",
        "company",
        "location",
        "description",
        "industry",
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
        """Create an instance of ResumeWorkExpEntry from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict["location"] = self.location.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResumeWorkExpEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "title": obj.get("title"),
                "start_date": obj.get("start_date"),
                "end_date": obj.get("end_date"),
                "company": obj.get("company"),
                "location": ResumeLocation.from_dict(obj["location"])
                if obj.get("location") is not None
                else None,
                "description": obj.get("description"),
                "industry": obj.get("industry"),
            }
        )
        return _obj
