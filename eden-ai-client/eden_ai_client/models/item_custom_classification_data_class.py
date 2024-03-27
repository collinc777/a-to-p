from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ItemCustomClassificationDataClass")


@_attrs_define
class ItemCustomClassificationDataClass:
    """
    Attributes:
        input_ (str):
        label (str):
        confidence (int):
    """

    input_: str
    label: str
    confidence: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        input_ = self.input_

        label = self.label

        confidence = self.confidence

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input": input_,
                "label": label,
                "confidence": confidence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        input_ = d.pop("input")

        label = d.pop("label")

        confidence = d.pop("confidence")

        item_custom_classification_data_class = cls(
            input_=input_,
            label=label,
            confidence=confidence,
        )

        item_custom_classification_data_class.additional_properties = d
        return item_custom_classification_data_class

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
