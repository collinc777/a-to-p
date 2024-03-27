import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prompt_text_params_type_0 import PromptTextParamsType0


T = TypeVar("T", bound="PromptText")


@_attrs_define
class PromptText:
    """
    Attributes:
        name (str):
        text (str):
        feature (str):
        subfeature (str):
        provider (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        model (Union[None, Unset, str]):
        params (Union['PromptTextParamsType0', None, Unset]):
    """

    name: str
    text: str
    feature: str
    subfeature: str
    provider: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    model: Union[None, Unset, str] = UNSET
    params: Union["PromptTextParamsType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.prompt_text_params_type_0 import PromptTextParamsType0

        name = self.name

        text = self.text

        feature = self.feature

        subfeature = self.subfeature

        provider = self.provider

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        model: Union[None, Unset, str]
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        params: Union[Dict[str, Any], None, Unset]
        if isinstance(self.params, Unset):
            params = UNSET
        elif isinstance(self.params, PromptTextParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "text": text,
                "feature": feature,
                "subfeature": subfeature,
                "provider": provider,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.prompt_text_params_type_0 import PromptTextParamsType0

        d = src_dict.copy()
        name = d.pop("name")

        text = d.pop("text")

        feature = d.pop("feature")

        subfeature = d.pop("subfeature")

        provider = d.pop("provider")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_params(data: object) -> Union["PromptTextParamsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = PromptTextParamsType0.from_dict(data)

                return params_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PromptTextParamsType0", None, Unset], data)

        params = _parse_params(d.pop("params", UNSET))

        prompt_text = cls(
            name=name,
            text=text,
            feature=feature,
            subfeature=subfeature,
            provider=provider,
            created_at=created_at,
            updated_at=updated_at,
            model=model,
            params=params,
        )

        prompt_text.additional_properties = d
        return prompt_text

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
