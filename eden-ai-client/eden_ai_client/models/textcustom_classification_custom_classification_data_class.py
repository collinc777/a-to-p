from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_f43_enum import StatusF43Enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_custom_classification_data_class import ItemCustomClassificationDataClass


T = TypeVar("T", bound="TextcustomClassificationCustomClassificationDataClass")


@_attrs_define
class TextcustomClassificationCustomClassificationDataClass:
    """
    Attributes:
        status (StatusF43Enum):
        classifications (Union[Unset, List['ItemCustomClassificationDataClass']]):
        original_response (Union[Unset, Any]): original response sent by the provider, hidden by default, show it by
            passing the `show_original_response` field to `true` in your request
    """

    status: StatusF43Enum
    classifications: Union[Unset, List["ItemCustomClassificationDataClass"]] = UNSET
    original_response: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        classifications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.classifications, Unset):
            classifications = []
            for classifications_item_data in self.classifications:
                classifications_item = classifications_item_data.to_dict()
                classifications.append(classifications_item)

        original_response = self.original_response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if classifications is not UNSET:
            field_dict["classifications"] = classifications
        if original_response is not UNSET:
            field_dict["original_response"] = original_response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_custom_classification_data_class import ItemCustomClassificationDataClass

        d = src_dict.copy()
        status = StatusF43Enum(d.pop("status"))

        classifications = []
        _classifications = d.pop("classifications", UNSET)
        for classifications_item_data in _classifications or []:
            classifications_item = ItemCustomClassificationDataClass.from_dict(classifications_item_data)

            classifications.append(classifications_item)

        original_response = d.pop("original_response", UNSET)

        textcustom_classification_custom_classification_data_class = cls(
            status=status,
            classifications=classifications,
            original_response=original_response,
        )

        textcustom_classification_custom_classification_data_class.additional_properties = d
        return textcustom_classification_custom_classification_data_class

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