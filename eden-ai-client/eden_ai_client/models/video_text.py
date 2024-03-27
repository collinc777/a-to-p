from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.video_text_frames import VideoTextFrames


T = TypeVar("T", bound="VideoText")


@_attrs_define
class VideoText:
    """
    Attributes:
        text (str):
        frames (Union[Unset, List['VideoTextFrames']]):
    """

    text: str
    frames: Union[Unset, List["VideoTextFrames"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

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
                "text": text,
            }
        )
        if frames is not UNSET:
            field_dict["frames"] = frames

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.video_text_frames import VideoTextFrames

        d = src_dict.copy()
        text = d.pop("text")

        frames = []
        _frames = d.pop("frames", UNSET)
        for frames_item_data in _frames or []:
            frames_item = VideoTextFrames.from_dict(frames_item_data)

            frames.append(frames_item)

        video_text = cls(
            text=text,
            frames=frames,
        )

        video_text.additional_properties = d
        return video_text

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
