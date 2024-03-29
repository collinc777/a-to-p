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
from openapi_client.models.financial_parser_object_data_class import FinancialParserObjectDataClass
from openapi_client.models.status_f43_enum import StatusF43Enum
from typing import Optional, Set
from typing_extensions import Self

class PydanticMainOcrfinancialParserFinancialParserDataClass94559368405584(BaseModel):
    """
    PydanticMainOcrfinancialParserFinancialParserDataClass94559368405584
    """ # noqa: E501
    extracted_data: Optional[List[FinancialParserObjectDataClass]] = Field(default=None, description="List of parsed financial data objects (per page).")
    original_response: Optional[Any] = Field(default=None, description="original response sent by the provider, hidden by default, show it by passing the `show_original_response` field to `true` in your request")
    status: StatusF43Enum
    __properties: ClassVar[List[str]] = ["extracted_data", "original_response", "status"]

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
        """Create an instance of PydanticMainOcrfinancialParserFinancialParserDataClass94559368405584 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in extracted_data (list)
        _items = []
        if self.extracted_data:
            for _item in self.extracted_data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['extracted_data'] = _items
        # set to None if original_response (nullable) is None
        # and model_fields_set contains the field
        if self.original_response is None and "original_response" in self.model_fields_set:
            _dict['original_response'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PydanticMainOcrfinancialParserFinancialParserDataClass94559368405584 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "extracted_data": [FinancialParserObjectDataClass.from_dict(_item) for _item in obj["extracted_data"]] if obj.get("extracted_data") is not None else None,
            "original_response": obj.get("original_response"),
            "status": obj.get("status")
        })
        return _obj


