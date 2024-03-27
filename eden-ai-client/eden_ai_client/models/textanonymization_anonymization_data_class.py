from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_f43_enum import StatusF43Enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anonymization_entity import AnonymizationEntity


T = TypeVar("T", bound="TextanonymizationAnonymizationDataClass")


@_attrs_define
class TextanonymizationAnonymizationDataClass:
    """
    Attributes:
        result (str):
        status (StatusF43Enum):
        entities (Union[Unset, List['AnonymizationEntity']]):
        original_response (Union[Unset, Any]): original response sent by the provider, hidden by default, show it by
            passing the `show_original_response` field to `true` in your request
    """

    result: str
    status: StatusF43Enum
    entities: Union[Unset, List["AnonymizationEntity"]] = UNSET
    original_response: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result = self.result

        status = self.status.value

        entities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entities, Unset):
            entities = []
            for entities_item_data in self.entities:
                entities_item = entities_item_data.to_dict()
                entities.append(entities_item)

        original_response = self.original_response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result": result,
                "status": status,
            }
        )
        if entities is not UNSET:
            field_dict["entities"] = entities
        if original_response is not UNSET:
            field_dict["original_response"] = original_response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.anonymization_entity import AnonymizationEntity

        d = src_dict.copy()
        result = d.pop("result")

        status = StatusF43Enum(d.pop("status"))

        entities = []
        _entities = d.pop("entities", UNSET)
        for entities_item_data in _entities or []:
            entities_item = AnonymizationEntity.from_dict(entities_item_data)

            entities.append(entities_item)

        original_response = d.pop("original_response", UNSET)

        textanonymization_anonymization_data_class = cls(
            result=result,
            status=status,
            entities=entities,
            original_response=original_response,
        )

        textanonymization_anonymization_data_class.additional_properties = d
        return textanonymization_anonymization_data_class

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
