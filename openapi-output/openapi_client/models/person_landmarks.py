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

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PersonLandmarks(BaseModel):
    """
    PersonLandmarks
    """ # noqa: E501
    eye_left: Optional[List[StrictInt]] = None
    eye_right: Optional[List[StrictInt]] = None
    nose: Optional[List[StrictInt]] = None
    ear_left: Optional[List[StrictInt]] = None
    ear_right: Optional[List[StrictInt]] = None
    shoulder_left: Optional[List[StrictInt]] = None
    shoulder_right: Optional[List[StrictInt]] = None
    elbow_left: Optional[List[StrictInt]] = None
    elbow_right: Optional[List[StrictInt]] = None
    wrist_left: Optional[List[StrictInt]] = None
    wrist_right: Optional[List[StrictInt]] = None
    hip_left: Optional[List[StrictInt]] = None
    hip_right: Optional[List[StrictInt]] = None
    knee_left: Optional[List[StrictInt]] = None
    knee_right: Optional[List[StrictInt]] = None
    ankle_left: Optional[List[StrictInt]] = None
    ankle_right: Optional[List[StrictInt]] = None
    mouth_left: Optional[List[StrictInt]] = None
    mouth_right: Optional[List[StrictInt]] = None
    __properties: ClassVar[List[str]] = ["eye_left", "eye_right", "nose", "ear_left", "ear_right", "shoulder_left", "shoulder_right", "elbow_left", "elbow_right", "wrist_left", "wrist_right", "hip_left", "hip_right", "knee_left", "knee_right", "ankle_left", "ankle_right", "mouth_left", "mouth_right"]

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
        """Create an instance of PersonLandmarks from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PersonLandmarks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eye_left": obj.get("eye_left"),
            "eye_right": obj.get("eye_right"),
            "nose": obj.get("nose"),
            "ear_left": obj.get("ear_left"),
            "ear_right": obj.get("ear_right"),
            "shoulder_left": obj.get("shoulder_left"),
            "shoulder_right": obj.get("shoulder_right"),
            "elbow_left": obj.get("elbow_left"),
            "elbow_right": obj.get("elbow_right"),
            "wrist_left": obj.get("wrist_left"),
            "wrist_right": obj.get("wrist_right"),
            "hip_left": obj.get("hip_left"),
            "hip_right": obj.get("hip_right"),
            "knee_left": obj.get("knee_left"),
            "knee_right": obj.get("knee_right"),
            "ankle_left": obj.get("ankle_left"),
            "ankle_right": obj.get("ankle_right"),
            "mouth_left": obj.get("mouth_left"),
            "mouth_right": obj.get("mouth_right")
        })
        return _obj


