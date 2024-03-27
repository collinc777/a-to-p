from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.final_status_enum import FinalStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.video_face import VideoFace
    from ..models.videoface_detection_async_face_detection_async_data_class_error import (
        VideofaceDetectionAsyncFaceDetectionAsyncDataClassError,
    )


T = TypeVar("T", bound="VideofaceDetectionAsyncFaceDetectionAsyncDataClass")


@_attrs_define
class VideofaceDetectionAsyncFaceDetectionAsyncDataClass:
    """
    Attributes:
        id (str):
        final_status (FinalStatusEnum):
        faces (Union[Unset, List['VideoFace']]):
        original_response (Union[Unset, Any]): original response sent by the provider, hidden by default, show it by
            passing the `show_original_response` field to `true` in your request
        error (Union[Unset, VideofaceDetectionAsyncFaceDetectionAsyncDataClassError]):
    """

    id: str
    final_status: FinalStatusEnum
    faces: Union[Unset, List["VideoFace"]] = UNSET
    original_response: Union[Unset, Any] = UNSET
    error: Union[Unset, "VideofaceDetectionAsyncFaceDetectionAsyncDataClassError"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        final_status = self.final_status.value

        faces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.faces, Unset):
            faces = []
            for faces_item_data in self.faces:
                faces_item = faces_item_data.to_dict()
                faces.append(faces_item)

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
        if faces is not UNSET:
            field_dict["faces"] = faces
        if original_response is not UNSET:
            field_dict["original_response"] = original_response
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.video_face import VideoFace
        from ..models.videoface_detection_async_face_detection_async_data_class_error import (
            VideofaceDetectionAsyncFaceDetectionAsyncDataClassError,
        )

        d = src_dict.copy()
        id = d.pop("id")

        final_status = FinalStatusEnum(d.pop("final_status"))

        faces = []
        _faces = d.pop("faces", UNSET)
        for faces_item_data in _faces or []:
            faces_item = VideoFace.from_dict(faces_item_data)

            faces.append(faces_item)

        original_response = d.pop("original_response", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, VideofaceDetectionAsyncFaceDetectionAsyncDataClassError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = VideofaceDetectionAsyncFaceDetectionAsyncDataClassError.from_dict(_error)

        videoface_detection_async_face_detection_async_data_class = cls(
            id=id,
            final_status=final_status,
            faces=faces,
            original_response=original_response,
            error=error,
        )

        videoface_detection_async_face_detection_async_data_class.additional_properties = d
        return videoface_detection_async_face_detection_async_data_class

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
