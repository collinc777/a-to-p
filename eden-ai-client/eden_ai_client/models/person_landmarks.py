from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonLandmarks")


@_attrs_define
class PersonLandmarks:
    """
    Attributes:
        eye_left (Union[Unset, List[int]]):
        eye_right (Union[Unset, List[int]]):
        nose (Union[Unset, List[int]]):
        ear_left (Union[Unset, List[int]]):
        ear_right (Union[Unset, List[int]]):
        shoulder_left (Union[Unset, List[int]]):
        shoulder_right (Union[Unset, List[int]]):
        elbow_left (Union[Unset, List[int]]):
        elbow_right (Union[Unset, List[int]]):
        wrist_left (Union[Unset, List[int]]):
        wrist_right (Union[Unset, List[int]]):
        hip_left (Union[Unset, List[int]]):
        hip_right (Union[Unset, List[int]]):
        knee_left (Union[Unset, List[int]]):
        knee_right (Union[Unset, List[int]]):
        ankle_left (Union[Unset, List[int]]):
        ankle_right (Union[Unset, List[int]]):
        mouth_left (Union[Unset, List[int]]):
        mouth_right (Union[Unset, List[int]]):
    """

    eye_left: Union[Unset, List[int]] = UNSET
    eye_right: Union[Unset, List[int]] = UNSET
    nose: Union[Unset, List[int]] = UNSET
    ear_left: Union[Unset, List[int]] = UNSET
    ear_right: Union[Unset, List[int]] = UNSET
    shoulder_left: Union[Unset, List[int]] = UNSET
    shoulder_right: Union[Unset, List[int]] = UNSET
    elbow_left: Union[Unset, List[int]] = UNSET
    elbow_right: Union[Unset, List[int]] = UNSET
    wrist_left: Union[Unset, List[int]] = UNSET
    wrist_right: Union[Unset, List[int]] = UNSET
    hip_left: Union[Unset, List[int]] = UNSET
    hip_right: Union[Unset, List[int]] = UNSET
    knee_left: Union[Unset, List[int]] = UNSET
    knee_right: Union[Unset, List[int]] = UNSET
    ankle_left: Union[Unset, List[int]] = UNSET
    ankle_right: Union[Unset, List[int]] = UNSET
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

        ear_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.ear_left, Unset):
            ear_left = self.ear_left

        ear_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.ear_right, Unset):
            ear_right = self.ear_right

        shoulder_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.shoulder_left, Unset):
            shoulder_left = self.shoulder_left

        shoulder_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.shoulder_right, Unset):
            shoulder_right = self.shoulder_right

        elbow_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.elbow_left, Unset):
            elbow_left = self.elbow_left

        elbow_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.elbow_right, Unset):
            elbow_right = self.elbow_right

        wrist_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.wrist_left, Unset):
            wrist_left = self.wrist_left

        wrist_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.wrist_right, Unset):
            wrist_right = self.wrist_right

        hip_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.hip_left, Unset):
            hip_left = self.hip_left

        hip_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.hip_right, Unset):
            hip_right = self.hip_right

        knee_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.knee_left, Unset):
            knee_left = self.knee_left

        knee_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.knee_right, Unset):
            knee_right = self.knee_right

        ankle_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.ankle_left, Unset):
            ankle_left = self.ankle_left

        ankle_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.ankle_right, Unset):
            ankle_right = self.ankle_right

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
        if ear_left is not UNSET:
            field_dict["ear_left"] = ear_left
        if ear_right is not UNSET:
            field_dict["ear_right"] = ear_right
        if shoulder_left is not UNSET:
            field_dict["shoulder_left"] = shoulder_left
        if shoulder_right is not UNSET:
            field_dict["shoulder_right"] = shoulder_right
        if elbow_left is not UNSET:
            field_dict["elbow_left"] = elbow_left
        if elbow_right is not UNSET:
            field_dict["elbow_right"] = elbow_right
        if wrist_left is not UNSET:
            field_dict["wrist_left"] = wrist_left
        if wrist_right is not UNSET:
            field_dict["wrist_right"] = wrist_right
        if hip_left is not UNSET:
            field_dict["hip_left"] = hip_left
        if hip_right is not UNSET:
            field_dict["hip_right"] = hip_right
        if knee_left is not UNSET:
            field_dict["knee_left"] = knee_left
        if knee_right is not UNSET:
            field_dict["knee_right"] = knee_right
        if ankle_left is not UNSET:
            field_dict["ankle_left"] = ankle_left
        if ankle_right is not UNSET:
            field_dict["ankle_right"] = ankle_right
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

        ear_left = cast(List[int], d.pop("ear_left", UNSET))

        ear_right = cast(List[int], d.pop("ear_right", UNSET))

        shoulder_left = cast(List[int], d.pop("shoulder_left", UNSET))

        shoulder_right = cast(List[int], d.pop("shoulder_right", UNSET))

        elbow_left = cast(List[int], d.pop("elbow_left", UNSET))

        elbow_right = cast(List[int], d.pop("elbow_right", UNSET))

        wrist_left = cast(List[int], d.pop("wrist_left", UNSET))

        wrist_right = cast(List[int], d.pop("wrist_right", UNSET))

        hip_left = cast(List[int], d.pop("hip_left", UNSET))

        hip_right = cast(List[int], d.pop("hip_right", UNSET))

        knee_left = cast(List[int], d.pop("knee_left", UNSET))

        knee_right = cast(List[int], d.pop("knee_right", UNSET))

        ankle_left = cast(List[int], d.pop("ankle_left", UNSET))

        ankle_right = cast(List[int], d.pop("ankle_right", UNSET))

        mouth_left = cast(List[int], d.pop("mouth_left", UNSET))

        mouth_right = cast(List[int], d.pop("mouth_right", UNSET))

        person_landmarks = cls(
            eye_left=eye_left,
            eye_right=eye_right,
            nose=nose,
            ear_left=ear_left,
            ear_right=ear_right,
            shoulder_left=shoulder_left,
            shoulder_right=shoulder_right,
            elbow_left=elbow_left,
            elbow_right=elbow_right,
            wrist_left=wrist_left,
            wrist_right=wrist_right,
            hip_left=hip_left,
            hip_right=hip_right,
            knee_left=knee_left,
            knee_right=knee_right,
            ankle_left=ankle_left,
            ankle_right=ankle_right,
            mouth_left=mouth_left,
            mouth_right=mouth_right,
        )

        person_landmarks.additional_properties = d
        return person_landmarks

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
