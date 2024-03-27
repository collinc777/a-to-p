from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.entity_sentiment_enum import EntitySentimentEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Entity")


@_attrs_define
class Entity:
    """
    Attributes:
        type (str): Recognized Entity type
        text (str): Text corresponding to the entity
        sentiment (EntitySentimentEnum):
        begin_offset (Union[Unset, int]):
        end_offset (Union[Unset, int]):
    """

    type: str
    text: str
    sentiment: EntitySentimentEnum
    begin_offset: Union[Unset, int] = UNSET
    end_offset: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        text = self.text

        sentiment = self.sentiment.value

        begin_offset = self.begin_offset

        end_offset = self.end_offset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "text": text,
                "sentiment": sentiment,
            }
        )
        if begin_offset is not UNSET:
            field_dict["begin_offset"] = begin_offset
        if end_offset is not UNSET:
            field_dict["end_offset"] = end_offset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        text = d.pop("text")

        sentiment = EntitySentimentEnum(d.pop("sentiment"))

        begin_offset = d.pop("begin_offset", UNSET)

        end_offset = d.pop("end_offset", UNSET)

        entity = cls(
            type=type,
            text=text,
            sentiment=sentiment,
            begin_offset=begin_offset,
            end_offset=end_offset,
        )

        entity.additional_properties = d
        return entity

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
