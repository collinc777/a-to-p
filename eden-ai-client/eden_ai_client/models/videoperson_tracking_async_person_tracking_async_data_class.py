from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.final_status_enum import FinalStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.video_tracking_person import VideoTrackingPerson
    from ..models.videoperson_tracking_async_person_tracking_async_data_class_error import (
        VideopersonTrackingAsyncPersonTrackingAsyncDataClassError,
    )


T = TypeVar("T", bound="VideopersonTrackingAsyncPersonTrackingAsyncDataClass")


@_attrs_define
class VideopersonTrackingAsyncPersonTrackingAsyncDataClass:
    """
    Attributes:
        id (str):
        final_status (FinalStatusEnum):
        persons (Union[Unset, List['VideoTrackingPerson']]):
        original_response (Union[Unset, Any]): original response sent by the provider, hidden by default, show it by
            passing the `show_original_response` field to `true` in your request
        error (Union[Unset, VideopersonTrackingAsyncPersonTrackingAsyncDataClassError]):
    """

    id: str
    final_status: FinalStatusEnum
    persons: Union[Unset, List["VideoTrackingPerson"]] = UNSET
    original_response: Union[Unset, Any] = UNSET
    error: Union[Unset, "VideopersonTrackingAsyncPersonTrackingAsyncDataClassError"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        final_status = self.final_status.value

        persons: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.persons, Unset):
            persons = []
            for persons_item_data in self.persons:
                persons_item = persons_item_data.to_dict()
                persons.append(persons_item)

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
        if persons is not UNSET:
            field_dict["persons"] = persons
        if original_response is not UNSET:
            field_dict["original_response"] = original_response
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.video_tracking_person import VideoTrackingPerson
        from ..models.videoperson_tracking_async_person_tracking_async_data_class_error import (
            VideopersonTrackingAsyncPersonTrackingAsyncDataClassError,
        )

        d = src_dict.copy()
        id = d.pop("id")

        final_status = FinalStatusEnum(d.pop("final_status"))

        persons = []
        _persons = d.pop("persons", UNSET)
        for persons_item_data in _persons or []:
            persons_item = VideoTrackingPerson.from_dict(persons_item_data)

            persons.append(persons_item)

        original_response = d.pop("original_response", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, VideopersonTrackingAsyncPersonTrackingAsyncDataClassError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = VideopersonTrackingAsyncPersonTrackingAsyncDataClassError.from_dict(_error)

        videoperson_tracking_async_person_tracking_async_data_class = cls(
            id=id,
            final_status=final_status,
            persons=persons,
            original_response=original_response,
            error=error,
        )

        videoperson_tracking_async_person_tracking_async_data_class.additional_properties = d
        return videoperson_tracking_async_person_tracking_async_data_class

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
