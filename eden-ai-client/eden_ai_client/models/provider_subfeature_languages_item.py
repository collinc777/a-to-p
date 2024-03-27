from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderSubfeatureLanguagesItem")


@_attrs_define
class ProviderSubfeatureLanguagesItem:
    """
    Attributes:
        language_name (Union[Unset, str]):
        language_code (Union[Unset, str]):
    """

    language_name: Union[Unset, str] = UNSET
    language_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language_name = self.language_name

        language_code = self.language_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language_name is not UNSET:
            field_dict["language_name"] = language_name
        if language_code is not UNSET:
            field_dict["language_code"] = language_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language_name = d.pop("language_name", UNSET)

        language_code = d.pop("language_code", UNSET)

        provider_subfeature_languages_item = cls(
            language_name=language_name,
            language_code=language_code,
        )

        provider_subfeature_languages_item.additional_properties = d
        return provider_subfeature_languages_item

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
