from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResumeLocation")


@_attrs_define
class ResumeLocation:
    """
    Attributes:
        formatted_location (str):
        postal_code (str):
        region (str):
        country (str):
        country_code (str):
        raw_input_location (str):
        street (str):
        street_number (str):
        appartment_number (str):
        city (str):
    """

    formatted_location: str
    postal_code: str
    region: str
    country: str
    country_code: str
    raw_input_location: str
    street: str
    street_number: str
    appartment_number: str
    city: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        formatted_location = self.formatted_location

        postal_code = self.postal_code

        region = self.region

        country = self.country

        country_code = self.country_code

        raw_input_location = self.raw_input_location

        street = self.street

        street_number = self.street_number

        appartment_number = self.appartment_number

        city = self.city

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "formatted_location": formatted_location,
                "postal_code": postal_code,
                "region": region,
                "country": country,
                "country_code": country_code,
                "raw_input_location": raw_input_location,
                "street": street,
                "street_number": street_number,
                "appartment_number": appartment_number,
                "city": city,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        formatted_location = d.pop("formatted_location")

        postal_code = d.pop("postal_code")

        region = d.pop("region")

        country = d.pop("country")

        country_code = d.pop("country_code")

        raw_input_location = d.pop("raw_input_location")

        street = d.pop("street")

        street_number = d.pop("street_number")

        appartment_number = d.pop("appartment_number")

        city = d.pop("city")

        resume_location = cls(
            formatted_location=formatted_location,
            postal_code=postal_code,
            region=region,
            country=country,
            country_code=country_code,
            raw_input_location=raw_input_location,
            street=street,
            street_number=street_number,
            appartment_number=appartment_number,
            city=city,
        )

        resume_location.additional_properties = d
        return resume_location

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
