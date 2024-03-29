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
from openapi_client.models.final_status_enum import FinalStatusEnum
from openapi_client.models.page import Page
from typing import Optional, Set
from typing_extensions import Self

class PydanticMainOcrocrAsyncOcrAsyncDataClass94559367722320(BaseModel):
    """
    PydanticMainOcrocrAsyncOcrAsyncDataClass94559367722320
    """ # noqa: E501
    raw_text: StrictStr
    pages: Optional[List[Page]] = Field(default=None, description="List of pages")
    number_of_pages: StrictInt = Field(description="Number of pages in the document")
    original_response: Optional[Any] = Field(default=None, description="original response sent by the provider, hidden by default, show it by passing the `show_original_response` field to `true` in your request")
    id: StrictStr
    final_status: FinalStatusEnum
    error: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["raw_text", "pages", "number_of_pages", "original_response", "id", "final_status", "error"]

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
        """Create an instance of PydanticMainOcrocrAsyncOcrAsyncDataClass94559367722320 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in pages (list)
        _items = []
        if self.pages:
            for _item in self.pages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pages'] = _items
        # set to None if original_response (nullable) is None
        # and model_fields_set contains the field
        if self.original_response is None and "original_response" in self.model_fields_set:
            _dict['original_response'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PydanticMainOcrocrAsyncOcrAsyncDataClass94559367722320 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "raw_text": obj.get("raw_text"),
            "pages": [Page.from_dict(_item) for _item in obj["pages"]] if obj.get("pages") is not None else None,
            "number_of_pages": obj.get("number_of_pages"),
            "original_response": obj.get("original_response"),
            "id": obj.get("id"),
            "final_status": obj.get("final_status"),
            "error": obj.get("error")
        })
        return _obj


