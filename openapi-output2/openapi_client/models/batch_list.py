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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.status_e80_enum import StatusE80Enum
from typing import Set
from typing_extensions import Self


class BatchList(BaseModel):
    """
    BatchList
    """  # noqa: E501

    name: Optional[Annotated[str, Field(strict=True, max_length=1023)]] = None
    status: Optional[StatusE80Enum] = None
    feature: StrictStr
    subfeature: StrictStr
    total_requests: StrictInt
    nb_processing: StrictInt
    nb_succeeded: StrictInt
    nb_failed: StrictInt
    get_response_url: StrictStr
    __properties: ClassVar[List[str]] = [
        "name",
        "status",
        "feature",
        "subfeature",
        "total_requests",
        "nb_processing",
        "nb_succeeded",
        "nb_failed",
        "get_response_url",
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
        """Create an instance of BatchList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                "feature",
                "subfeature",
                "total_requests",
                "nb_processing",
                "nb_succeeded",
                "nb_failed",
                "get_response_url",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BatchList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "status": obj.get("status"),
                "feature": obj.get("feature"),
                "subfeature": obj.get("subfeature"),
                "total_requests": obj.get("total_requests"),
                "nb_processing": obj.get("nb_processing"),
                "nb_succeeded": obj.get("nb_succeeded"),
                "nb_failed": obj.get("nb_failed"),
                "get_response_url": obj.get("get_response_url"),
            }
        )
        return _obj
