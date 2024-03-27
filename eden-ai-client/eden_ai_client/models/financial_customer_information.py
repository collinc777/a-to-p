from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialCustomerInformation")


@_attrs_define
class FinancialCustomerInformation:
    """
    Attributes:
        name (Union[Unset, str]): The name of the invoiced customer.
        id_reference (Union[Unset, str]): Unique reference ID for the customer.
        mailling_address (Union[Unset, str]): The mailing address of the customer.
        billing_address (Union[Unset, str]): The explicit billing address for the customer.
        shipping_address (Union[Unset, str]): The shipping address for the customer.
        service_address (Union[Unset, str]): The service address associated with the customer.
        remittance_address (Union[Unset, str]): The address to which payments should be remitted.
        email (Union[Unset, str]): The email address of the customer.
        phone (Union[Unset, str]): The phone number associated with the customer.
        vat_number (Union[Unset, str]): VAT (Value Added Tax) number of the customer.
        abn_number (Union[Unset, str]): ABN (Australian Business Number) of the customer.
        gst_number (Union[Unset, str]): GST (Goods and Services Tax) number of the customer.
        pan_number (Union[Unset, str]): PAN (Permanent Account Number) of the customer.
        business_number (Union[Unset, str]): Business registration number of the customer.
        siret_number (Union[Unset, str]): SIRET (Système d'Identification du Répertoire des Entreprises et de leurs
            Établissements) number of the customer.
        siren_number (Union[Unset, str]): SIREN (Système d'Identification du Répertoire des Entreprises) number of the
            customer.
        customer_number (Union[Unset, str]): Customer identification number.
        coc_number (Union[Unset, str]): Chamber of Commerce registration number.
        fiscal_number (Union[Unset, str]): Fiscal identification number of the customer.
        registration_number (Union[Unset, str]): Official registration number of the customer.
        tax_id (Union[Unset, str]): Tax identification number of the customer.
        website (Union[Unset, str]): The website associated with the customer.
        remit_to_name (Union[Unset, str]): The name associated with the customer's remittance address.
        city (Union[Unset, str]): The city associated with the customer's address.
        country (Union[Unset, str]): The country associated with the customer's address.
        house_number (Union[Unset, str]): The house number associated with the customer's address.
        province (Union[Unset, str]): The province associated with the customer's address.
        street_name (Union[Unset, str]): The street name associated with the customer's address.
        zip_code (Union[Unset, str]): The ZIP code associated with the customer's address.
        municipality (Union[Unset, str]): The municipality associated with the customer's address.
    """

    name: Union[Unset, str] = UNSET
    id_reference: Union[Unset, str] = UNSET
    mailling_address: Union[Unset, str] = UNSET
    billing_address: Union[Unset, str] = UNSET
    shipping_address: Union[Unset, str] = UNSET
    service_address: Union[Unset, str] = UNSET
    remittance_address: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    vat_number: Union[Unset, str] = UNSET
    abn_number: Union[Unset, str] = UNSET
    gst_number: Union[Unset, str] = UNSET
    pan_number: Union[Unset, str] = UNSET
    business_number: Union[Unset, str] = UNSET
    siret_number: Union[Unset, str] = UNSET
    siren_number: Union[Unset, str] = UNSET
    customer_number: Union[Unset, str] = UNSET
    coc_number: Union[Unset, str] = UNSET
    fiscal_number: Union[Unset, str] = UNSET
    registration_number: Union[Unset, str] = UNSET
    tax_id: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    remit_to_name: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    house_number: Union[Unset, str] = UNSET
    province: Union[Unset, str] = UNSET
    street_name: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    municipality: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        id_reference = self.id_reference

        mailling_address = self.mailling_address

        billing_address = self.billing_address

        shipping_address = self.shipping_address

        service_address = self.service_address

        remittance_address = self.remittance_address

        email = self.email

        phone = self.phone

        vat_number = self.vat_number

        abn_number = self.abn_number

        gst_number = self.gst_number

        pan_number = self.pan_number

        business_number = self.business_number

        siret_number = self.siret_number

        siren_number = self.siren_number

        customer_number = self.customer_number

        coc_number = self.coc_number

        fiscal_number = self.fiscal_number

        registration_number = self.registration_number

        tax_id = self.tax_id

        website = self.website

        remit_to_name = self.remit_to_name

        city = self.city

        country = self.country

        house_number = self.house_number

        province = self.province

        street_name = self.street_name

        zip_code = self.zip_code

        municipality = self.municipality

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if id_reference is not UNSET:
            field_dict["id_reference"] = id_reference
        if mailling_address is not UNSET:
            field_dict["mailling_address"] = mailling_address
        if billing_address is not UNSET:
            field_dict["billing_address"] = billing_address
        if shipping_address is not UNSET:
            field_dict["shipping_address"] = shipping_address
        if service_address is not UNSET:
            field_dict["service_address"] = service_address
        if remittance_address is not UNSET:
            field_dict["remittance_address"] = remittance_address
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if vat_number is not UNSET:
            field_dict["vat_number"] = vat_number
        if abn_number is not UNSET:
            field_dict["abn_number"] = abn_number
        if gst_number is not UNSET:
            field_dict["gst_number"] = gst_number
        if pan_number is not UNSET:
            field_dict["pan_number"] = pan_number
        if business_number is not UNSET:
            field_dict["business_number"] = business_number
        if siret_number is not UNSET:
            field_dict["siret_number"] = siret_number
        if siren_number is not UNSET:
            field_dict["siren_number"] = siren_number
        if customer_number is not UNSET:
            field_dict["customer_number"] = customer_number
        if coc_number is not UNSET:
            field_dict["coc_number"] = coc_number
        if fiscal_number is not UNSET:
            field_dict["fiscal_number"] = fiscal_number
        if registration_number is not UNSET:
            field_dict["registration_number"] = registration_number
        if tax_id is not UNSET:
            field_dict["tax_id"] = tax_id
        if website is not UNSET:
            field_dict["website"] = website
        if remit_to_name is not UNSET:
            field_dict["remit_to_name"] = remit_to_name
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if house_number is not UNSET:
            field_dict["house_number"] = house_number
        if province is not UNSET:
            field_dict["province"] = province
        if street_name is not UNSET:
            field_dict["street_name"] = street_name
        if zip_code is not UNSET:
            field_dict["zip_code"] = zip_code
        if municipality is not UNSET:
            field_dict["municipality"] = municipality

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        id_reference = d.pop("id_reference", UNSET)

        mailling_address = d.pop("mailling_address", UNSET)

        billing_address = d.pop("billing_address", UNSET)

        shipping_address = d.pop("shipping_address", UNSET)

        service_address = d.pop("service_address", UNSET)

        remittance_address = d.pop("remittance_address", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        vat_number = d.pop("vat_number", UNSET)

        abn_number = d.pop("abn_number", UNSET)

        gst_number = d.pop("gst_number", UNSET)

        pan_number = d.pop("pan_number", UNSET)

        business_number = d.pop("business_number", UNSET)

        siret_number = d.pop("siret_number", UNSET)

        siren_number = d.pop("siren_number", UNSET)

        customer_number = d.pop("customer_number", UNSET)

        coc_number = d.pop("coc_number", UNSET)

        fiscal_number = d.pop("fiscal_number", UNSET)

        registration_number = d.pop("registration_number", UNSET)

        tax_id = d.pop("tax_id", UNSET)

        website = d.pop("website", UNSET)

        remit_to_name = d.pop("remit_to_name", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        house_number = d.pop("house_number", UNSET)

        province = d.pop("province", UNSET)

        street_name = d.pop("street_name", UNSET)

        zip_code = d.pop("zip_code", UNSET)

        municipality = d.pop("municipality", UNSET)

        financial_customer_information = cls(
            name=name,
            id_reference=id_reference,
            mailling_address=mailling_address,
            billing_address=billing_address,
            shipping_address=shipping_address,
            service_address=service_address,
            remittance_address=remittance_address,
            email=email,
            phone=phone,
            vat_number=vat_number,
            abn_number=abn_number,
            gst_number=gst_number,
            pan_number=pan_number,
            business_number=business_number,
            siret_number=siret_number,
            siren_number=siren_number,
            customer_number=customer_number,
            coc_number=coc_number,
            fiscal_number=fiscal_number,
            registration_number=registration_number,
            tax_id=tax_id,
            website=website,
            remit_to_name=remit_to_name,
            city=city,
            country=country,
            house_number=house_number,
            province=province,
            street_name=street_name,
            zip_code=zip_code,
            municipality=municipality,
        )

        financial_customer_information.additional_properties = d
        return financial_customer_information

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
