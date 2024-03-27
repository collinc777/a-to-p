from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MerchantInformation")


@_attrs_define
class MerchantInformation:
    """
    Attributes:
        merchant_name (Union[Unset, str]):
        merchant_address (Union[Unset, str]):
        merchant_phone (Union[Unset, str]):
        merchant_url (Union[Unset, str]):
        merchant_siret (Union[Unset, str]):
        merchant_siren (Union[Unset, str]):
        merchant_vat_number (Union[Unset, str]):
        merchant_gst_number (Union[Unset, str]):
        merchant_abn_number (Union[Unset, str]):
    """

    merchant_name: Union[Unset, str] = UNSET
    merchant_address: Union[Unset, str] = UNSET
    merchant_phone: Union[Unset, str] = UNSET
    merchant_url: Union[Unset, str] = UNSET
    merchant_siret: Union[Unset, str] = UNSET
    merchant_siren: Union[Unset, str] = UNSET
    merchant_vat_number: Union[Unset, str] = UNSET
    merchant_gst_number: Union[Unset, str] = UNSET
    merchant_abn_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        merchant_name = self.merchant_name

        merchant_address = self.merchant_address

        merchant_phone = self.merchant_phone

        merchant_url = self.merchant_url

        merchant_siret = self.merchant_siret

        merchant_siren = self.merchant_siren

        merchant_vat_number = self.merchant_vat_number

        merchant_gst_number = self.merchant_gst_number

        merchant_abn_number = self.merchant_abn_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if merchant_name is not UNSET:
            field_dict["merchant_name"] = merchant_name
        if merchant_address is not UNSET:
            field_dict["merchant_address"] = merchant_address
        if merchant_phone is not UNSET:
            field_dict["merchant_phone"] = merchant_phone
        if merchant_url is not UNSET:
            field_dict["merchant_url"] = merchant_url
        if merchant_siret is not UNSET:
            field_dict["merchant_siret"] = merchant_siret
        if merchant_siren is not UNSET:
            field_dict["merchant_siren"] = merchant_siren
        if merchant_vat_number is not UNSET:
            field_dict["merchant_vat_number"] = merchant_vat_number
        if merchant_gst_number is not UNSET:
            field_dict["merchant_gst_number"] = merchant_gst_number
        if merchant_abn_number is not UNSET:
            field_dict["merchant_abn_number"] = merchant_abn_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        merchant_name = d.pop("merchant_name", UNSET)

        merchant_address = d.pop("merchant_address", UNSET)

        merchant_phone = d.pop("merchant_phone", UNSET)

        merchant_url = d.pop("merchant_url", UNSET)

        merchant_siret = d.pop("merchant_siret", UNSET)

        merchant_siren = d.pop("merchant_siren", UNSET)

        merchant_vat_number = d.pop("merchant_vat_number", UNSET)

        merchant_gst_number = d.pop("merchant_gst_number", UNSET)

        merchant_abn_number = d.pop("merchant_abn_number", UNSET)

        merchant_information = cls(
            merchant_name=merchant_name,
            merchant_address=merchant_address,
            merchant_phone=merchant_phone,
            merchant_url=merchant_url,
            merchant_siret=merchant_siret,
            merchant_siren=merchant_siren,
            merchant_vat_number=merchant_vat_number,
            merchant_gst_number=merchant_gst_number,
            merchant_abn_number=merchant_abn_number,
        )

        merchant_information.additional_properties = d
        return merchant_information

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
