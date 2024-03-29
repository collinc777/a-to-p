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
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.resume_location import ResumeLocation
from openapi_client.models.resume_personal_name import ResumePersonalName
from typing import Optional, Set
from typing_extensions import Self

class ResumePersonalInfo(BaseModel):
    """
    ResumePersonalInfo
    """ # noqa: E501
    name: ResumePersonalName
    address: ResumeLocation
    self_summary: StrictStr
    objective: StrictStr
    date_of_birth: StrictStr
    place_of_birth: StrictStr
    phones: Optional[List[StrictStr]] = None
    mails: Optional[List[StrictStr]] = None
    urls: Optional[List[StrictStr]] = None
    fax: Optional[List[StrictStr]] = None
    current_profession: StrictStr
    gender: StrictStr
    nationality: StrictStr
    martial_status: StrictStr
    current_salary: StrictStr
    __properties: ClassVar[List[str]] = ["name", "address", "self_summary", "objective", "date_of_birth", "place_of_birth", "phones", "mails", "urls", "fax", "current_profession", "gender", "nationality", "martial_status", "current_salary"]

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
        """Create an instance of ResumePersonalInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of name
        if self.name:
            _dict['name'] = self.name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResumePersonalInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": ResumePersonalName.from_dict(obj["name"]) if obj.get("name") is not None else None,
            "address": ResumeLocation.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "self_summary": obj.get("self_summary"),
            "objective": obj.get("objective"),
            "date_of_birth": obj.get("date_of_birth"),
            "place_of_birth": obj.get("place_of_birth"),
            "phones": obj.get("phones"),
            "mails": obj.get("mails"),
            "urls": obj.get("urls"),
            "fax": obj.get("fax"),
            "current_profession": obj.get("current_profession"),
            "gender": obj.get("gender"),
            "nationality": obj.get("nationality"),
            "martial_status": obj.get("martial_status"),
            "current_salary": obj.get("current_salary")
        })
        return _obj


