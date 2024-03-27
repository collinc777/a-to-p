from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InfosKeywordExtractionDataClass")


@_attrs_define
class InfosKeywordExtractionDataClass:
    """
    Attributes:
        keyword (str):
        importance (int):
    """

    keyword: str
    importance: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keyword = self.keyword

        importance = self.importance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keyword": keyword,
                "importance": importance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keyword = d.pop("keyword")

        importance = d.pop("importance")

        infos_keyword_extraction_data_class = cls(
            keyword=keyword,
            importance=importance,
        )

        infos_keyword_extraction_data_class.additional_properties = d
        return infos_keyword_extraction_data_class

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
