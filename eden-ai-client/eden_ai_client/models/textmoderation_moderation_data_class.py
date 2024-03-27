from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_f43_enum import StatusF43Enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_moderation_item import TextModerationItem


T = TypeVar("T", bound="TextmoderationModerationDataClass")


@_attrs_define
class TextmoderationModerationDataClass:
    """
    Attributes:
        nsfw_likelihood (int):
        nsfw_likelihood_score (int):
        status (StatusF43Enum):
        items (Union[Unset, List['TextModerationItem']]):
        original_response (Union[Unset, Any]): original response sent by the provider, hidden by default, show it by
            passing the `show_original_response` field to `true` in your request
    """

    nsfw_likelihood: int
    nsfw_likelihood_score: int
    status: StatusF43Enum
    items: Union[Unset, List["TextModerationItem"]] = UNSET
    original_response: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nsfw_likelihood = self.nsfw_likelihood

        nsfw_likelihood_score = self.nsfw_likelihood_score

        status = self.status.value

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        original_response = self.original_response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nsfw_likelihood": nsfw_likelihood,
                "nsfw_likelihood_score": nsfw_likelihood_score,
                "status": status,
            }
        )
        if items is not UNSET:
            field_dict["items"] = items
        if original_response is not UNSET:
            field_dict["original_response"] = original_response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.text_moderation_item import TextModerationItem

        d = src_dict.copy()
        nsfw_likelihood = d.pop("nsfw_likelihood")

        nsfw_likelihood_score = d.pop("nsfw_likelihood_score")

        status = StatusF43Enum(d.pop("status"))

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = TextModerationItem.from_dict(items_item_data)

            items.append(items_item)

        original_response = d.pop("original_response", UNSET)

        textmoderation_moderation_data_class = cls(
            nsfw_likelihood=nsfw_likelihood,
            nsfw_likelihood_score=nsfw_likelihood_score,
            status=status,
            items=items,
            original_response=original_response,
        )

        textmoderation_moderation_data_class.additional_properties = d
        return textmoderation_moderation_data_class

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
