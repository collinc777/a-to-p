from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MicrModel")


@_attrs_define
class MicrModel:
    """
    Attributes:
        raw (str):
        account_number (str):
        routing_number (str):
        serial_number (str):
        check_number (str):
    """

    raw: str
    account_number: str
    routing_number: str
    serial_number: str
    check_number: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        raw = self.raw

        account_number = self.account_number

        routing_number = self.routing_number

        serial_number = self.serial_number

        check_number = self.check_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "raw": raw,
                "account_number": account_number,
                "routing_number": routing_number,
                "serial_number": serial_number,
                "check_number": check_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        raw = d.pop("raw")

        account_number = d.pop("account_number")

        routing_number = d.pop("routing_number")

        serial_number = d.pop("serial_number")

        check_number = d.pop("check_number")

        micr_model = cls(
            raw=raw,
            account_number=account_number,
            routing_number=routing_number,
            serial_number=serial_number,
            check_number=check_number,
        )

        micr_model.additional_properties = d
        return micr_model

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
