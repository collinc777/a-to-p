from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialLocalInformation")


@_attrs_define
class FinancialLocalInformation:
    """
    Attributes:
        currency (Union[Unset, str]): Currency used in financial transactions.
        currency_code (Union[Unset, str]): Currency code (e.g., USD, EUR).
        currency_exchange_rate (Union[Unset, str]): Exchange rate for the specified currency.
        country (Union[Unset, str]): Country associated with the local financial information.
        language (Union[Unset, str]): Language used in financial transactions.
    """

    currency: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    currency_exchange_rate: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency

        currency_code = self.currency_code

        currency_exchange_rate = self.currency_exchange_rate

        country = self.country

        language = self.language

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if currency_exchange_rate is not UNSET:
            field_dict["currency_exchange_rate"] = currency_exchange_rate
        if country is not UNSET:
            field_dict["country"] = country
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency = d.pop("currency", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        currency_exchange_rate = d.pop("currency_exchange_rate", UNSET)

        country = d.pop("country", UNSET)

        language = d.pop("language", UNSET)

        financial_local_information = cls(
            currency=currency,
            currency_code=currency_code,
            currency_exchange_rate=currency_exchange_rate,
            country=country,
            language=language,
        )

        financial_local_information.additional_properties = d
        return financial_local_information

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
