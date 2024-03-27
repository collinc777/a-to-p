from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plagia_detection_candidate import PlagiaDetectionCandidate


T = TypeVar("T", bound="PlagiaDetectionItem")


@_attrs_define
class PlagiaDetectionItem:
    """
    Attributes:
        text (str):
        candidates (Union[Unset, List['PlagiaDetectionCandidate']]):
    """

    text: str
    candidates: Union[Unset, List["PlagiaDetectionCandidate"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        candidates: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.candidates, Unset):
            candidates = []
            for candidates_item_data in self.candidates:
                candidates_item = candidates_item_data.to_dict()
                candidates.append(candidates_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if candidates is not UNSET:
            field_dict["candidates"] = candidates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plagia_detection_candidate import PlagiaDetectionCandidate

        d = src_dict.copy()
        text = d.pop("text")

        candidates = []
        _candidates = d.pop("candidates", UNSET)
        for candidates_item_data in _candidates or []:
            candidates_item = PlagiaDetectionCandidate.from_dict(candidates_item_data)

            candidates.append(candidates_item)

        plagia_detection_item = cls(
            text=text,
            candidates=candidates,
        )

        plagia_detection_item.additional_properties = d
        return plagia_detection_item

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
