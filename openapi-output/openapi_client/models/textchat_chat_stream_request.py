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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from openapi_client.models.fallback_type_enum import FallbackTypeEnum
from typing import Optional, Set
from typing_extensions import Self

class TextchatChatStreamRequest(BaseModel):
    """
    TextchatChatStreamRequest
    """ # noqa: E501
    providers: Annotated[str, Field(min_length=1, strict=True)] = Field(description="It can be one (ex: **'amazon'** or **'google'**) or multiple provider(s) (ex: **'amazon,microsoft,google'**)             that the data will be redirected to in order to get the processed results.")
    fallback_providers: Optional[StrictStr] = Field(default=None, description="Providers in this list will be used as fallback if the call to provider in `providers` parameter fails.     To use this feature, you must input **only one** provider in the `providers` parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn't fail.   *Doesn't work with async subfeatures.*     ")
    response_as_dict: Optional[StrictBool] = Field(default=True, description="Optional : When set to **true** (default), the response is an object of responses with providers names as keys : <br>                    ``` {\"google\" : { \"status\": \"success\", ... }, } ``` <br>                 When set to **false** the response structure is a list of response objects : <br>                     ``` [{\"status\": \"success\", \"provider\": \"google\" ... }, ] ```. <br>                   ")
    attributes_as_list: Optional[StrictBool] = Field(default=False, description="Optional : When set to **false** (default) the structure of the extracted items is list of objects having different attributes : <br>      ```{'items': [{\"attribute_1\": \"x1\",\"attribute_2\": \"y2\"}, ... ]}``` <br>      When it is set to **true**, the response contains an object with each attribute as a list : <br>      ```{ \"attribute_1\": [\"x1\",\"x2\", ...], \"attribute_2\": [y1, y2, ...]}``` ")
    show_original_response: Optional[StrictBool] = Field(default=False, description="Optional : Shows the original response of the provider.<br>         When set to **true**, a new attribute *original_response* will appear in the response object.")
    settings: Optional[StrictStr] = Field(default=None, description="A dictionnary or a json object to specify specific models to use for some providers. <br>                     It can be in the following format: {\"google\" : \"google_model\", \"ibm\": \"ibm_model\"...}.                      **Caution**: setting models can be done only with `Content-Type` : `application/json`.                      ")
    text: Optional[StrictStr] = Field(default='', description="Start your conversation here...")
    chatbot_global_action: Optional[StrictStr] = Field(default='', description="A system message that helps set the behavior of the assistant. For example, 'You are a helpful assistant'.")
    previous_history: Optional[List[Dict[str, Any]]] = Field(default=None, description="A list containing all the previous conversations between the user and the chatbot AI. Each item in the list should be a dictionary with two keys: 'role' and 'message'. The 'role' key specifies the role of the speaker and can have the values 'user' or 'assistant'. The 'message' key contains the text of the conversation from the respective role. For example: [{'role': 'user', 'message': 'Hello'}, {'role': 'assistant', 'message': 'Hi, how can I help you?'}, ...]. This format allows easy identification of the speaker's role and their corresponding message.")
    temperature: Optional[Union[Annotated[float, Field(le=2, strict=True, ge=0)], Annotated[int, Field(le=2, strict=True, ge=0)]]] = Field(default=0.0, description="Higher values mean the model will take more risks and value 0 (argmax sampling) works better for scenarios with a well-defined answer.")
    max_tokens: Optional[Annotated[int, Field(le=16385, strict=True, ge=1)]] = Field(default=1000, description="The maximum number of tokens to generate in the completion. The token count of your prompt plus max_tokens cannot exceed the model's context length.")
    fallback_type: Optional[FallbackTypeEnum] = None
    __properties: ClassVar[List[str]] = ["providers", "fallback_providers", "response_as_dict", "attributes_as_list", "show_original_response", "settings", "text", "chatbot_global_action", "previous_history", "temperature", "max_tokens", "fallback_type"]

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
        """Create an instance of TextchatChatStreamRequest from a JSON string"""
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

        # set to None if text (nullable) is None
        # and model_fields_set contains the field
        if self.text is None and "text" in self.model_fields_set:
            _dict['text'] = None

        # set to None if chatbot_global_action (nullable) is None
        # and model_fields_set contains the field
        if self.chatbot_global_action is None and "chatbot_global_action" in self.model_fields_set:
            _dict['chatbot_global_action'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TextchatChatStreamRequest from a dict"""
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
            "settings": obj.get("settings"),
            "text": obj.get("text") if obj.get("text") is not None else '',
            "chatbot_global_action": obj.get("chatbot_global_action") if obj.get("chatbot_global_action") is not None else '',
            "previous_history": obj.get("previous_history"),
            "temperature": obj.get("temperature") if obj.get("temperature") is not None else 0.0,
            "max_tokens": obj.get("max_tokens") if obj.get("max_tokens") is not None else 1000,
            "fallback_type": obj.get("fallback_type")
        })
        return _obj


