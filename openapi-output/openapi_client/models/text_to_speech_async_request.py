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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.text_to_speech_async_request_option import TextToSpeechAsyncRequestOption
from typing import Optional, Set
from typing_extensions import Self

class TextToSpeechAsyncRequest(BaseModel):
    """
    TextToSpeechAsyncRequest
    """ # noqa: E501
    providers: Annotated[str, Field(min_length=1, strict=True)] = Field(description="It can be one (ex: **'amazon'** or **'google'**) or multiple provider(s) (ex: **'amazon,microsoft,google'**)             that the data will be redirected to in order to get the processed results.")
    fallback_providers: Optional[StrictStr] = Field(default=None, description="Providers in this list will be used as fallback if the call to provider in `providers` parameter fails.     To use this feature, you must input **only one** provider in the `providers` parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn't fail.   *Doesn't work with async subfeatures.*     ")
    show_original_response: Optional[StrictBool] = Field(default=False, description="Optional : Shows the original response of the provider.<br>         When set to **true**, a new attribute *original_response* will appear in the response object.")
    webhook_receiver: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Webhook receiver should be a valid https URL (ex : https://your.listner.com/endpoint).             After the processing is done, the webhook endpoint will receive a POST request with the result.")
    users_webhook_parameters: Optional[Dict[str, Any]] = Field(default=None, description="Json data that contains of additional parameters that will be sent back to the webhook receiver             (ex: api key for security or client's data ID to link the result internally).             Will only be used when webhook_receiver is set.")
    settings: Optional[StrictStr] = Field(default=None, description="A dictionnary or a json object to specify specific models to use for some providers. <br>                     It can be in the following format: {\"google\" : \"google_model\", \"ibm\": \"ibm_model\"...}.                      **Caution**: setting models can be done only with `Content-Type` : `application/json`.                      ")
    text: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Text to analyze")
    language: Optional[StrictStr] = Field(default='', description="Language code expected (ex: en, fr)")
    option: Optional[TextToSpeechAsyncRequestOption] = None
    rate: Optional[Annotated[int, Field(le=100, strict=True, ge=-100)]] = Field(default=0, description="Increase or decrease the speaking rate by expressing a positif or negatif number ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%)")
    pitch: Optional[Annotated[int, Field(le=100, strict=True, ge=-100)]] = Field(default=0, description="Increase or decrease the speaking pitch by expressing a positif or negatif number ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%)")
    volume: Optional[Annotated[int, Field(le=100, strict=True, ge=-100)]] = Field(default=0, description="Increase or decrease the audio volume by expressing a positif or negatif number ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%)")
    audio_format: Optional[StrictStr] = Field(default='', description="Optional parameter to specify the audio format in which the audio will be generated. By default,             audios are encoded in MP3, except for lovoai which use the wav container.")
    sampling_rate: Optional[Annotated[int, Field(le=200000, strict=True, ge=0)]] = Field(default=0, description="Optional. The synthesis sample rate (in hertz) for this audio. When this is specified, the audio will be converted             either to the right passed value, or to a the nearest value acceptable by the provider")
    __properties: ClassVar[List[str]] = ["providers", "fallback_providers", "show_original_response", "webhook_receiver", "users_webhook_parameters", "settings", "text", "language", "option", "rate", "pitch", "volume", "audio_format", "sampling_rate"]

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
        """Create an instance of TextToSpeechAsyncRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of option
        if self.option:
            _dict['option'] = self.option.to_dict()
        # set to None if fallback_providers (nullable) is None
        # and model_fields_set contains the field
        if self.fallback_providers is None and "fallback_providers" in self.model_fields_set:
            _dict['fallback_providers'] = None

        # set to None if language (nullable) is None
        # and model_fields_set contains the field
        if self.language is None and "language" in self.model_fields_set:
            _dict['language'] = None

        # set to None if rate (nullable) is None
        # and model_fields_set contains the field
        if self.rate is None and "rate" in self.model_fields_set:
            _dict['rate'] = None

        # set to None if pitch (nullable) is None
        # and model_fields_set contains the field
        if self.pitch is None and "pitch" in self.model_fields_set:
            _dict['pitch'] = None

        # set to None if volume (nullable) is None
        # and model_fields_set contains the field
        if self.volume is None and "volume" in self.model_fields_set:
            _dict['volume'] = None

        # set to None if audio_format (nullable) is None
        # and model_fields_set contains the field
        if self.audio_format is None and "audio_format" in self.model_fields_set:
            _dict['audio_format'] = None

        # set to None if sampling_rate (nullable) is None
        # and model_fields_set contains the field
        if self.sampling_rate is None and "sampling_rate" in self.model_fields_set:
            _dict['sampling_rate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TextToSpeechAsyncRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "providers": obj.get("providers"),
            "fallback_providers": obj.get("fallback_providers"),
            "show_original_response": obj.get("show_original_response") if obj.get("show_original_response") is not None else False,
            "webhook_receiver": obj.get("webhook_receiver"),
            "users_webhook_parameters": obj.get("users_webhook_parameters"),
            "settings": obj.get("settings"),
            "text": obj.get("text"),
            "language": obj.get("language") if obj.get("language") is not None else '',
            "option": TextToSpeechAsyncRequestOption.from_dict(obj["option"]) if obj.get("option") is not None else None,
            "rate": obj.get("rate") if obj.get("rate") is not None else 0,
            "pitch": obj.get("pitch") if obj.get("pitch") is not None else 0,
            "volume": obj.get("volume") if obj.get("volume") is not None else 0,
            "audio_format": obj.get("audio_format") if obj.get("audio_format") is not None else '',
            "sampling_rate": obj.get("sampling_rate") if obj.get("sampling_rate") is not None else 0
        })
        return _obj


