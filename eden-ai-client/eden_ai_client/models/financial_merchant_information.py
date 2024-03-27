from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialMerchantInformation")


@_attrs_define
class FinancialMerchantInformation:
    """
    Attributes:
        name (Union[Unset, str]): Name of the merchant.
        address (Union[Unset, str]): Address of the merchant.
        phone (Union[Unset, str]): Phone number of the merchant.
        tax_id (Union[Unset, str]): Tax identification number of the merchant.
        id_reference (Union[Unset, str]): Unique reference ID for the merchant.
        vat_number (Union[Unset, str]): VAT (Value Added Tax) number of the merchant.
        abn_number (Union[Unset, str]): ABN (Australian Business Number) of the merchant.
        gst_number (Union[Unset, str]): GST (Goods and Services Tax) number of the merchant.
        business_number (Union[Unset, str]): Business registration number of the merchant.
        siret_number (Union[Unset, str]): SIRET (Système d'Identification du Répertoire des Entreprises et de leurs
            Établissements) number of the merchant.
        siren_number (Union[Unset, str]): SIREN (Système d'Identification du Répertoire des Entreprises) number of the
            merchant.
        pan_number (Union[Unset, str]): PAN (Permanent Account Number) of the merchant.
        coc_number (Union[Unset, str]): Chamber of Commerce registration number of the merchant.
        fiscal_number (Union[Unset, str]): Fiscal identification number of the merchant.
        email (Union[Unset, str]): Email address of the merchant.
        fax (Union[Unset, str]): Fax number of the merchant.
        website (Union[Unset, str]): Website of the merchant.
        registration (Union[Unset, str]): Official registration information of the merchant.
        city (Union[Unset, str]): City associated with the merchant's address.
        country (Union[Unset, str]): Country associated with the merchant's address.
        house_number (Union[Unset, str]): House number associated with the merchant's address.
        province (Union[Unset, str]): Province associated with the merchant's address.
        street_name (Union[Unset, str]): Street name associated with the merchant's address.
        zip_code (Union[Unset, str]): ZIP code associated with the merchant's address.
        country_code (Union[Unset, str]): Country code associated with the merchant's location.
    """

    name: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    tax_id: Union[Unset, str] = UNSET
    id_reference: Union[Unset, str] = UNSET
    vat_number: Union[Unset, str] = UNSET
    abn_number: Union[Unset, str] = UNSET
    gst_number: Union[Unset, str] = UNSET
    business_number: Union[Unset, str] = UNSET
    siret_number: Union[Unset, str] = UNSET
    siren_number: Union[Unset, str] = UNSET
    pan_number: Union[Unset, str] = UNSET
    coc_number: Union[Unset, str] = UNSET
    fiscal_number: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    fax: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    registration: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    house_number: Union[Unset, str] = UNSET
    province: Union[Unset, str] = UNSET
    street_name: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        address = self.address

        phone = self.phone

        tax_id = self.tax_id

        id_reference = self.id_reference

        vat_number = self.vat_number

        abn_number = self.abn_number

        gst_number = self.gst_number

        business_number = self.business_number

        siret_number = self.siret_number

        siren_number = self.siren_number

        pan_number = self.pan_number

        coc_number = self.coc_number

        fiscal_number = self.fiscal_number

        email = self.email

        fax = self.fax

        website = self.website

        registration = self.registration

        city = self.city

        country = self.country

        house_number = self.house_number

        province = self.province

        street_name = self.street_name

        zip_code = self.zip_code

        country_code = self.country_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if phone is not UNSET:
            field_dict["phone"] = phone
        if tax_id is not UNSET:
            field_dict["tax_id"] = tax_id
        if id_reference is not UNSET:
            field_dict["id_reference"] = id_reference
        if vat_number is not UNSET:
            field_dict["vat_number"] = vat_number
        if abn_number is not UNSET:
            field_dict["abn_number"] = abn_number
        if gst_number is not UNSET:
            field_dict["gst_number"] = gst_number
        if business_number is not UNSET:
            field_dict["business_number"] = business_number
        if siret_number is not UNSET:
            field_dict["siret_number"] = siret_number
        if siren_number is not UNSET:
            field_dict["siren_number"] = siren_number
        if pan_number is not UNSET:
            field_dict["pan_number"] = pan_number
        if coc_number is not UNSET:
            field_dict["coc_number"] = coc_number
        if fiscal_number is not UNSET:
            field_dict["fiscal_number"] = fiscal_number
        if email is not UNSET:
            field_dict["email"] = email
        if fax is not UNSET:
            field_dict["fax"] = fax
        if website is not UNSET:
            field_dict["website"] = website
        if registration is not UNSET:
            field_dict["registration"] = registration
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
        if country_code is not UNSET:
            field_dict["country_code"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        address = d.pop("address", UNSET)

        phone = d.pop("phone", UNSET)

        tax_id = d.pop("tax_id", UNSET)

        id_reference = d.pop("id_reference", UNSET)

        vat_number = d.pop("vat_number", UNSET)

        abn_number = d.pop("abn_number", UNSET)

        gst_number = d.pop("gst_number", UNSET)

        business_number = d.pop("business_number", UNSET)

        siret_number = d.pop("siret_number", UNSET)

        siren_number = d.pop("siren_number", UNSET)

        pan_number = d.pop("pan_number", UNSET)

        coc_number = d.pop("coc_number", UNSET)

        fiscal_number = d.pop("fiscal_number", UNSET)

        email = d.pop("email", UNSET)

        fax = d.pop("fax", UNSET)

        website = d.pop("website", UNSET)

        registration = d.pop("registration", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        house_number = d.pop("house_number", UNSET)

        province = d.pop("province", UNSET)

        street_name = d.pop("street_name", UNSET)

        zip_code = d.pop("zip_code", UNSET)

        country_code = d.pop("country_code", UNSET)

        financial_merchant_information = cls(
            name=name,
            address=address,
            phone=phone,
            tax_id=tax_id,
            id_reference=id_reference,
            vat_number=vat_number,
            abn_number=abn_number,
            gst_number=gst_number,
            business_number=business_number,
            siret_number=siret_number,
            siren_number=siren_number,
            pan_number=pan_number,
            coc_number=coc_number,
            fiscal_number=fiscal_number,
            email=email,
            fax=fax,
            website=website,
            registration=registration,
            city=city,
            country=country,
            house_number=house_number,
            province=province,
            street_name=street_name,
            zip_code=zip_code,
            country_code=country_code,
        )

        financial_merchant_information.additional_properties = d
        return financial_merchant_information

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
