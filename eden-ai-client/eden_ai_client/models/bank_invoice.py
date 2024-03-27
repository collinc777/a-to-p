from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BankInvoice")


@_attrs_define
class BankInvoice:
    """
    Attributes:
        account_number (str):
        iban (str):
        bsb (str):
        sort_code (str):
        vat_number (str):
        rooting_number (str):
        swift (str):
    """

    account_number: str
    iban: str
    bsb: str
    sort_code: str
    vat_number: str
    rooting_number: str
    swift: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_number = self.account_number

        iban = self.iban

        bsb = self.bsb

        sort_code = self.sort_code

        vat_number = self.vat_number

        rooting_number = self.rooting_number

        swift = self.swift

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_number": account_number,
                "iban": iban,
                "bsb": bsb,
                "sort_code": sort_code,
                "vat_number": vat_number,
                "rooting_number": rooting_number,
                "swift": swift,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_number = d.pop("account_number")

        iban = d.pop("iban")

        bsb = d.pop("bsb")

        sort_code = d.pop("sort_code")

        vat_number = d.pop("vat_number")

        rooting_number = d.pop("rooting_number")

        swift = d.pop("swift")

        bank_invoice = cls(
            account_number=account_number,
            iban=iban,
            bsb=bsb,
            sort_code=sort_code,
            vat_number=vat_number,
            rooting_number=rooting_number,
            swift=swift,
        )

        bank_invoice.additional_properties = d
        return bank_invoice

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
