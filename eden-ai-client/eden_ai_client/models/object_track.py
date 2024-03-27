from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_frame import ObjectFrame


T = TypeVar("T", bound="ObjectTrack")


@_attrs_define
class ObjectTrack:
    """
    Attributes:
        description (str):
        confidence (int):
        frames (Union[Unset, List['ObjectFrame']]):
    """

    description: str
    confidence: int
    frames: Union[Unset, List["ObjectFrame"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        confidence = self.confidence

        frames: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.frames, Unset):
            frames = []
            for frames_item_data in self.frames:
                frames_item = frames_item_data.to_dict()
                frames.append(frames_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "confidence": confidence,
            }
        )
        if frames is not UNSET:
            field_dict["frames"] = frames

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.object_frame import ObjectFrame

        d = src_dict.copy()
        description = d.pop("description")

        confidence = d.pop("confidence")

        frames = []
        _frames = d.pop("frames", UNSET)
        for frames_item_data in _frames or []:
            frames_item = ObjectFrame.from_dict(frames_item_data)

            frames.append(frames_item)

        object_track = cls(
            description=description,
            confidence=confidence,
            frames=frames,
        )

        object_track.additional_properties = d
        return object_track

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
