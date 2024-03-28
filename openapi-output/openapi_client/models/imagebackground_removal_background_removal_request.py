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
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ImagebackgroundRemovalBackgroundRemovalRequest(BaseModel):
    """
    ImagebackgroundRemovalBackgroundRemovalRequest
    """ # noqa: E501
    providers: Annotated[str, Field(min_length=1, strict=True)] = Field(description="It can be one (ex: **'amazon'** or **'google'**) or multiple provider(s) (ex: **'amazon,microsoft,google'**)             that the data will be redirected to in order to get the processed results.")
    fallback_providers: Optional[StrictStr] = Field(default=None, description="Providers in this list will be used as fallback if the call to provider in `providers` parameter fails.     To use this feature, you must input **only one** provider in the `providers` parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn't fail.   *Doesn't work with async subfeatures.*     ")
    response_as_dict: Optional[StrictBool] = Field(default=True, description="Optional : When set to **true** (default), the response is an object of responses with providers names as keys : <br>                    ``` {\"google\" : { \"status\": \"success\", ... }, } ``` <br>                 When set to **false** the response structure is a list of response objects : <br>                     ``` [{\"status\": \"success\", \"provider\": \"google\" ... }, ] ```. <br>                   ")
    attributes_as_list: Optional[StrictBool] = Field(default=False, description="Optional : When set to **false** (default) the structure of the extracted items is list of objects having different attributes : <br>      ```{'items': [{\"attribute_1\": \"x1\",\"attribute_2\": \"y2\"}, ... ]}``` <br>      When it is set to **true**, the response contains an object with each attribute as a list : <br>      ```{ \"attribute_1\": [\"x1\",\"x2\", ...], \"attribute_2\": [y1, y2, ...]}``` ")
    show_original_response: Optional[StrictBool] = Field(default=False, description="Optional : Shows the original response of the provider.<br>         When set to **true**, a new attribute *original_response* will appear in the response object.")
    file: Optional[Union[Annotated[bytes, Field(strict=True)], Annotated[str, Field(strict=True)]]] = Field(default=None, description="File to analyse in binary format to be used with *content-type*: **multipart/form-data** <br> **Does not work with application/json !**")
    file_url: Optional[StrictStr] = Field(default=None, description="File **URL** to analyse to be used with with *content-type*: **application/json**.")
    provider_params: Optional[StrictStr] = Field(default=None, description="Provider specific parameters")
    __properties: ClassVar[List[str]] = ["providers", "fallback_providers", "response_as_dict", "attributes_as_list", "show_original_response", "file", "file_url", "provider_params"]

    @field_validator('file')
    def file_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"(?:jpg|jpeg|png|tiff)$", value):
            raise ValueError(r"must validate the regular expression /(?:jpg|jpeg|png|tiff)$/")
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
        """Create an instance of ImagebackgroundRemovalBackgroundRemovalRequest from a JSON string"""
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
        # set to None if fallback_providers (nullable) is None
        # and model_fields_set contains the field
        if self.fallback_providers is None and "fallback_providers" in self.model_fields_set:
            _dict['fallback_providers'] = None

        # set to None if file_url (nullable) is None
        # and model_fields_set contains the field
        if self.file_url is None and "file_url" in self.model_fields_set:
            _dict['file_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ImagebackgroundRemovalBackgroundRemovalRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "providers": obj.get("providers"),
            "fallback_providers": obj.get("fallback_providers"),
            "response_as_dict": obj.get("response_as_dict") if obj.get("response_as_dict") is not None else True,
            "attributes_as_list": obj.get("attributes_as_list") if obj.get("attributes_as_list") is not None else False,
            "show_original_response": obj.get("show_original_response") if obj.get("show_original_response") is not None else False,
            "file": obj.get("file"),
            "file_url": obj.get("file_url"),
            "provider_params": obj.get("provider_params")
        })
        return _obj


