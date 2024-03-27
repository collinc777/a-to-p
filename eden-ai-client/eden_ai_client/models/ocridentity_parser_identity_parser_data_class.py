from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_f43_enum import StatusF43Enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.infos_identity_parser_data_class import InfosIdentityParserDataClass


T = TypeVar("T", bound="OcridentityParserIdentityParserDataClass")


@_attrs_define
class OcridentityParserIdentityParserDataClass:
    """
    Attributes:
        status (StatusF43Enum):
        extracted_data (Union[Unset, List['InfosIdentityParserDataClass']]):
        original_response (Union[Unset, Any]): original response sent by the provider, hidden by default, show it by
            passing the `show_original_response` field to `true` in your request
    """

    status: StatusF43Enum
    extracted_data: Union[Unset, List["InfosIdentityParserDataClass"]] = UNSET
    original_response: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        extracted_data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.extracted_data, Unset):
            extracted_data = []
            for extracted_data_item_data in self.extracted_data:
                extracted_data_item = extracted_data_item_data.to_dict()
                extracted_data.append(extracted_data_item)

        original_response = self.original_response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if extracted_data is not UNSET:
            field_dict["extracted_data"] = extracted_data
        if original_response is not UNSET:
            field_dict["original_response"] = original_response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.infos_identity_parser_data_class import InfosIdentityParserDataClass

        d = src_dict.copy()
        status = StatusF43Enum(d.pop("status"))

        extracted_data = []
        _extracted_data = d.pop("extracted_data", UNSET)
        for extracted_data_item_data in _extracted_data or []:
            extracted_data_item = InfosIdentityParserDataClass.from_dict(extracted_data_item_data)

            extracted_data.append(extracted_data_item)

        original_response = d.pop("original_response", UNSET)

        ocridentity_parser_identity_parser_data_class = cls(
            status=status,
            extracted_data=extracted_data,
            original_response=original_response,
        )

        ocridentity_parser_identity_parser_data_class.additional_properties = d
        return ocridentity_parser_identity_parser_data_class

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
