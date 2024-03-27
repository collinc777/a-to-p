from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.suggestion_item import SuggestionItem


T = TypeVar("T", bound="SpellCheckItem")


@_attrs_define
class SpellCheckItem:
    """Represents a spell check item with suggestions.

    Args:
        text (str): The text to spell check.
        type (str, optional): The type of the text.
        offset (int): The offset of the text.
        length (int): The length of the text.
        suggestions (Sequence[SuggestionItem], optional): The list of suggestions for the misspelled text.

    Raises:
        ValueError: If the offset or length is not positive.

    Returns:
        SpellCheckItem: An instance of the SpellCheckItem class.


    Attributes:
        text (str):
        type (str):
        offset (int):
        length (int):
        suggestions (Union[Unset, List['SuggestionItem']]):
    """

    text: str
    type: str
    offset: int
    length: int
    suggestions: Union[Unset, List["SuggestionItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        type = self.type

        offset = self.offset

        length = self.length

        suggestions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.suggestions, Unset):
            suggestions = []
            for suggestions_item_data in self.suggestions:
                suggestions_item = suggestions_item_data.to_dict()
                suggestions.append(suggestions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "type": type,
                "offset": offset,
                "length": length,
            }
        )
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.suggestion_item import SuggestionItem

        d = src_dict.copy()
        text = d.pop("text")

        type = d.pop("type")

        offset = d.pop("offset")

        length = d.pop("length")

        suggestions = []
        _suggestions = d.pop("suggestions", UNSET)
        for suggestions_item_data in _suggestions or []:
            suggestions_item = SuggestionItem.from_dict(suggestions_item_data)

            suggestions.append(suggestions_item)

        spell_check_item = cls(
            text=text,
            type=type,
            offset=offset,
            length=length,
            suggestions=suggestions,
        )

        spell_check_item.additional_properties = d
        return spell_check_item

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
