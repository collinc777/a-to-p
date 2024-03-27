from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Country")


@_attrs_define
class Country:
    """
    Attributes:
        name (str):
        alpha2 (str):
        alpha3 (str):
        confidence (Union[Unset, int]):
    """

    name: str
    alpha2: str
    alpha3: str
    confidence: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        alpha2 = self.alpha2

        alpha3 = self.alpha3

        confidence = self.confidence

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "alpha2": alpha2,
                "alpha3": alpha3,
            }
        )
        if confidence is not UNSET:
            field_dict["confidence"] = confidence

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        alpha2 = d.pop("alpha2")

        alpha3 = d.pop("alpha3")

        confidence = d.pop("confidence", UNSET)

        country = cls(
            name=name,
            alpha2=alpha2,
            alpha3=alpha3,
            confidence=confidence,
        )

        country.additional_properties = d
        return country

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
