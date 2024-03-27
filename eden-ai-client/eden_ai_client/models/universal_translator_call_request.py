from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UniversalTranslatorCallRequest")


@_attrs_define
class UniversalTranslatorCallRequest:
    """
    Attributes:
        text (str): Text to analyze
        target_language (str): Target language code (ex: en, fr)
        source_language (Union[None, Unset, str]): Source language code (ex: en, fr)
    """

    text: str
    target_language: str
    source_language: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        target_language = self.target_language

        source_language: Union[None, Unset, str]
        if isinstance(self.source_language, Unset):
            source_language = UNSET
        else:
            source_language = self.source_language

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "target_language": target_language,
            }
        )
        if source_language is not UNSET:
            field_dict["source_language"] = source_language

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        text = self.text if isinstance(self.text, Unset) else (None, str(self.text).encode(), "text/plain")

        target_language = (
            self.target_language
            if isinstance(self.target_language, Unset)
            else (None, str(self.target_language).encode(), "text/plain")
        )

        source_language: Union[None, Unset, str]
        if isinstance(self.source_language, Unset):
            source_language = UNSET
        else:
            source_language = self.source_language

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "text": text,
                "target_language": target_language,
            }
        )
        if source_language is not UNSET:
            field_dict["source_language"] = source_language

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        target_language = d.pop("target_language")

        def _parse_source_language(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_language = _parse_source_language(d.pop("source_language", UNSET))

        universal_translator_call_request = cls(
            text=text,
            target_language=target_language,
            source_language=source_language,
        )

        universal_translator_call_request.additional_properties = d
        return universal_translator_call_request

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
