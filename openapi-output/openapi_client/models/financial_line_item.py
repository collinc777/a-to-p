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
from typing import Optional, Set
from typing_extensions import Self

class FinancialLineItem(BaseModel):
    """
    FinancialLineItem
    """ # noqa: E501
    tax: Optional[StrictInt] = Field(default=None, description="Tax amount for the line item.")
    amount_line: Optional[StrictInt] = Field(default=None, description="Total amount for the line item.")
    description: Optional[StrictStr] = Field(default=None, description="Description of the line item.")
    quantity: Optional[StrictInt] = Field(default=None, description="Quantity of units for the line item.")
    unit_price: Optional[StrictInt] = Field(default=None, description="Unit price for each unit in the line item.")
    unit_type: Optional[StrictStr] = Field(default=None, description="Type of unit (e.g., hours, items).")
    var_date: Optional[StrictStr] = Field(default=None, description="Date associated with the line item.", alias="date")
    product_code: Optional[StrictStr] = Field(default=None, description="Product code or identifier for the line item.")
    purchase_order: Optional[StrictStr] = Field(default=None, description="Purchase order related to the line item.")
    tax_rate: Optional[StrictInt] = Field(default=None, description="Tax rate applied to the line item.")
    base_total: Optional[StrictInt] = Field(default=None, description="Base total amount before any discounts or taxes.")
    sub_total: Optional[StrictInt] = Field(default=None, description="Subtotal amount for the line item.")
    discount_amount: Optional[StrictInt] = Field(default=None, description="Amount of discount applied to the line item.")
    discount_rate: Optional[StrictInt] = Field(default=None, description="Rate of discount applied to the line item.")
    discount_code: Optional[StrictStr] = Field(default=None, description="Code associated with any discount applied to the line item.")
    order_number: Optional[StrictStr] = Field(default=None, description="Order number associated with the line item.")
    title: Optional[StrictStr] = Field(default=None, description="Title or name of the line item.")
    __properties: ClassVar[List[str]] = ["tax", "amount_line", "description", "quantity", "unit_price", "unit_type", "date", "product_code", "purchase_order", "tax_rate", "base_total", "sub_total", "discount_amount", "discount_rate", "discount_code", "order_number", "title"]

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
        """Create an instance of FinancialLineItem from a JSON string"""
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
        """Create an instance of FinancialLineItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tax": obj.get("tax"),
            "amount_line": obj.get("amount_line"),
            "description": obj.get("description"),
            "quantity": obj.get("quantity"),
            "unit_price": obj.get("unit_price"),
            "unit_type": obj.get("unit_type"),
            "date": obj.get("date"),
            "product_code": obj.get("product_code"),
            "purchase_order": obj.get("purchase_order"),
            "tax_rate": obj.get("tax_rate"),
            "base_total": obj.get("base_total"),
            "sub_total": obj.get("sub_total"),
            "discount_amount": obj.get("discount_amount"),
            "discount_rate": obj.get("discount_rate"),
            "discount_code": obj.get("discount_code"),
            "order_number": obj.get("order_number"),
            "title": obj.get("title")
        })
        return _obj


