from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.videoobject_tracking_async_object_tracking_async_data_class import (
        VideoobjectTrackingAsyncObjectTrackingAsyncDataClass,
    )


T = TypeVar("T", bound="VideoobjectTrackingAsyncModel")


@_attrs_define
class VideoobjectTrackingAsyncModel:
    """
    Attributes:
        google (Union[Unset, VideoobjectTrackingAsyncObjectTrackingAsyncDataClass]):
    """

    google: Union[Unset, "VideoobjectTrackingAsyncObjectTrackingAsyncDataClass"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        google: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.google, Unset):
            google = self.google.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if google is not UNSET:
            field_dict["google"] = google

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.videoobject_tracking_async_object_tracking_async_data_class import (
            VideoobjectTrackingAsyncObjectTrackingAsyncDataClass,
        )

        d = src_dict.copy()
        _google = d.pop("google", UNSET)
        google: Union[Unset, VideoobjectTrackingAsyncObjectTrackingAsyncDataClass]
        if isinstance(_google, Unset):
            google = UNSET
        else:
            google = VideoobjectTrackingAsyncObjectTrackingAsyncDataClass.from_dict(_google)

        videoobject_tracking_async_model = cls(
            google=google,
        )

        videoobject_tracking_async_model.additional_properties = d
        return videoobject_tracking_async_model

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
