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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from openapi_client.models.asset_list import AssetList
from openapi_client.models.type_enum import TypeEnum
from typing import Optional, Set
from typing_extensions import Self


class ResourceUpdate(BaseModel):
    """
    ResourceUpdate
    """  # noqa: E501

    resource: Annotated[str, Field(strict=True, max_length=255)]
    data: Dict[str, Any]
    type: TypeEnum
    provider: Annotated[str, Field(strict=True, max_length=100)]
    assets: List[AssetList]
    __properties: ClassVar[List[str]] = [
        "resource",
        "data",
        "type",
        "provider",
        "assets",
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
        """Create an instance of ResourceUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                "assets",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in assets (list)
        _items = []
        if self.assets:
            for _item in self.assets:
                if _item:
                    _items.append(_item.to_dict())
            _dict["assets"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResourceUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "resource": obj.get("resource"),
                "data": obj.get("data"),
                "type": obj.get("type"),
                "provider": obj.get("provider"),
                "assets": [AssetList.from_dict(_item) for _item in obj["assets"]]
                if obj.get("assets") is not None
                else None,
            }
        )
        return _obj
