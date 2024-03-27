from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LandmarksVideo")


@_attrs_define
class LandmarksVideo:
    """
    Attributes:
        eye_left (Union[Unset, List[int]]):
        eye_right (Union[Unset, List[int]]):
        nose (Union[Unset, List[int]]):
        mouth_left (Union[Unset, List[int]]):
        mouth_right (Union[Unset, List[int]]):
    """

    eye_left: Union[Unset, List[int]] = UNSET
    eye_right: Union[Unset, List[int]] = UNSET
    nose: Union[Unset, List[int]] = UNSET
    mouth_left: Union[Unset, List[int]] = UNSET
    mouth_right: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        eye_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.eye_left, Unset):
            eye_left = self.eye_left

        eye_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.eye_right, Unset):
            eye_right = self.eye_right

        nose: Union[Unset, List[int]] = UNSET
        if not isinstance(self.nose, Unset):
            nose = self.nose

        mouth_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.mouth_left, Unset):
            mouth_left = self.mouth_left

        mouth_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.mouth_right, Unset):
            mouth_right = self.mouth_right

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eye_left is not UNSET:
            field_dict["eye_left"] = eye_left
        if eye_right is not UNSET:
            field_dict["eye_right"] = eye_right
        if nose is not UNSET:
            field_dict["nose"] = nose
        if mouth_left is not UNSET:
            field_dict["mouth_left"] = mouth_left
        if mouth_right is not UNSET:
            field_dict["mouth_right"] = mouth_right

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        eye_left = cast(List[int], d.pop("eye_left", UNSET))

        eye_right = cast(List[int], d.pop("eye_right", UNSET))

        nose = cast(List[int], d.pop("nose", UNSET))

        mouth_left = cast(List[int], d.pop("mouth_left", UNSET))

        mouth_right = cast(List[int], d.pop("mouth_right", UNSET))

        landmarks_video = cls(
            eye_left=eye_left,
            eye_right=eye_right,
            nose=nose,
            mouth_left=mouth_left,
            mouth_right=mouth_right,
        )

        landmarks_video.additional_properties = d
        return landmarks_video

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
