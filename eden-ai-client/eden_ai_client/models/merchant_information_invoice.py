from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MerchantInformationInvoice")


@_attrs_define
class MerchantInformationInvoice:
    """
    Attributes:
        merchant_name (str):
        merchant_address (str):
        merchant_phone (str):
        merchant_email (str):
        merchant_fax (str):
        merchant_website (str):
        merchant_tax_id (str):
        merchant_siret (str):
        merchant_siren (str):
        abn_number (str):
        gst_number (str):
        pan_number (str):
        vat_number (str):
    """

    merchant_name: str
    merchant_address: str
    merchant_phone: str
    merchant_email: str
    merchant_fax: str
    merchant_website: str
    merchant_tax_id: str
    merchant_siret: str
    merchant_siren: str
    abn_number: str
    gst_number: str
    pan_number: str
    vat_number: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        merchant_name = self.merchant_name

        merchant_address = self.merchant_address

        merchant_phone = self.merchant_phone

        merchant_email = self.merchant_email

        merchant_fax = self.merchant_fax

        merchant_website = self.merchant_website

        merchant_tax_id = self.merchant_tax_id

        merchant_siret = self.merchant_siret

        merchant_siren = self.merchant_siren

        abn_number = self.abn_number

        gst_number = self.gst_number

        pan_number = self.pan_number

        vat_number = self.vat_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "merchant_name": merchant_name,
                "merchant_address": merchant_address,
                "merchant_phone": merchant_phone,
                "merchant_email": merchant_email,
                "merchant_fax": merchant_fax,
                "merchant_website": merchant_website,
                "merchant_tax_id": merchant_tax_id,
                "merchant_siret": merchant_siret,
                "merchant_siren": merchant_siren,
                "abn_number": abn_number,
                "gst_number": gst_number,
                "pan_number": pan_number,
                "vat_number": vat_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        merchant_name = d.pop("merchant_name")

        merchant_address = d.pop("merchant_address")

        merchant_phone = d.pop("merchant_phone")

        merchant_email = d.pop("merchant_email")

        merchant_fax = d.pop("merchant_fax")

        merchant_website = d.pop("merchant_website")

        merchant_tax_id = d.pop("merchant_tax_id")

        merchant_siret = d.pop("merchant_siret")

        merchant_siren = d.pop("merchant_siren")

        abn_number = d.pop("abn_number")

        gst_number = d.pop("gst_number")

        pan_number = d.pop("pan_number")

        vat_number = d.pop("vat_number")

        merchant_information_invoice = cls(
            merchant_name=merchant_name,
            merchant_address=merchant_address,
            merchant_phone=merchant_phone,
            merchant_email=merchant_email,
            merchant_fax=merchant_fax,
            merchant_website=merchant_website,
            merchant_tax_id=merchant_tax_id,
            merchant_siret=merchant_siret,
            merchant_siren=merchant_siren,
            abn_number=abn_number,
            gst_number=gst_number,
            pan_number=pan_number,
            vat_number=vat_number,
        )

        merchant_information_invoice.additional_properties = d
        return merchant_information_invoice

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
