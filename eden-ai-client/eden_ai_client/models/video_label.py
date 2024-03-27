from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.video_label_bounding_box import VideoLabelBoundingBox
    from ..models.video_label_time_stamp import VideoLabelTimeStamp


T = TypeVar("T", bound="VideoLabel")


@_attrs_define
class VideoLabel:
    """
    Attributes:
        name (str):
        confidence (int):
        timestamp (Union[Unset, List['VideoLabelTimeStamp']]):
        category (Union[Unset, List[str]]):
        bounding_box (Union[Unset, List['VideoLabelBoundingBox']]):
    """

    name: str
    confidence: int
    timestamp: Union[Unset, List["VideoLabelTimeStamp"]] = UNSET
    category: Union[Unset, List[str]] = UNSET
    bounding_box: Union[Unset, List["VideoLabelBoundingBox"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        confidence = self.confidence

        timestamp: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = []
            for timestamp_item_data in self.timestamp:
                timestamp_item = timestamp_item_data.to_dict()
                timestamp.append(timestamp_item)

        category: Union[Unset, List[str]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        bounding_box: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bounding_box, Unset):
            bounding_box = []
            for bounding_box_item_data in self.bounding_box:
                bounding_box_item = bounding_box_item_data.to_dict()
                bounding_box.append(bounding_box_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "confidence": confidence,
            }
        )
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if category is not UNSET:
            field_dict["category"] = category
        if bounding_box is not UNSET:
            field_dict["bounding_box"] = bounding_box

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.video_label_bounding_box import VideoLabelBoundingBox
        from ..models.video_label_time_stamp import VideoLabelTimeStamp

        d = src_dict.copy()
        name = d.pop("name")

        confidence = d.pop("confidence")

        timestamp = []
        _timestamp = d.pop("timestamp", UNSET)
        for timestamp_item_data in _timestamp or []:
            timestamp_item = VideoLabelTimeStamp.from_dict(timestamp_item_data)

            timestamp.append(timestamp_item)

        category = cast(List[str], d.pop("category", UNSET))

        bounding_box = []
        _bounding_box = d.pop("bounding_box", UNSET)
        for bounding_box_item_data in _bounding_box or []:
            bounding_box_item = VideoLabelBoundingBox.from_dict(bounding_box_item_data)

            bounding_box.append(bounding_box_item)

        video_label = cls(
            name=name,
            confidence=confidence,
            timestamp=timestamp,
            category=category,
            bounding_box=bounding_box,
        )

        video_label.additional_properties = d
        return video_label

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
