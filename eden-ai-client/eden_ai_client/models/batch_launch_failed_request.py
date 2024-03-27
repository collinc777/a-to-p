from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.batch_launch_failed_request_body import BatchLaunchFailedRequestBody
    from ..models.batch_launch_failed_request_errors import BatchLaunchFailedRequestErrors


T = TypeVar("T", bound="BatchLaunchFailedRequest")


@_attrs_define
class BatchLaunchFailedRequest:
    """
    Attributes:
        name (str): Request name, if any were given
        public_id (int): Request ID
        body (BatchLaunchFailedRequestBody): Parameters passed to the request
        errors (BatchLaunchFailedRequestErrors): Error received from the request validator
    """

    name: str
    public_id: int
    body: "BatchLaunchFailedRequestBody"
    errors: "BatchLaunchFailedRequestErrors"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        public_id = self.public_id

        body = self.body.to_dict()

        errors = self.errors.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "public_id": public_id,
                "body": body,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.batch_launch_failed_request_body import BatchLaunchFailedRequestBody
        from ..models.batch_launch_failed_request_errors import BatchLaunchFailedRequestErrors

        d = src_dict.copy()
        name = d.pop("name")

        public_id = d.pop("public_id")

        body = BatchLaunchFailedRequestBody.from_dict(d.pop("body"))

        errors = BatchLaunchFailedRequestErrors.from_dict(d.pop("errors"))

        batch_launch_failed_request = cls(
            name=name,
            public_id=public_id,
            body=body,
            errors=errors,
        )

        batch_launch_failed_request.additional_properties = d
        return batch_launch_failed_request

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
