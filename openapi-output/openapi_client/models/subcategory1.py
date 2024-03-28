# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from openapi_client.models.content_sub_category_type import ContentSubCategoryType
from openapi_client.models.drug_and_alcohol_sub_category_type import DrugAndAlcoholSubCategoryType
from openapi_client.models.finance_sub_category_type import FinanceSubCategoryType
from openapi_client.models.hate_and_extremism_sub_category_type import HateAndExtremismSubCategoryType
from openapi_client.models.other_sub_category_type import OtherSubCategoryType
from openapi_client.models.safe_sub_category_type import SafeSubCategoryType
from openapi_client.models.sexual_sub_category_type import SexualSubCategoryType
from openapi_client.models.toxic_sub_category_type import ToxicSubCategoryType
from openapi_client.models.violence_sub_category_type import ViolenceSubCategoryType
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

SUBCATEGORY1_ANY_OF_SCHEMAS = ["ContentSubCategoryType", "DrugAndAlcoholSubCategoryType", "FinanceSubCategoryType", "HateAndExtremismSubCategoryType", "OtherSubCategoryType", "SafeSubCategoryType", "SexualSubCategoryType", "ToxicSubCategoryType", "ViolenceSubCategoryType"]

class Subcategory1(BaseModel):
    """
    Subcategory1
    """

    # data type: ToxicSubCategoryType
    anyof_schema_1_validator: Optional[ToxicSubCategoryType] = None
    # data type: ContentSubCategoryType
    anyof_schema_2_validator: Optional[ContentSubCategoryType] = None
    # data type: SexualSubCategoryType
    anyof_schema_3_validator: Optional[SexualSubCategoryType] = None
    # data type: ViolenceSubCategoryType
    anyof_schema_4_validator: Optional[ViolenceSubCategoryType] = None
    # data type: DrugAndAlcoholSubCategoryType
    anyof_schema_5_validator: Optional[DrugAndAlcoholSubCategoryType] = None
    # data type: FinanceSubCategoryType
    anyof_schema_6_validator: Optional[FinanceSubCategoryType] = None
    # data type: HateAndExtremismSubCategoryType
    anyof_schema_7_validator: Optional[HateAndExtremismSubCategoryType] = None
    # data type: SafeSubCategoryType
    anyof_schema_8_validator: Optional[SafeSubCategoryType] = None
    # data type: OtherSubCategoryType
    anyof_schema_9_validator: Optional[OtherSubCategoryType] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[ContentSubCategoryType, DrugAndAlcoholSubCategoryType, FinanceSubCategoryType, HateAndExtremismSubCategoryType, OtherSubCategoryType, SafeSubCategoryType, SexualSubCategoryType, ToxicSubCategoryType, ViolenceSubCategoryType]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: List[str] = Field(default=Literal["ContentSubCategoryType", "DrugAndAlcoholSubCategoryType", "FinanceSubCategoryType", "HateAndExtremismSubCategoryType", "OtherSubCategoryType", "SafeSubCategoryType", "SexualSubCategoryType", "ToxicSubCategoryType", "ViolenceSubCategoryType"])

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = Subcategory1.model_construct()
        error_messages = []
        # validate data type: ToxicSubCategoryType
        if not isinstance(v, ToxicSubCategoryType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ToxicSubCategoryType`")
        else:
            return v

        # validate data type: ContentSubCategoryType
        if not isinstance(v, ContentSubCategoryType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ContentSubCategoryType`")
        else:
            return v

        # validate data type: SexualSubCategoryType
        if not isinstance(v, SexualSubCategoryType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SexualSubCategoryType`")
        else:
            return v

        # validate data type: ViolenceSubCategoryType
        if not isinstance(v, ViolenceSubCategoryType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ViolenceSubCategoryType`")
        else:
            return v

        # validate data type: DrugAndAlcoholSubCategoryType
        if not isinstance(v, DrugAndAlcoholSubCategoryType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DrugAndAlcoholSubCategoryType`")
        else:
            return v

        # validate data type: FinanceSubCategoryType
        if not isinstance(v, FinanceSubCategoryType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FinanceSubCategoryType`")
        else:
            return v

        # validate data type: HateAndExtremismSubCategoryType
        if not isinstance(v, HateAndExtremismSubCategoryType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HateAndExtremismSubCategoryType`")
        else:
            return v

        # validate data type: SafeSubCategoryType
        if not isinstance(v, SafeSubCategoryType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SafeSubCategoryType`")
        else:
            return v

        # validate data type: OtherSubCategoryType
        if not isinstance(v, OtherSubCategoryType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OtherSubCategoryType`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in Subcategory1 with anyOf schemas: ContentSubCategoryType, DrugAndAlcoholSubCategoryType, FinanceSubCategoryType, HateAndExtremismSubCategoryType, OtherSubCategoryType, SafeSubCategoryType, SexualSubCategoryType, ToxicSubCategoryType, ViolenceSubCategoryType. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[ToxicSubCategoryType] = None
        try:
            instance.actual_instance = ToxicSubCategoryType.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[ContentSubCategoryType] = None
        try:
            instance.actual_instance = ContentSubCategoryType.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[SexualSubCategoryType] = None
        try:
            instance.actual_instance = SexualSubCategoryType.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[ViolenceSubCategoryType] = None
        try:
            instance.actual_instance = ViolenceSubCategoryType.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_5_validator: Optional[DrugAndAlcoholSubCategoryType] = None
        try:
            instance.actual_instance = DrugAndAlcoholSubCategoryType.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_6_validator: Optional[FinanceSubCategoryType] = None
        try:
            instance.actual_instance = FinanceSubCategoryType.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_7_validator: Optional[HateAndExtremismSubCategoryType] = None
        try:
            instance.actual_instance = HateAndExtremismSubCategoryType.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_8_validator: Optional[SafeSubCategoryType] = None
        try:
            instance.actual_instance = SafeSubCategoryType.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_9_validator: Optional[OtherSubCategoryType] = None
        try:
            instance.actual_instance = OtherSubCategoryType.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Subcategory1 with anyOf schemas: ContentSubCategoryType, DrugAndAlcoholSubCategoryType, FinanceSubCategoryType, HateAndExtremismSubCategoryType, OtherSubCategoryType, SafeSubCategoryType, SexualSubCategoryType, ToxicSubCategoryType, ViolenceSubCategoryType. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], ContentSubCategoryType, DrugAndAlcoholSubCategoryType, FinanceSubCategoryType, HateAndExtremismSubCategoryType, OtherSubCategoryType, SafeSubCategoryType, SexualSubCategoryType, ToxicSubCategoryType, ViolenceSubCategoryType]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())

