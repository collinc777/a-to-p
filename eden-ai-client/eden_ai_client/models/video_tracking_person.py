from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.person_tracking import PersonTracking


T = TypeVar("T", bound="VideoTrackingPerson")


@_attrs_define
class VideoTrackingPerson:
    """
    Attributes:
        tracked (Union[Unset, List['PersonTracking']]):
    """

    tracked: Union[Unset, List["PersonTracking"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tracked: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tracked, Unset):
            tracked = []
            for tracked_item_data in self.tracked:
                tracked_item = tracked_item_data.to_dict()
                tracked.append(tracked_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tracked is not UNSET:
            field_dict["tracked"] = tracked

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.person_tracking import PersonTracking

        d = src_dict.copy()
        tracked = []
        _tracked = d.pop("tracked", UNSET)
        for tracked_item_data in _tracked or []:
            tracked_item = PersonTracking.from_dict(tracked_item_data)

            tracked.append(tracked_item)

        video_tracking_person = cls(
            tracked=tracked,
        )

        video_tracking_person.additional_properties = d
        return video_tracking_person

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
