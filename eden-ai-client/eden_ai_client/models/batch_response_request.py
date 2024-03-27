from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_e80_enum import StatusE80Enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_response_request_errors_type_0 import BatchResponseRequestErrorsType0
    from ..models.batch_response_request_response_type_0 import BatchResponseRequestResponseType0


T = TypeVar("T", bound="BatchResponseRequest")


@_attrs_define
class BatchResponseRequest:
    """
    Attributes:
        public_id (int):
        status (Union[Unset, StatusE80Enum]): * `succeeded` - Status Succeeded
            * `failed` - Status Failed
            * `finished` - Status Finished
            * `processing` - Status Processing
        name (Union[None, Unset, str]):
        errors (Union['BatchResponseRequestErrorsType0', None, Unset]):
        response (Union['BatchResponseRequestResponseType0', None, Unset]):
    """

    public_id: int
    status: Union[Unset, StatusE80Enum] = UNSET
    name: Union[None, Unset, str] = UNSET
    errors: Union["BatchResponseRequestErrorsType0", None, Unset] = UNSET
    response: Union["BatchResponseRequestResponseType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.batch_response_request_errors_type_0 import BatchResponseRequestErrorsType0
        from ..models.batch_response_request_response_type_0 import BatchResponseRequestResponseType0

        public_id = self.public_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        errors: Union[Dict[str, Any], None, Unset]
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, BatchResponseRequestErrorsType0):
            errors = self.errors.to_dict()
        else:
            errors = self.errors

        response: Union[Dict[str, Any], None, Unset]
        if isinstance(self.response, Unset):
            response = UNSET
        elif isinstance(self.response, BatchResponseRequestResponseType0):
            response = self.response.to_dict()
        else:
            response = self.response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_id": public_id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if name is not UNSET:
            field_dict["name"] = name
        if errors is not UNSET:
            field_dict["errors"] = errors
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.batch_response_request_errors_type_0 import BatchResponseRequestErrorsType0
        from ..models.batch_response_request_response_type_0 import BatchResponseRequestResponseType0

        d = src_dict.copy()
        public_id = d.pop("public_id")

        _status = d.pop("status", UNSET)
        status: Union[Unset, StatusE80Enum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusE80Enum(_status)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_errors(data: object) -> Union["BatchResponseRequestErrorsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                errors_type_0 = BatchResponseRequestErrorsType0.from_dict(data)

                return errors_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BatchResponseRequestErrorsType0", None, Unset], data)

        errors = _parse_errors(d.pop("errors", UNSET))

        def _parse_response(data: object) -> Union["BatchResponseRequestResponseType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_type_0 = BatchResponseRequestResponseType0.from_dict(data)

                return response_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BatchResponseRequestResponseType0", None, Unset], data)

        response = _parse_response(d.pop("response", UNSET))

        batch_response_request = cls(
            public_id=public_id,
            status=status,
            name=name,
            errors=errors,
            response=response,
        )

        batch_response_request.additional_properties = d
        return batch_response_request

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
