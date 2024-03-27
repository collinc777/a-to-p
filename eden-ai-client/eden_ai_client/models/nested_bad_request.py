from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.field_error import FieldError


T = TypeVar("T", bound="NestedBadRequest")


@_attrs_define
class NestedBadRequest:
    """
    Attributes:
        type (str):
        message (FieldError):
    """

    type: str
    message: "FieldError"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        message = self.message.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.field_error import FieldError

        d = src_dict.copy()
        type = d.pop("type")

        message = FieldError.from_dict(d.pop("message"))

        nested_bad_request = cls(
            type=type,
            message=message,
        )

        nested_bad_request.additional_properties = d
        return nested_bad_request

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
