from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.final_status_enum import FinalStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_track import ObjectTrack
    from ..models.videoobject_tracking_async_object_tracking_async_data_class_error import (
        VideoobjectTrackingAsyncObjectTrackingAsyncDataClassError,
    )


T = TypeVar("T", bound="VideoobjectTrackingAsyncObjectTrackingAsyncDataClass")


@_attrs_define
class VideoobjectTrackingAsyncObjectTrackingAsyncDataClass:
    """
    Attributes:
        id (str):
        final_status (FinalStatusEnum):
        objects (Union[Unset, List['ObjectTrack']]):
        original_response (Union[Unset, Any]): original response sent by the provider, hidden by default, show it by
            passing the `show_original_response` field to `true` in your request
        error (Union[Unset, VideoobjectTrackingAsyncObjectTrackingAsyncDataClassError]):
    """

    id: str
    final_status: FinalStatusEnum
    objects: Union[Unset, List["ObjectTrack"]] = UNSET
    original_response: Union[Unset, Any] = UNSET
    error: Union[Unset, "VideoobjectTrackingAsyncObjectTrackingAsyncDataClassError"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        final_status = self.final_status.value

        objects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.objects, Unset):
            objects = []
            for objects_item_data in self.objects:
                objects_item = objects_item_data.to_dict()
                objects.append(objects_item)

        original_response = self.original_response

        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "final_status": final_status,
            }
        )
        if objects is not UNSET:
            field_dict["objects"] = objects
        if original_response is not UNSET:
            field_dict["original_response"] = original_response
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.object_track import ObjectTrack
        from ..models.videoobject_tracking_async_object_tracking_async_data_class_error import (
            VideoobjectTrackingAsyncObjectTrackingAsyncDataClassError,
        )

        d = src_dict.copy()
        id = d.pop("id")

        final_status = FinalStatusEnum(d.pop("final_status"))

        objects = []
        _objects = d.pop("objects", UNSET)
        for objects_item_data in _objects or []:
            objects_item = ObjectTrack.from_dict(objects_item_data)

            objects.append(objects_item)

        original_response = d.pop("original_response", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, VideoobjectTrackingAsyncObjectTrackingAsyncDataClassError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = VideoobjectTrackingAsyncObjectTrackingAsyncDataClassError.from_dict(_error)

        videoobject_tracking_async_object_tracking_async_data_class = cls(
            id=id,
            final_status=final_status,
            objects=objects,
            original_response=original_response,
            error=error,
        )

        videoobject_tracking_async_object_tracking_async_data_class.additional_properties = d
        return videoobject_tracking_async_object_tracking_async_data_class

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
