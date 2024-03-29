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
from typing import Any, ClassVar, Dict, List
from openapi_client.models.batch_launch_failed_request import BatchLaunchFailedRequest
from typing import Optional, Set
from typing_extensions import Self

class BatchLaunchResponse(BaseModel):
    """
    BatchLaunchResponse
    """ # noqa: E501
    job_id: StrictStr = Field(description="Job ID/name")
    nb_launched: StrictInt = Field(description="Number of successfully launched requests")
    nb_failed: StrictInt = Field(description="Number of failed_requests")
    total: StrictInt = Field(description="Total number of requests sent")
    failed_requests: List[BatchLaunchFailedRequest] = Field(description="if any requests failed, they will be shown in this list")
    __properties: ClassVar[List[str]] = ["job_id", "nb_launched", "nb_failed", "total", "failed_requests"]

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
        """Create an instance of BatchLaunchResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in failed_requests (list)
        _items = []
        if self.failed_requests:
            for _item in self.failed_requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['failed_requests'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BatchLaunchResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "job_id": obj.get("job_id"),
            "nb_launched": obj.get("nb_launched"),
            "nb_failed": obj.get("nb_failed"),
            "total": obj.get("total"),
            "failed_requests": [BatchLaunchFailedRequest.from_dict(_item) for _item in obj["failed_requests"]] if obj.get("failed_requests") is not None else None
        })
        return _obj


