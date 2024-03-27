from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialBankInformation")


@_attrs_define
class FinancialBankInformation:
    """
    Attributes:
        iban (Union[Unset, str]): International Bank Account Number.
        swift (Union[Unset, str]): Society for Worldwide Interbank Financial Telecommunication code.
        bsb (Union[Unset, str]): Bank State Branch code (Australia).
        sort_code (Union[Unset, str]): Sort code for UK banks.
        account_number (Union[Unset, str]): Bank account number.
        routing_number (Union[Unset, str]): Routing number for banks in the United States.
        bic (Union[Unset, str]): Bank Identifier Code.
    """

    iban: Union[Unset, str] = UNSET
    swift: Union[Unset, str] = UNSET
    bsb: Union[Unset, str] = UNSET
    sort_code: Union[Unset, str] = UNSET
    account_number: Union[Unset, str] = UNSET
    routing_number: Union[Unset, str] = UNSET
    bic: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        iban = self.iban

        swift = self.swift

        bsb = self.bsb

        sort_code = self.sort_code

        account_number = self.account_number

        routing_number = self.routing_number

        bic = self.bic

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if iban is not UNSET:
            field_dict["iban"] = iban
        if swift is not UNSET:
            field_dict["swift"] = swift
        if bsb is not UNSET:
            field_dict["bsb"] = bsb
        if sort_code is not UNSET:
            field_dict["sort_code"] = sort_code
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if routing_number is not UNSET:
            field_dict["routing_number"] = routing_number
        if bic is not UNSET:
            field_dict["bic"] = bic

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        iban = d.pop("iban", UNSET)

        swift = d.pop("swift", UNSET)

        bsb = d.pop("bsb", UNSET)

        sort_code = d.pop("sort_code", UNSET)

        account_number = d.pop("account_number", UNSET)

        routing_number = d.pop("routing_number", UNSET)

        bic = d.pop("bic", UNSET)

        financial_bank_information = cls(
            iban=iban,
            swift=swift,
            bsb=bsb,
            sort_code=sort_code,
            account_number=account_number,
            routing_number=routing_number,
            bic=bic,
        )

        financial_bank_information.additional_properties = d
        return financial_bank_information

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
