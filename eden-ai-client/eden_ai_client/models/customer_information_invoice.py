from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerInformationInvoice")


@_attrs_define
class CustomerInformationInvoice:
    """
    Attributes:
        customer_name (str):
        customer_address (str):
        customer_email (str):
        customer_id (str):
        customer_tax_id (str):
        customer_mailing_address (str):
        customer_billing_address (str):
        customer_shipping_address (str):
        customer_service_address (str):
        customer_remittance_address (str):
        abn_number (str):
        gst_number (str):
        pan_number (str):
        vat_number (str):
        siret_number (Union[Unset, str]):
        siren_number (Union[Unset, str]):
    """

    customer_name: str
    customer_address: str
    customer_email: str
    customer_id: str
    customer_tax_id: str
    customer_mailing_address: str
    customer_billing_address: str
    customer_shipping_address: str
    customer_service_address: str
    customer_remittance_address: str
    abn_number: str
    gst_number: str
    pan_number: str
    vat_number: str
    siret_number: Union[Unset, str] = UNSET
    siren_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_name = self.customer_name

        customer_address = self.customer_address

        customer_email = self.customer_email

        customer_id = self.customer_id

        customer_tax_id = self.customer_tax_id

        customer_mailing_address = self.customer_mailing_address

        customer_billing_address = self.customer_billing_address

        customer_shipping_address = self.customer_shipping_address

        customer_service_address = self.customer_service_address

        customer_remittance_address = self.customer_remittance_address

        abn_number = self.abn_number

        gst_number = self.gst_number

        pan_number = self.pan_number

        vat_number = self.vat_number

        siret_number = self.siret_number

        siren_number = self.siren_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer_name": customer_name,
                "customer_address": customer_address,
                "customer_email": customer_email,
                "customer_id": customer_id,
                "customer_tax_id": customer_tax_id,
                "customer_mailing_address": customer_mailing_address,
                "customer_billing_address": customer_billing_address,
                "customer_shipping_address": customer_shipping_address,
                "customer_service_address": customer_service_address,
                "customer_remittance_address": customer_remittance_address,
                "abn_number": abn_number,
                "gst_number": gst_number,
                "pan_number": pan_number,
                "vat_number": vat_number,
            }
        )
        if siret_number is not UNSET:
            field_dict["siret_number"] = siret_number
        if siren_number is not UNSET:
            field_dict["siren_number"] = siren_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        customer_name = d.pop("customer_name")

        customer_address = d.pop("customer_address")

        customer_email = d.pop("customer_email")

        customer_id = d.pop("customer_id")

        customer_tax_id = d.pop("customer_tax_id")

        customer_mailing_address = d.pop("customer_mailing_address")

        customer_billing_address = d.pop("customer_billing_address")

        customer_shipping_address = d.pop("customer_shipping_address")

        customer_service_address = d.pop("customer_service_address")

        customer_remittance_address = d.pop("customer_remittance_address")

        abn_number = d.pop("abn_number")

        gst_number = d.pop("gst_number")

        pan_number = d.pop("pan_number")

        vat_number = d.pop("vat_number")

        siret_number = d.pop("siret_number", UNSET)

        siren_number = d.pop("siren_number", UNSET)

        customer_information_invoice = cls(
            customer_name=customer_name,
            customer_address=customer_address,
            customer_email=customer_email,
            customer_id=customer_id,
            customer_tax_id=customer_tax_id,
            customer_mailing_address=customer_mailing_address,
            customer_billing_address=customer_billing_address,
            customer_shipping_address=customer_shipping_address,
            customer_service_address=customer_service_address,
            customer_remittance_address=customer_remittance_address,
            abn_number=abn_number,
            gst_number=gst_number,
            pan_number=pan_number,
            vat_number=vat_number,
            siret_number=siret_number,
            siren_number=siren_number,
        )

        customer_information_invoice.additional_properties = d
        return customer_information_invoice

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
