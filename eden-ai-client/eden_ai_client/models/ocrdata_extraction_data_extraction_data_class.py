from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_f43_enum import StatusF43Enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_data_extraction import ItemDataExtraction


T = TypeVar("T", bound="OcrdataExtractionDataExtractionDataClass")


@_attrs_define
class OcrdataExtractionDataExtractionDataClass:
    """
    Attributes:
        status (StatusF43Enum):
        fields (Union[Unset, List['ItemDataExtraction']]):
        original_response (Union[Unset, Any]): original response sent by the provider, hidden by default, show it by
            passing the `show_original_response` field to `true` in your request
    """

    status: StatusF43Enum
    fields: Union[Unset, List["ItemDataExtraction"]] = UNSET
    original_response: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        original_response = self.original_response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if fields is not UNSET:
            field_dict["fields"] = fields
        if original_response is not UNSET:
            field_dict["original_response"] = original_response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_data_extraction import ItemDataExtraction

        d = src_dict.copy()
        status = StatusF43Enum(d.pop("status"))

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = ItemDataExtraction.from_dict(fields_item_data)

            fields.append(fields_item)

        original_response = d.pop("original_response", UNSET)

        ocrdata_extraction_data_extraction_data_class = cls(
            status=status,
            fields=fields,
            original_response=original_response,
        )

        ocrdata_extraction_data_extraction_data_class.additional_properties = d
        return ocrdata_extraction_data_extraction_data_class

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
