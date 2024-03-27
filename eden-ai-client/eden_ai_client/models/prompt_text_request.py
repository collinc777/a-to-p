import json
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prompt_text_request_params_type_0 import PromptTextRequestParamsType0


T = TypeVar("T", bound="PromptTextRequest")


@_attrs_define
class PromptTextRequest:
    """
    Attributes:
        text (str):
        feature (str):
        subfeature (str):
        provider (str):
        model (Union[None, Unset, str]):
        params (Union['PromptTextRequestParamsType0', None, Unset]):
    """

    text: str
    feature: str
    subfeature: str
    provider: str
    model: Union[None, Unset, str] = UNSET
    params: Union["PromptTextRequestParamsType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.prompt_text_request_params_type_0 import PromptTextRequestParamsType0

        text = self.text

        feature = self.feature

        subfeature = self.subfeature

        provider = self.provider

        model: Union[None, Unset, str]
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        params: Union[Dict[str, Any], None, Unset]
        if isinstance(self.params, Unset):
            params = UNSET
        elif isinstance(self.params, PromptTextRequestParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "feature": feature,
                "subfeature": subfeature,
                "provider": provider,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        text = self.text if isinstance(self.text, Unset) else (None, str(self.text).encode(), "text/plain")

        feature = self.feature if isinstance(self.feature, Unset) else (None, str(self.feature).encode(), "text/plain")

        subfeature = (
            self.subfeature
            if isinstance(self.subfeature, Unset)
            else (None, str(self.subfeature).encode(), "text/plain")
        )

        provider = (
            self.provider if isinstance(self.provider, Unset) else (None, str(self.provider).encode(), "text/plain")
        )

        model: Union[None, Unset, str]
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        params: Union[None, Tuple[None, bytes, str], Unset]
        if isinstance(self.params, Unset):
            params = UNSET
        elif isinstance(self.params, PromptTextRequestParamsType0):
            params = (None, json.dumps(self.params.to_dict()).encode(), "application/json")
        else:
            params = self.params

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "text": text,
                "feature": feature,
                "subfeature": subfeature,
                "provider": provider,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.prompt_text_request_params_type_0 import PromptTextRequestParamsType0

        d = src_dict.copy()
        text = d.pop("text")

        feature = d.pop("feature")

        subfeature = d.pop("subfeature")

        provider = d.pop("provider")

        def _parse_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_params(data: object) -> Union["PromptTextRequestParamsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = PromptTextRequestParamsType0.from_dict(data)

                return params_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PromptTextRequestParamsType0", None, Unset], data)

        params = _parse_params(d.pop("params", UNSET))

        prompt_text_request = cls(
            text=text,
            feature=feature,
            subfeature=subfeature,
            provider=provider,
            model=model,
            params=params,
        )

        prompt_text_request.additional_properties = d
        return prompt_text_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
