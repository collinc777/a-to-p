from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.country import Country
    from ..models.item_identity_parser_data_class import ItemIdentityParserDataClass


T = TypeVar("T", bound="InfosIdentityParserDataClass")


@_attrs_define
class InfosIdentityParserDataClass:
    """
    Attributes:
        last_name (ItemIdentityParserDataClass):
        birth_place (ItemIdentityParserDataClass):
        birth_date (ItemIdentityParserDataClass):
        issuance_date (ItemIdentityParserDataClass):
        expire_date (ItemIdentityParserDataClass):
        document_id (ItemIdentityParserDataClass):
        issuing_state (ItemIdentityParserDataClass):
        address (ItemIdentityParserDataClass):
        age (ItemIdentityParserDataClass):
        country (Country):
        document_type (ItemIdentityParserDataClass):
        gender (ItemIdentityParserDataClass):
        mrz (ItemIdentityParserDataClass):
        nationality (ItemIdentityParserDataClass):
        given_names (Union[Unset, List['ItemIdentityParserDataClass']]):
        image_id (Union[Unset, List['ItemIdentityParserDataClass']]):
        image_signature (Union[Unset, List['ItemIdentityParserDataClass']]):
    """

    last_name: "ItemIdentityParserDataClass"
    birth_place: "ItemIdentityParserDataClass"
    birth_date: "ItemIdentityParserDataClass"
    issuance_date: "ItemIdentityParserDataClass"
    expire_date: "ItemIdentityParserDataClass"
    document_id: "ItemIdentityParserDataClass"
    issuing_state: "ItemIdentityParserDataClass"
    address: "ItemIdentityParserDataClass"
    age: "ItemIdentityParserDataClass"
    country: "Country"
    document_type: "ItemIdentityParserDataClass"
    gender: "ItemIdentityParserDataClass"
    mrz: "ItemIdentityParserDataClass"
    nationality: "ItemIdentityParserDataClass"
    given_names: Union[Unset, List["ItemIdentityParserDataClass"]] = UNSET
    image_id: Union[Unset, List["ItemIdentityParserDataClass"]] = UNSET
    image_signature: Union[Unset, List["ItemIdentityParserDataClass"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_name = self.last_name.to_dict()

        birth_place = self.birth_place.to_dict()

        birth_date = self.birth_date.to_dict()

        issuance_date = self.issuance_date.to_dict()

        expire_date = self.expire_date.to_dict()

        document_id = self.document_id.to_dict()

        issuing_state = self.issuing_state.to_dict()

        address = self.address.to_dict()

        age = self.age.to_dict()

        country = self.country.to_dict()

        document_type = self.document_type.to_dict()

        gender = self.gender.to_dict()

        mrz = self.mrz.to_dict()

        nationality = self.nationality.to_dict()

        given_names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.given_names, Unset):
            given_names = []
            for given_names_item_data in self.given_names:
                given_names_item = given_names_item_data.to_dict()
                given_names.append(given_names_item)

        image_id: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.image_id, Unset):
            image_id = []
            for image_id_item_data in self.image_id:
                image_id_item = image_id_item_data.to_dict()
                image_id.append(image_id_item)

        image_signature: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.image_signature, Unset):
            image_signature = []
            for image_signature_item_data in self.image_signature:
                image_signature_item = image_signature_item_data.to_dict()
                image_signature.append(image_signature_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "last_name": last_name,
                "birth_place": birth_place,
                "birth_date": birth_date,
                "issuance_date": issuance_date,
                "expire_date": expire_date,
                "document_id": document_id,
                "issuing_state": issuing_state,
                "address": address,
                "age": age,
                "country": country,
                "document_type": document_type,
                "gender": gender,
                "mrz": mrz,
                "nationality": nationality,
            }
        )
        if given_names is not UNSET:
            field_dict["given_names"] = given_names
        if image_id is not UNSET:
            field_dict["image_id"] = image_id
        if image_signature is not UNSET:
            field_dict["image_signature"] = image_signature

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.country import Country
        from ..models.item_identity_parser_data_class import ItemIdentityParserDataClass

        d = src_dict.copy()
        last_name = ItemIdentityParserDataClass.from_dict(d.pop("last_name"))

        birth_place = ItemIdentityParserDataClass.from_dict(d.pop("birth_place"))

        birth_date = ItemIdentityParserDataClass.from_dict(d.pop("birth_date"))

        issuance_date = ItemIdentityParserDataClass.from_dict(d.pop("issuance_date"))

        expire_date = ItemIdentityParserDataClass.from_dict(d.pop("expire_date"))

        document_id = ItemIdentityParserDataClass.from_dict(d.pop("document_id"))

        issuing_state = ItemIdentityParserDataClass.from_dict(d.pop("issuing_state"))

        address = ItemIdentityParserDataClass.from_dict(d.pop("address"))

        age = ItemIdentityParserDataClass.from_dict(d.pop("age"))

        country = Country.from_dict(d.pop("country"))

        document_type = ItemIdentityParserDataClass.from_dict(d.pop("document_type"))

        gender = ItemIdentityParserDataClass.from_dict(d.pop("gender"))

        mrz = ItemIdentityParserDataClass.from_dict(d.pop("mrz"))

        nationality = ItemIdentityParserDataClass.from_dict(d.pop("nationality"))

        given_names = []
        _given_names = d.pop("given_names", UNSET)
        for given_names_item_data in _given_names or []:
            given_names_item = ItemIdentityParserDataClass.from_dict(given_names_item_data)

            given_names.append(given_names_item)

        image_id = []
        _image_id = d.pop("image_id", UNSET)
        for image_id_item_data in _image_id or []:
            image_id_item = ItemIdentityParserDataClass.from_dict(image_id_item_data)

            image_id.append(image_id_item)

        image_signature = []
        _image_signature = d.pop("image_signature", UNSET)
        for image_signature_item_data in _image_signature or []:
            image_signature_item = ItemIdentityParserDataClass.from_dict(image_signature_item_data)

            image_signature.append(image_signature_item)

        infos_identity_parser_data_class = cls(
            last_name=last_name,
            birth_place=birth_place,
            birth_date=birth_date,
            issuance_date=issuance_date,
            expire_date=expire_date,
            document_id=document_id,
            issuing_state=issuing_state,
            address=address,
            age=age,
            country=country,
            document_type=document_type,
            gender=gender,
            mrz=mrz,
            nationality=nationality,
            given_names=given_names,
            image_id=image_id,
            image_signature=image_signature,
        )

        infos_identity_parser_data_class.additional_properties = d
        return infos_identity_parser_data_class

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
