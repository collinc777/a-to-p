from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InfosLanguageDetectionDataClass")


@_attrs_define
class InfosLanguageDetectionDataClass:
    """
    Attributes:
        language (str):
        display_name (str):
        confidence (int):
    """

    language: str
    display_name: str
    confidence: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language

        display_name = self.display_name

        confidence = self.confidence

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
                "display_name": display_name,
                "confidence": confidence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language = d.pop("language")

        display_name = d.pop("display_name")

        confidence = d.pop("confidence")

        infos_language_detection_data_class = cls(
            language=language,
            display_name=display_name,
            confidence=confidence,
        )

        infos_language_detection_data_class.additional_properties = d
        return infos_language_detection_data_class

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
