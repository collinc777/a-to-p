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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.pydantic_main_ocrocr_tables_async_ocr_tables_async_data_class94559364101216 import (
    PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559364101216,
)
from openapi_client.models.pydantic_main_ocrocr_tables_async_ocr_tables_async_data_class94559364529376 import (
    PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559364529376,
)
from openapi_client.models.pydantic_main_ocrocr_tables_async_ocr_tables_async_data_class94559372486640 import (
    PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559372486640,
)
from typing import Set
from typing_extensions import Self


class OcrocrTablesAsyncModel(BaseModel):
    """
    OcrocrTablesAsyncModel
    """  # noqa: E501

    amazon: Optional[
        PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559364529376
    ] = None
    microsoft: Optional[
        PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559372486640
    ] = None
    google: Optional[
        PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559364101216
    ] = None
    __properties: ClassVar[List[str]] = ["amazon", "microsoft", "google"]

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
        """Create an instance of OcrocrTablesAsyncModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of amazon
        if self.amazon:
            _dict["amazon"] = self.amazon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of microsoft
        if self.microsoft:
            _dict["microsoft"] = self.microsoft.to_dict()
        # override the default output from pydantic by calling `to_dict()` of google
        if self.google:
            _dict["google"] = self.google.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OcrocrTablesAsyncModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "amazon": PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559364529376.from_dict(
                    obj["amazon"]
                )
                if obj.get("amazon") is not None
                else None,
                "microsoft": PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559372486640.from_dict(
                    obj["microsoft"]
                )
                if obj.get("microsoft") is not None
                else None,
                "google": PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559364101216.from_dict(
                    obj["google"]
                )
                if obj.get("google") is not None
                else None,
            }
        )
        return _obj
