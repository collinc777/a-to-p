from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SuggestionItem")


@_attrs_define
class SuggestionItem:
    """
    Represents a suggestion for a misspelled word.

    Args:
        suggestion (str): The suggested text.
        score (float, optional): The score of the suggested text (between 0 and 1).

    Raises:
        ValueError: If the score is not between 0 and 1.

    Returns:
        SuggestionItem: An instance of the SuggestionItem class.


    Attributes:
        suggestion (str):
        score (int):
    """

    suggestion: str
    score: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        suggestion = self.suggestion

        score = self.score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "suggestion": suggestion,
                "score": score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        suggestion = d.pop("suggestion")

        score = d.pop("score")

        suggestion_item = cls(
            suggestion=suggestion,
            score=score,
        )

        suggestion_item.additional_properties = d
        return suggestion_item

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
