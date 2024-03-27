from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Taxes")


@_attrs_define
class Taxes:
    """
    Attributes:
        taxes (Union[Unset, int]):
        rate (Union[Unset, int]):
    """

    taxes: Union[Unset, int] = UNSET
    rate: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        taxes = self.taxes

        rate = self.rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        taxes = d.pop("taxes", UNSET)

        rate = d.pop("rate", UNSET)

        taxes = cls(
            taxes=taxes,
            rate=rate,
        )

        taxes.additional_properties = d
        return taxes

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
