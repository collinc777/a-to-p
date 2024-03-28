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
from openapi_client.models.pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559363588336 import PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559363588336
from openapi_client.models.pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559367610192 import PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559367610192
from openapi_client.models.pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559367908288 import PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559367908288
from openapi_client.models.pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559367909232 import PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559367909232
from openapi_client.models.pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559368075040 import PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368075040
from openapi_client.models.pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559368093952 import PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368093952
from openapi_client.models.pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559368095440 import PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368095440
from openapi_client.models.pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559368287712 import PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368287712
from openapi_client.models.pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559368301216 import PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368301216
from openapi_client.models.pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559368307872 import PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368307872
from openapi_client.models.pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559368343216 import PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368343216
from openapi_client.models.pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559368347584 import PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368347584
from typing import Optional, Set
from typing_extensions import Self

class TextsentimentAnalysisResponseModel(BaseModel):
    """
    TextsentimentAnalysisResponseModel
    """ # noqa: E501
    sapling: Optional[PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559363588336] = None
    tenstorrent: Optional[PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559367610192] = None
    microsoft: Optional[PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368307872] = None
    ibm: Optional[PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368301216] = None
    emvista: Optional[PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559367908288] = None
    google: Optional[PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559367909232] = None
    oneai: Optional[PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368287712] = None
    amazon: Optional[PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368075040] = None
    lettria: Optional[PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368093952] = None
    nlpcloud: Optional[PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368095440] = None
    openai: Optional[PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368343216] = None
    connexun: Optional[PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368347584] = None
    __properties: ClassVar[List[str]] = ["sapling", "tenstorrent", "microsoft", "ibm", "emvista", "google", "oneai", "amazon", "lettria", "nlpcloud", "openai", "connexun"]

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
        """Create an instance of TextsentimentAnalysisResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of sapling
        if self.sapling:
            _dict['sapling'] = self.sapling.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tenstorrent
        if self.tenstorrent:
            _dict['tenstorrent'] = self.tenstorrent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of microsoft
        if self.microsoft:
            _dict['microsoft'] = self.microsoft.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ibm
        if self.ibm:
            _dict['ibm'] = self.ibm.to_dict()
        # override the default output from pydantic by calling `to_dict()` of emvista
        if self.emvista:
            _dict['emvista'] = self.emvista.to_dict()
        # override the default output from pydantic by calling `to_dict()` of google
        if self.google:
            _dict['google'] = self.google.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oneai
        if self.oneai:
            _dict['oneai'] = self.oneai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amazon
        if self.amazon:
            _dict['amazon'] = self.amazon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lettria
        if self.lettria:
            _dict['lettria'] = self.lettria.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nlpcloud
        if self.nlpcloud:
            _dict['nlpcloud'] = self.nlpcloud.to_dict()
        # override the default output from pydantic by calling `to_dict()` of openai
        if self.openai:
            _dict['openai'] = self.openai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of connexun
        if self.connexun:
            _dict['connexun'] = self.connexun.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TextsentimentAnalysisResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sapling": PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559363588336.from_dict(obj["sapling"]) if obj.get("sapling") is not None else None,
            "tenstorrent": PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559367610192.from_dict(obj["tenstorrent"]) if obj.get("tenstorrent") is not None else None,
            "microsoft": PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368307872.from_dict(obj["microsoft"]) if obj.get("microsoft") is not None else None,
            "ibm": PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368301216.from_dict(obj["ibm"]) if obj.get("ibm") is not None else None,
            "emvista": PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559367908288.from_dict(obj["emvista"]) if obj.get("emvista") is not None else None,
            "google": PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559367909232.from_dict(obj["google"]) if obj.get("google") is not None else None,
            "oneai": PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368287712.from_dict(obj["oneai"]) if obj.get("oneai") is not None else None,
            "amazon": PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368075040.from_dict(obj["amazon"]) if obj.get("amazon") is not None else None,
            "lettria": PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368093952.from_dict(obj["lettria"]) if obj.get("lettria") is not None else None,
            "nlpcloud": PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368095440.from_dict(obj["nlpcloud"]) if obj.get("nlpcloud") is not None else None,
            "openai": PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368343216.from_dict(obj["openai"]) if obj.get("openai") is not None else None,
            "connexun": PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368347584.from_dict(obj["connexun"]) if obj.get("connexun") is not None else None
        })
        return _obj

