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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.price_unit_type_enum import PriceUnitTypeEnum
from openapi_client.models.pricing_serialzier_detail_type import PricingSerialzierDetailType
from typing import Optional, Set
from typing_extensions import Self

class PricingSerialzier(BaseModel):
    """
    PricingSerialzier
    """ # noqa: E501
    model_name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Model name, default to 'default' if no models to chose from")
    price: Optional[Annotated[str, Field(strict=True)]] = None
    price_unit_quantity: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = None
    min_price_quantity: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = None
    price_unit_type: Optional[PriceUnitTypeEnum] = None
    detail_type: Optional[PricingSerialzierDetailType] = None
    detail_value: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="(Optional) extra value for detailed pricing, eg: 250x250 for resolution")
    get_detail_type_display: StrictStr
    is_post_call: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["model_name", "price", "price_unit_quantity", "min_price_quantity", "price_unit_type", "detail_type", "detail_value", "get_detail_type_display", "is_post_call"]

    @field_validator('price')
    def price_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^-?\d{0,6}(?:\.\d{0,9})?$", value):
            raise ValueError(r"must validate the regular expression /^-?\d{0,6}(?:\.\d{0,9})?$/")
        return value

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
        """Create an instance of PricingSerialzier from a JSON string"""
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
        excluded_fields: Set[str] = set([
            "get_detail_type_display",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of detail_type
        if self.detail_type:
            _dict['detail_type'] = self.detail_type.to_dict()
        # set to None if min_price_quantity (nullable) is None
        # and model_fields_set contains the field
        if self.min_price_quantity is None and "min_price_quantity" in self.model_fields_set:
            _dict['min_price_quantity'] = None

        # set to None if detail_type (nullable) is None
        # and model_fields_set contains the field
        if self.detail_type is None and "detail_type" in self.model_fields_set:
            _dict['detail_type'] = None

        # set to None if detail_value (nullable) is None
        # and model_fields_set contains the field
        if self.detail_value is None and "detail_value" in self.model_fields_set:
            _dict['detail_value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PricingSerialzier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "model_name": obj.get("model_name"),
            "price": obj.get("price"),
            "price_unit_quantity": obj.get("price_unit_quantity"),
            "min_price_quantity": obj.get("min_price_quantity"),
            "price_unit_type": obj.get("price_unit_type"),
            "detail_type": PricingSerialzierDetailType.from_dict(obj["detail_type"]) if obj.get("detail_type") is not None else None,
            "detail_value": obj.get("detail_value"),
            "get_detail_type_display": obj.get("get_detail_type_display"),
            "is_post_call": obj.get("is_post_call")
        })
        return _obj


