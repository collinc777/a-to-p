from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.video_logo import VideoLogo


T = TypeVar("T", bound="LogoTrack")


@_attrs_define
class LogoTrack:
    """
    Attributes:
        description (str):
        tracking (Union[Unset, List['VideoLogo']]):
    """

    description: str
    tracking: Union[Unset, List["VideoLogo"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        tracking: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tracking, Unset):
            tracking = []
            for tracking_item_data in self.tracking:
                tracking_item = tracking_item_data.to_dict()
                tracking.append(tracking_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
            }
        )
        if tracking is not UNSET:
            field_dict["tracking"] = tracking

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.video_logo import VideoLogo

        d = src_dict.copy()
        description = d.pop("description")

        tracking = []
        _tracking = d.pop("tracking", UNSET)
        for tracking_item_data in _tracking or []:
            tracking_item = VideoLogo.from_dict(tracking_item_data)

            tracking.append(tracking_item)

        logo_track = cls(
            description=description,
            tracking=tracking,
        )

        logo_track.additional_properties = d
        return logo_track

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
