from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InfosNamedEntityRecognitionDataClass")


@_attrs_define
class InfosNamedEntityRecognitionDataClass:
    """
    Attributes:
        entity (str):
        category (str):
        importance (int):
    """

    entity: str
    category: str
    importance: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity = self.entity

        category = self.category

        importance = self.importance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity": entity,
                "category": category,
                "importance": importance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entity = d.pop("entity")

        category = d.pop("category")

        importance = d.pop("importance")

        infos_named_entity_recognition_data_class = cls(
            entity=entity,
            category=category,
            importance=importance,
        )

        infos_named_entity_recognition_data_class.additional_properties = d
        return infos_named_entity_recognition_data_class

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
