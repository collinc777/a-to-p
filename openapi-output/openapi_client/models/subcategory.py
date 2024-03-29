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
from openapi_client.models.date_and_time_sub_category_type import DateAndTimeSubCategoryType
from openapi_client.models.financial_information_sub_category_type import FinancialInformationSubCategoryType
from openapi_client.models.identification_numbers_sub_category_type import IdentificationNumbersSubCategoryType
from openapi_client.models.location_information_sub_category_type import LocationInformationSubCategoryType
from openapi_client.models.miscellaneous_sub_category_type import MiscellaneousSubCategoryType
from openapi_client.models.organization_sub_category_type import OrganizationSubCategoryType
from openapi_client.models.other_sub_category_type import OtherSubCategoryType
from openapi_client.models.personal_information_sub_category_type import PersonalInformationSubCategoryType
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

SUBCATEGORY_ANY_OF_SCHEMAS = ["DateAndTimeSubCategoryType", "FinancialInformationSubCategoryType", "IdentificationNumbersSubCategoryType", "LocationInformationSubCategoryType", "MiscellaneousSubCategoryType", "OrganizationSubCategoryType", "OtherSubCategoryType", "PersonalInformationSubCategoryType"]

class Subcategory(BaseModel):
    """
    Subcategory
    """

    # data type: FinancialInformationSubCategoryType
    anyof_schema_1_validator: Optional[FinancialInformationSubCategoryType] = None
    # data type: PersonalInformationSubCategoryType
    anyof_schema_2_validator: Optional[PersonalInformationSubCategoryType] = None
    # data type: IdentificationNumbersSubCategoryType
    anyof_schema_3_validator: Optional[IdentificationNumbersSubCategoryType] = None
    # data type: MiscellaneousSubCategoryType
    anyof_schema_4_validator: Optional[MiscellaneousSubCategoryType] = None
    # data type: OrganizationSubCategoryType
    anyof_schema_5_validator: Optional[OrganizationSubCategoryType] = None
    # data type: DateAndTimeSubCategoryType
    anyof_schema_6_validator: Optional[DateAndTimeSubCategoryType] = None
    # data type: LocationInformationSubCategoryType
    anyof_schema_7_validator: Optional[LocationInformationSubCategoryType] = None
    # data type: OtherSubCategoryType
    anyof_schema_8_validator: Optional[OtherSubCategoryType] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[DateAndTimeSubCategoryType, FinancialInformationSubCategoryType, IdentificationNumbersSubCategoryType, LocationInformationSubCategoryType, MiscellaneousSubCategoryType, OrganizationSubCategoryType, OtherSubCategoryType, PersonalInformationSubCategoryType]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: List[str] = Field(default=Literal["DateAndTimeSubCategoryType", "FinancialInformationSubCategoryType", "IdentificationNumbersSubCategoryType", "LocationInformationSubCategoryType", "MiscellaneousSubCategoryType", "OrganizationSubCategoryType", "OtherSubCategoryType", "PersonalInformationSubCategoryType"])

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
        instance = Subcategory.model_construct()
        error_messages = []
        # validate data type: FinancialInformationSubCategoryType
        if not isinstance(v, FinancialInformationSubCategoryType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FinancialInformationSubCategoryType`")
        else:
            return v

        # validate data type: PersonalInformationSubCategoryType
        if not isinstance(v, PersonalInformationSubCategoryType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PersonalInformationSubCategoryType`")
        else:
            return v

        # validate data type: IdentificationNumbersSubCategoryType
        if not isinstance(v, IdentificationNumbersSubCategoryType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationNumbersSubCategoryType`")
        else:
            return v

        # validate data type: MiscellaneousSubCategoryType
        if not isinstance(v, MiscellaneousSubCategoryType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MiscellaneousSubCategoryType`")
        else:
            return v

        # validate data type: OrganizationSubCategoryType
        if not isinstance(v, OrganizationSubCategoryType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OrganizationSubCategoryType`")
        else:
            return v

        # validate data type: DateAndTimeSubCategoryType
        if not isinstance(v, DateAndTimeSubCategoryType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DateAndTimeSubCategoryType`")
        else:
            return v

        # validate data type: LocationInformationSubCategoryType
        if not isinstance(v, LocationInformationSubCategoryType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LocationInformationSubCategoryType`")
        else:
            return v

        # validate data type: OtherSubCategoryType
        if not isinstance(v, OtherSubCategoryType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OtherSubCategoryType`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in Subcategory with anyOf schemas: DateAndTimeSubCategoryType, FinancialInformationSubCategoryType, IdentificationNumbersSubCategoryType, LocationInformationSubCategoryType, MiscellaneousSubCategoryType, OrganizationSubCategoryType, OtherSubCategoryType, PersonalInformationSubCategoryType. Details: " + ", ".join(error_messages))
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
        # anyof_schema_1_validator: Optional[FinancialInformationSubCategoryType] = None
        try:
            instance.actual_instance = FinancialInformationSubCategoryType.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[PersonalInformationSubCategoryType] = None
        try:
            instance.actual_instance = PersonalInformationSubCategoryType.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[IdentificationNumbersSubCategoryType] = None
        try:
            instance.actual_instance = IdentificationNumbersSubCategoryType.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[MiscellaneousSubCategoryType] = None
        try:
            instance.actual_instance = MiscellaneousSubCategoryType.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_5_validator: Optional[OrganizationSubCategoryType] = None
        try:
            instance.actual_instance = OrganizationSubCategoryType.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_6_validator: Optional[DateAndTimeSubCategoryType] = None
        try:
            instance.actual_instance = DateAndTimeSubCategoryType.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_7_validator: Optional[LocationInformationSubCategoryType] = None
        try:
            instance.actual_instance = LocationInformationSubCategoryType.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_8_validator: Optional[OtherSubCategoryType] = None
        try:
            instance.actual_instance = OtherSubCategoryType.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Subcategory with anyOf schemas: DateAndTimeSubCategoryType, FinancialInformationSubCategoryType, IdentificationNumbersSubCategoryType, LocationInformationSubCategoryType, MiscellaneousSubCategoryType, OrganizationSubCategoryType, OtherSubCategoryType, PersonalInformationSubCategoryType. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], DateAndTimeSubCategoryType, FinancialInformationSubCategoryType, IdentificationNumbersSubCategoryType, LocationInformationSubCategoryType, MiscellaneousSubCategoryType, OrganizationSubCategoryType, OtherSubCategoryType, PersonalInformationSubCategoryType]]:
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


