from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.videoobject_tracking_async_model import VideoobjectTrackingAsyncModel


T = TypeVar("T", bound="AsyncvideoobjectTrackingAsyncResponseModel")


@_attrs_define
class AsyncvideoobjectTrackingAsyncResponseModel:
    """
    Attributes:
        results (VideoobjectTrackingAsyncModel):
        error (str):
        public_id (str):
        status (str):
    """

    results: "VideoobjectTrackingAsyncModel"
    error: str
    public_id: str
    status: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results = self.results.to_dict()

        error = self.error

        public_id = self.public_id

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "error": error,
                "public_id": public_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.videoobject_tracking_async_model import VideoobjectTrackingAsyncModel

        d = src_dict.copy()
        results = VideoobjectTrackingAsyncModel.from_dict(d.pop("results"))

        error = d.pop("error")

        public_id = d.pop("public_id")

        status = d.pop("status")

        asyncvideoobject_tracking_async_response_model = cls(
            results=results,
            error=error,
            public_id=public_id,
            status=status,
        )

        asyncvideoobject_tracking_async_response_model.additional_properties = d
        return asyncvideoobject_tracking_async_response_model

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
