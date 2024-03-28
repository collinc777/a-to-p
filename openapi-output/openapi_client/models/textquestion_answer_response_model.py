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
from openapi_client.models.pydantic_main_textquestion_answer_question_answer_data_class94559363483456 import PydanticMainTextquestionAnswerQuestionAnswerDataClass94559363483456
from openapi_client.models.pydantic_main_textquestion_answer_question_answer_data_class94559368883120 import PydanticMainTextquestionAnswerQuestionAnswerDataClass94559368883120
from openapi_client.models.pydantic_main_textquestion_answer_question_answer_data_class94559368992208 import PydanticMainTextquestionAnswerQuestionAnswerDataClass94559368992208
from openapi_client.models.pydantic_main_textquestion_answer_question_answer_data_class94559369027328 import PydanticMainTextquestionAnswerQuestionAnswerDataClass94559369027328
from typing import Optional, Set
from typing_extensions import Self

class TextquestionAnswerResponseModel(BaseModel):
    """
    TextquestionAnswerResponseModel
    """ # noqa: E501
    tenstorrent: Optional[PydanticMainTextquestionAnswerQuestionAnswerDataClass94559368992208] = None
    huggingface: Optional[PydanticMainTextquestionAnswerQuestionAnswerDataClass94559369027328] = None
    openai: Optional[PydanticMainTextquestionAnswerQuestionAnswerDataClass94559368883120] = None
    eden_ai: Optional[PydanticMainTextquestionAnswerQuestionAnswerDataClass94559363483456] = Field(default=None, alias="eden-ai")
    __properties: ClassVar[List[str]] = ["tenstorrent", "huggingface", "openai", "eden-ai"]

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
        """Create an instance of TextquestionAnswerResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of tenstorrent
        if self.tenstorrent:
            _dict['tenstorrent'] = self.tenstorrent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of huggingface
        if self.huggingface:
            _dict['huggingface'] = self.huggingface.to_dict()
        # override the default output from pydantic by calling `to_dict()` of openai
        if self.openai:
            _dict['openai'] = self.openai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of eden_ai
        if self.eden_ai:
            _dict['eden-ai'] = self.eden_ai.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TextquestionAnswerResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenstorrent": PydanticMainTextquestionAnswerQuestionAnswerDataClass94559368992208.from_dict(obj["tenstorrent"]) if obj.get("tenstorrent") is not None else None,
            "huggingface": PydanticMainTextquestionAnswerQuestionAnswerDataClass94559369027328.from_dict(obj["huggingface"]) if obj.get("huggingface") is not None else None,
            "openai": PydanticMainTextquestionAnswerQuestionAnswerDataClass94559368883120.from_dict(obj["openai"]) if obj.get("openai") is not None else None,
            "eden-ai": PydanticMainTextquestionAnswerQuestionAnswerDataClass94559363483456.from_dict(obj["eden-ai"]) if obj.get("eden-ai") is not None else None
        })
        return _obj


