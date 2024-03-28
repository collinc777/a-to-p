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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.batch_response_request import BatchResponseRequest
from openapi_client.models.status_e80_enum import StatusE80Enum
from typing import Optional, Set
from typing_extensions import Self

class PaginatedBatchResponse(BaseModel):
    """
    PaginatedBatchResponse
    """ # noqa: E501
    total: StrictInt = Field(description="Total requests made")
    current_page: StrictInt = Field(description="Current page number")
    last_page: StrictInt
    per_page: StrictInt = Field(description="Number of requests per page")
    var_from: StrictInt = Field(alias="From")
    to: StrictInt
    prev_page_url: Optional[StrictStr] = None
    next_page_url: Optional[StrictStr] = None
    requests: List[BatchResponseRequest]
    status: Optional[StatusE80Enum] = None
    created: datetime
    updated: datetime
    __properties: ClassVar[List[str]] = ["total", "current_page", "last_page", "per_page", "From", "to", "prev_page_url", "next_page_url", "requests", "status", "created", "updated"]

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
        """Create an instance of PaginatedBatchResponse from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created",
            "updated",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in requests (list)
        _items = []
        if self.requests:
            for _item in self.requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['requests'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaginatedBatchResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "total": obj.get("total"),
            "current_page": obj.get("current_page"),
            "last_page": obj.get("last_page"),
            "per_page": obj.get("per_page"),
            "From": obj.get("From"),
            "to": obj.get("to"),
            "prev_page_url": obj.get("prev_page_url"),
            "next_page_url": obj.get("next_page_url"),
            "requests": [BatchResponseRequest.from_dict(_item) for _item in obj["requests"]] if obj.get("requests") is not None else None,
            "status": obj.get("status"),
            "created": obj.get("created"),
            "updated": obj.get("updated")
        })
        return _obj

