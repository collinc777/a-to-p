from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FaceLandmarks")


@_attrs_define
class FaceLandmarks:
    """
    Attributes:
        left_eye (Union[Unset, List[int]]):
        left_eye_top (Union[Unset, List[int]]):
        left_eye_right (Union[Unset, List[int]]):
        left_eye_bottom (Union[Unset, List[int]]):
        left_eye_left (Union[Unset, List[int]]):
        right_eye (Union[Unset, List[int]]):
        right_eye_top (Union[Unset, List[int]]):
        right_eye_right (Union[Unset, List[int]]):
        right_eye_bottom (Union[Unset, List[int]]):
        right_eye_left (Union[Unset, List[int]]):
        left_eyebrow_left (Union[Unset, List[int]]):
        left_eyebrow_right (Union[Unset, List[int]]):
        left_eyebrow_top (Union[Unset, List[int]]):
        right_eyebrow_left (Union[Unset, List[int]]):
        right_eyebrow_right (Union[Unset, List[int]]):
        left_pupil (Union[Unset, List[int]]):
        right_pupil (Union[Unset, List[int]]):
        nose_tip (Union[Unset, List[int]]):
        nose_bottom_right (Union[Unset, List[int]]):
        nose_bottom_left (Union[Unset, List[int]]):
        mouth_left (Union[Unset, List[int]]):
        mouth_right (Union[Unset, List[int]]):
        right_eyebrow_top (Union[Unset, List[int]]):
        midpoint_between_eyes (Union[Unset, List[int]]):
        nose_bottom_center (Union[Unset, List[int]]):
        nose_left_alar_out_tip (Union[Unset, List[int]]):
        nose_left_alar_top (Union[Unset, List[int]]):
        nose_right_alar_out_tip (Union[Unset, List[int]]):
        nose_right_alar_top (Union[Unset, List[int]]):
        nose_root_left (Union[Unset, List[int]]):
        nose_root_right (Union[Unset, List[int]]):
        upper_lip (Union[Unset, List[int]]):
        under_lip (Union[Unset, List[int]]):
        under_lip_bottom (Union[Unset, List[int]]):
        under_lip_top (Union[Unset, List[int]]):
        upper_lip_bottom (Union[Unset, List[int]]):
        upper_lip_top (Union[Unset, List[int]]):
        mouth_center (Union[Unset, List[int]]):
        mouth_top (Union[Unset, List[int]]):
        mouth_bottom (Union[Unset, List[int]]):
        left_ear_tragion (Union[Unset, List[int]]):
        right_ear_tragion (Union[Unset, List[int]]):
        forehead_glabella (Union[Unset, List[int]]):
        chin_gnathion (Union[Unset, List[int]]):
        chin_left_gonion (Union[Unset, List[int]]):
        chin_right_gonion (Union[Unset, List[int]]):
        upper_jawline_left (Union[Unset, List[int]]):
        mid_jawline_left (Union[Unset, List[int]]):
        mid_jawline_right (Union[Unset, List[int]]):
        upper_jawline_right (Union[Unset, List[int]]):
        left_cheek_center (Union[Unset, List[int]]):
        right_cheek_center (Union[Unset, List[int]]):
    """

    left_eye: Union[Unset, List[int]] = UNSET
    left_eye_top: Union[Unset, List[int]] = UNSET
    left_eye_right: Union[Unset, List[int]] = UNSET
    left_eye_bottom: Union[Unset, List[int]] = UNSET
    left_eye_left: Union[Unset, List[int]] = UNSET
    right_eye: Union[Unset, List[int]] = UNSET
    right_eye_top: Union[Unset, List[int]] = UNSET
    right_eye_right: Union[Unset, List[int]] = UNSET
    right_eye_bottom: Union[Unset, List[int]] = UNSET
    right_eye_left: Union[Unset, List[int]] = UNSET
    left_eyebrow_left: Union[Unset, List[int]] = UNSET
    left_eyebrow_right: Union[Unset, List[int]] = UNSET
    left_eyebrow_top: Union[Unset, List[int]] = UNSET
    right_eyebrow_left: Union[Unset, List[int]] = UNSET
    right_eyebrow_right: Union[Unset, List[int]] = UNSET
    left_pupil: Union[Unset, List[int]] = UNSET
    right_pupil: Union[Unset, List[int]] = UNSET
    nose_tip: Union[Unset, List[int]] = UNSET
    nose_bottom_right: Union[Unset, List[int]] = UNSET
    nose_bottom_left: Union[Unset, List[int]] = UNSET
    mouth_left: Union[Unset, List[int]] = UNSET
    mouth_right: Union[Unset, List[int]] = UNSET
    right_eyebrow_top: Union[Unset, List[int]] = UNSET
    midpoint_between_eyes: Union[Unset, List[int]] = UNSET
    nose_bottom_center: Union[Unset, List[int]] = UNSET
    nose_left_alar_out_tip: Union[Unset, List[int]] = UNSET
    nose_left_alar_top: Union[Unset, List[int]] = UNSET
    nose_right_alar_out_tip: Union[Unset, List[int]] = UNSET
    nose_right_alar_top: Union[Unset, List[int]] = UNSET
    nose_root_left: Union[Unset, List[int]] = UNSET
    nose_root_right: Union[Unset, List[int]] = UNSET
    upper_lip: Union[Unset, List[int]] = UNSET
    under_lip: Union[Unset, List[int]] = UNSET
    under_lip_bottom: Union[Unset, List[int]] = UNSET
    under_lip_top: Union[Unset, List[int]] = UNSET
    upper_lip_bottom: Union[Unset, List[int]] = UNSET
    upper_lip_top: Union[Unset, List[int]] = UNSET
    mouth_center: Union[Unset, List[int]] = UNSET
    mouth_top: Union[Unset, List[int]] = UNSET
    mouth_bottom: Union[Unset, List[int]] = UNSET
    left_ear_tragion: Union[Unset, List[int]] = UNSET
    right_ear_tragion: Union[Unset, List[int]] = UNSET
    forehead_glabella: Union[Unset, List[int]] = UNSET
    chin_gnathion: Union[Unset, List[int]] = UNSET
    chin_left_gonion: Union[Unset, List[int]] = UNSET
    chin_right_gonion: Union[Unset, List[int]] = UNSET
    upper_jawline_left: Union[Unset, List[int]] = UNSET
    mid_jawline_left: Union[Unset, List[int]] = UNSET
    mid_jawline_right: Union[Unset, List[int]] = UNSET
    upper_jawline_right: Union[Unset, List[int]] = UNSET
    left_cheek_center: Union[Unset, List[int]] = UNSET
    right_cheek_center: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        left_eye: Union[Unset, List[int]] = UNSET
        if not isinstance(self.left_eye, Unset):
            left_eye = self.left_eye

        left_eye_top: Union[Unset, List[int]] = UNSET
        if not isinstance(self.left_eye_top, Unset):
            left_eye_top = self.left_eye_top

        left_eye_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.left_eye_right, Unset):
            left_eye_right = self.left_eye_right

        left_eye_bottom: Union[Unset, List[int]] = UNSET
        if not isinstance(self.left_eye_bottom, Unset):
            left_eye_bottom = self.left_eye_bottom

        left_eye_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.left_eye_left, Unset):
            left_eye_left = self.left_eye_left

        right_eye: Union[Unset, List[int]] = UNSET
        if not isinstance(self.right_eye, Unset):
            right_eye = self.right_eye

        right_eye_top: Union[Unset, List[int]] = UNSET
        if not isinstance(self.right_eye_top, Unset):
            right_eye_top = self.right_eye_top

        right_eye_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.right_eye_right, Unset):
            right_eye_right = self.right_eye_right

        right_eye_bottom: Union[Unset, List[int]] = UNSET
        if not isinstance(self.right_eye_bottom, Unset):
            right_eye_bottom = self.right_eye_bottom

        right_eye_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.right_eye_left, Unset):
            right_eye_left = self.right_eye_left

        left_eyebrow_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.left_eyebrow_left, Unset):
            left_eyebrow_left = self.left_eyebrow_left

        left_eyebrow_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.left_eyebrow_right, Unset):
            left_eyebrow_right = self.left_eyebrow_right

        left_eyebrow_top: Union[Unset, List[int]] = UNSET
        if not isinstance(self.left_eyebrow_top, Unset):
            left_eyebrow_top = self.left_eyebrow_top

        right_eyebrow_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.right_eyebrow_left, Unset):
            right_eyebrow_left = self.right_eyebrow_left

        right_eyebrow_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.right_eyebrow_right, Unset):
            right_eyebrow_right = self.right_eyebrow_right

        left_pupil: Union[Unset, List[int]] = UNSET
        if not isinstance(self.left_pupil, Unset):
            left_pupil = self.left_pupil

        right_pupil: Union[Unset, List[int]] = UNSET
        if not isinstance(self.right_pupil, Unset):
            right_pupil = self.right_pupil

        nose_tip: Union[Unset, List[int]] = UNSET
        if not isinstance(self.nose_tip, Unset):
            nose_tip = self.nose_tip

        nose_bottom_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.nose_bottom_right, Unset):
            nose_bottom_right = self.nose_bottom_right

        nose_bottom_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.nose_bottom_left, Unset):
            nose_bottom_left = self.nose_bottom_left

        mouth_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.mouth_left, Unset):
            mouth_left = self.mouth_left

        mouth_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.mouth_right, Unset):
            mouth_right = self.mouth_right

        right_eyebrow_top: Union[Unset, List[int]] = UNSET
        if not isinstance(self.right_eyebrow_top, Unset):
            right_eyebrow_top = self.right_eyebrow_top

        midpoint_between_eyes: Union[Unset, List[int]] = UNSET
        if not isinstance(self.midpoint_between_eyes, Unset):
            midpoint_between_eyes = self.midpoint_between_eyes

        nose_bottom_center: Union[Unset, List[int]] = UNSET
        if not isinstance(self.nose_bottom_center, Unset):
            nose_bottom_center = self.nose_bottom_center

        nose_left_alar_out_tip: Union[Unset, List[int]] = UNSET
        if not isinstance(self.nose_left_alar_out_tip, Unset):
            nose_left_alar_out_tip = self.nose_left_alar_out_tip

        nose_left_alar_top: Union[Unset, List[int]] = UNSET
        if not isinstance(self.nose_left_alar_top, Unset):
            nose_left_alar_top = self.nose_left_alar_top

        nose_right_alar_out_tip: Union[Unset, List[int]] = UNSET
        if not isinstance(self.nose_right_alar_out_tip, Unset):
            nose_right_alar_out_tip = self.nose_right_alar_out_tip

        nose_right_alar_top: Union[Unset, List[int]] = UNSET
        if not isinstance(self.nose_right_alar_top, Unset):
            nose_right_alar_top = self.nose_right_alar_top

        nose_root_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.nose_root_left, Unset):
            nose_root_left = self.nose_root_left

        nose_root_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.nose_root_right, Unset):
            nose_root_right = self.nose_root_right

        upper_lip: Union[Unset, List[int]] = UNSET
        if not isinstance(self.upper_lip, Unset):
            upper_lip = self.upper_lip

        under_lip: Union[Unset, List[int]] = UNSET
        if not isinstance(self.under_lip, Unset):
            under_lip = self.under_lip

        under_lip_bottom: Union[Unset, List[int]] = UNSET
        if not isinstance(self.under_lip_bottom, Unset):
            under_lip_bottom = self.under_lip_bottom

        under_lip_top: Union[Unset, List[int]] = UNSET
        if not isinstance(self.under_lip_top, Unset):
            under_lip_top = self.under_lip_top

        upper_lip_bottom: Union[Unset, List[int]] = UNSET
        if not isinstance(self.upper_lip_bottom, Unset):
            upper_lip_bottom = self.upper_lip_bottom

        upper_lip_top: Union[Unset, List[int]] = UNSET
        if not isinstance(self.upper_lip_top, Unset):
            upper_lip_top = self.upper_lip_top

        mouth_center: Union[Unset, List[int]] = UNSET
        if not isinstance(self.mouth_center, Unset):
            mouth_center = self.mouth_center

        mouth_top: Union[Unset, List[int]] = UNSET
        if not isinstance(self.mouth_top, Unset):
            mouth_top = self.mouth_top

        mouth_bottom: Union[Unset, List[int]] = UNSET
        if not isinstance(self.mouth_bottom, Unset):
            mouth_bottom = self.mouth_bottom

        left_ear_tragion: Union[Unset, List[int]] = UNSET
        if not isinstance(self.left_ear_tragion, Unset):
            left_ear_tragion = self.left_ear_tragion

        right_ear_tragion: Union[Unset, List[int]] = UNSET
        if not isinstance(self.right_ear_tragion, Unset):
            right_ear_tragion = self.right_ear_tragion

        forehead_glabella: Union[Unset, List[int]] = UNSET
        if not isinstance(self.forehead_glabella, Unset):
            forehead_glabella = self.forehead_glabella

        chin_gnathion: Union[Unset, List[int]] = UNSET
        if not isinstance(self.chin_gnathion, Unset):
            chin_gnathion = self.chin_gnathion

        chin_left_gonion: Union[Unset, List[int]] = UNSET
        if not isinstance(self.chin_left_gonion, Unset):
            chin_left_gonion = self.chin_left_gonion

        chin_right_gonion: Union[Unset, List[int]] = UNSET
        if not isinstance(self.chin_right_gonion, Unset):
            chin_right_gonion = self.chin_right_gonion

        upper_jawline_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.upper_jawline_left, Unset):
            upper_jawline_left = self.upper_jawline_left

        mid_jawline_left: Union[Unset, List[int]] = UNSET
        if not isinstance(self.mid_jawline_left, Unset):
            mid_jawline_left = self.mid_jawline_left

        mid_jawline_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.mid_jawline_right, Unset):
            mid_jawline_right = self.mid_jawline_right

        upper_jawline_right: Union[Unset, List[int]] = UNSET
        if not isinstance(self.upper_jawline_right, Unset):
            upper_jawline_right = self.upper_jawline_right

        left_cheek_center: Union[Unset, List[int]] = UNSET
        if not isinstance(self.left_cheek_center, Unset):
            left_cheek_center = self.left_cheek_center

        right_cheek_center: Union[Unset, List[int]] = UNSET
        if not isinstance(self.right_cheek_center, Unset):
            right_cheek_center = self.right_cheek_center

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if left_eye is not UNSET:
            field_dict["left_eye"] = left_eye
        if left_eye_top is not UNSET:
            field_dict["left_eye_top"] = left_eye_top
        if left_eye_right is not UNSET:
            field_dict["left_eye_right"] = left_eye_right
        if left_eye_bottom is not UNSET:
            field_dict["left_eye_bottom"] = left_eye_bottom
        if left_eye_left is not UNSET:
            field_dict["left_eye_left"] = left_eye_left
        if right_eye is not UNSET:
            field_dict["right_eye"] = right_eye
        if right_eye_top is not UNSET:
            field_dict["right_eye_top"] = right_eye_top
        if right_eye_right is not UNSET:
            field_dict["right_eye_right"] = right_eye_right
        if right_eye_bottom is not UNSET:
            field_dict["right_eye_bottom"] = right_eye_bottom
        if right_eye_left is not UNSET:
            field_dict["right_eye_left"] = right_eye_left
        if left_eyebrow_left is not UNSET:
            field_dict["left_eyebrow_left"] = left_eyebrow_left
        if left_eyebrow_right is not UNSET:
            field_dict["left_eyebrow_right"] = left_eyebrow_right
        if left_eyebrow_top is not UNSET:
            field_dict["left_eyebrow_top"] = left_eyebrow_top
        if right_eyebrow_left is not UNSET:
            field_dict["right_eyebrow_left"] = right_eyebrow_left
        if right_eyebrow_right is not UNSET:
            field_dict["right_eyebrow_right"] = right_eyebrow_right
        if left_pupil is not UNSET:
            field_dict["left_pupil"] = left_pupil
        if right_pupil is not UNSET:
            field_dict["right_pupil"] = right_pupil
        if nose_tip is not UNSET:
            field_dict["nose_tip"] = nose_tip
        if nose_bottom_right is not UNSET:
            field_dict["nose_bottom_right"] = nose_bottom_right
        if nose_bottom_left is not UNSET:
            field_dict["nose_bottom_left"] = nose_bottom_left
        if mouth_left is not UNSET:
            field_dict["mouth_left"] = mouth_left
        if mouth_right is not UNSET:
            field_dict["mouth_right"] = mouth_right
        if right_eyebrow_top is not UNSET:
            field_dict["right_eyebrow_top"] = right_eyebrow_top
        if midpoint_between_eyes is not UNSET:
            field_dict["midpoint_between_eyes"] = midpoint_between_eyes
        if nose_bottom_center is not UNSET:
            field_dict["nose_bottom_center"] = nose_bottom_center
        if nose_left_alar_out_tip is not UNSET:
            field_dict["nose_left_alar_out_tip"] = nose_left_alar_out_tip
        if nose_left_alar_top is not UNSET:
            field_dict["nose_left_alar_top"] = nose_left_alar_top
        if nose_right_alar_out_tip is not UNSET:
            field_dict["nose_right_alar_out_tip"] = nose_right_alar_out_tip
        if nose_right_alar_top is not UNSET:
            field_dict["nose_right_alar_top"] = nose_right_alar_top
        if nose_root_left is not UNSET:
            field_dict["nose_root_left"] = nose_root_left
        if nose_root_right is not UNSET:
            field_dict["nose_root_right"] = nose_root_right
        if upper_lip is not UNSET:
            field_dict["upper_lip"] = upper_lip
        if under_lip is not UNSET:
            field_dict["under_lip"] = under_lip
        if under_lip_bottom is not UNSET:
            field_dict["under_lip_bottom"] = under_lip_bottom
        if under_lip_top is not UNSET:
            field_dict["under_lip_top"] = under_lip_top
        if upper_lip_bottom is not UNSET:
            field_dict["upper_lip_bottom"] = upper_lip_bottom
        if upper_lip_top is not UNSET:
            field_dict["upper_lip_top"] = upper_lip_top
        if mouth_center is not UNSET:
            field_dict["mouth_center"] = mouth_center
        if mouth_top is not UNSET:
            field_dict["mouth_top"] = mouth_top
        if mouth_bottom is not UNSET:
            field_dict["mouth_bottom"] = mouth_bottom
        if left_ear_tragion is not UNSET:
            field_dict["left_ear_tragion"] = left_ear_tragion
        if right_ear_tragion is not UNSET:
            field_dict["right_ear_tragion"] = right_ear_tragion
        if forehead_glabella is not UNSET:
            field_dict["forehead_glabella"] = forehead_glabella
        if chin_gnathion is not UNSET:
            field_dict["chin_gnathion"] = chin_gnathion
        if chin_left_gonion is not UNSET:
            field_dict["chin_left_gonion"] = chin_left_gonion
        if chin_right_gonion is not UNSET:
            field_dict["chin_right_gonion"] = chin_right_gonion
        if upper_jawline_left is not UNSET:
            field_dict["upper_jawline_left"] = upper_jawline_left
        if mid_jawline_left is not UNSET:
            field_dict["mid_jawline_left"] = mid_jawline_left
        if mid_jawline_right is not UNSET:
            field_dict["mid_jawline_right"] = mid_jawline_right
        if upper_jawline_right is not UNSET:
            field_dict["upper_jawline_right"] = upper_jawline_right
        if left_cheek_center is not UNSET:
            field_dict["left_cheek_center"] = left_cheek_center
        if right_cheek_center is not UNSET:
            field_dict["right_cheek_center"] = right_cheek_center

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        left_eye = cast(List[int], d.pop("left_eye", UNSET))

        left_eye_top = cast(List[int], d.pop("left_eye_top", UNSET))

        left_eye_right = cast(List[int], d.pop("left_eye_right", UNSET))

        left_eye_bottom = cast(List[int], d.pop("left_eye_bottom", UNSET))

        left_eye_left = cast(List[int], d.pop("left_eye_left", UNSET))

        right_eye = cast(List[int], d.pop("right_eye", UNSET))

        right_eye_top = cast(List[int], d.pop("right_eye_top", UNSET))

        right_eye_right = cast(List[int], d.pop("right_eye_right", UNSET))

        right_eye_bottom = cast(List[int], d.pop("right_eye_bottom", UNSET))

        right_eye_left = cast(List[int], d.pop("right_eye_left", UNSET))

        left_eyebrow_left = cast(List[int], d.pop("left_eyebrow_left", UNSET))

        left_eyebrow_right = cast(List[int], d.pop("left_eyebrow_right", UNSET))

        left_eyebrow_top = cast(List[int], d.pop("left_eyebrow_top", UNSET))

        right_eyebrow_left = cast(List[int], d.pop("right_eyebrow_left", UNSET))

        right_eyebrow_right = cast(List[int], d.pop("right_eyebrow_right", UNSET))

        left_pupil = cast(List[int], d.pop("left_pupil", UNSET))

        right_pupil = cast(List[int], d.pop("right_pupil", UNSET))

        nose_tip = cast(List[int], d.pop("nose_tip", UNSET))

        nose_bottom_right = cast(List[int], d.pop("nose_bottom_right", UNSET))

        nose_bottom_left = cast(List[int], d.pop("nose_bottom_left", UNSET))

        mouth_left = cast(List[int], d.pop("mouth_left", UNSET))

        mouth_right = cast(List[int], d.pop("mouth_right", UNSET))

        right_eyebrow_top = cast(List[int], d.pop("right_eyebrow_top", UNSET))

        midpoint_between_eyes = cast(List[int], d.pop("midpoint_between_eyes", UNSET))

        nose_bottom_center = cast(List[int], d.pop("nose_bottom_center", UNSET))

        nose_left_alar_out_tip = cast(List[int], d.pop("nose_left_alar_out_tip", UNSET))

        nose_left_alar_top = cast(List[int], d.pop("nose_left_alar_top", UNSET))

        nose_right_alar_out_tip = cast(List[int], d.pop("nose_right_alar_out_tip", UNSET))

        nose_right_alar_top = cast(List[int], d.pop("nose_right_alar_top", UNSET))

        nose_root_left = cast(List[int], d.pop("nose_root_left", UNSET))

        nose_root_right = cast(List[int], d.pop("nose_root_right", UNSET))

        upper_lip = cast(List[int], d.pop("upper_lip", UNSET))

        under_lip = cast(List[int], d.pop("under_lip", UNSET))

        under_lip_bottom = cast(List[int], d.pop("under_lip_bottom", UNSET))

        under_lip_top = cast(List[int], d.pop("under_lip_top", UNSET))

        upper_lip_bottom = cast(List[int], d.pop("upper_lip_bottom", UNSET))

        upper_lip_top = cast(List[int], d.pop("upper_lip_top", UNSET))

        mouth_center = cast(List[int], d.pop("mouth_center", UNSET))

        mouth_top = cast(List[int], d.pop("mouth_top", UNSET))

        mouth_bottom = cast(List[int], d.pop("mouth_bottom", UNSET))

        left_ear_tragion = cast(List[int], d.pop("left_ear_tragion", UNSET))

        right_ear_tragion = cast(List[int], d.pop("right_ear_tragion", UNSET))

        forehead_glabella = cast(List[int], d.pop("forehead_glabella", UNSET))

        chin_gnathion = cast(List[int], d.pop("chin_gnathion", UNSET))

        chin_left_gonion = cast(List[int], d.pop("chin_left_gonion", UNSET))

        chin_right_gonion = cast(List[int], d.pop("chin_right_gonion", UNSET))

        upper_jawline_left = cast(List[int], d.pop("upper_jawline_left", UNSET))

        mid_jawline_left = cast(List[int], d.pop("mid_jawline_left", UNSET))

        mid_jawline_right = cast(List[int], d.pop("mid_jawline_right", UNSET))

        upper_jawline_right = cast(List[int], d.pop("upper_jawline_right", UNSET))

        left_cheek_center = cast(List[int], d.pop("left_cheek_center", UNSET))

        right_cheek_center = cast(List[int], d.pop("right_cheek_center", UNSET))

        face_landmarks = cls(
            left_eye=left_eye,
            left_eye_top=left_eye_top,
            left_eye_right=left_eye_right,
            left_eye_bottom=left_eye_bottom,
            left_eye_left=left_eye_left,
            right_eye=right_eye,
            right_eye_top=right_eye_top,
            right_eye_right=right_eye_right,
            right_eye_bottom=right_eye_bottom,
            right_eye_left=right_eye_left,
            left_eyebrow_left=left_eyebrow_left,
            left_eyebrow_right=left_eyebrow_right,
            left_eyebrow_top=left_eyebrow_top,
            right_eyebrow_left=right_eyebrow_left,
            right_eyebrow_right=right_eyebrow_right,
            left_pupil=left_pupil,
            right_pupil=right_pupil,
            nose_tip=nose_tip,
            nose_bottom_right=nose_bottom_right,
            nose_bottom_left=nose_bottom_left,
            mouth_left=mouth_left,
            mouth_right=mouth_right,
            right_eyebrow_top=right_eyebrow_top,
            midpoint_between_eyes=midpoint_between_eyes,
            nose_bottom_center=nose_bottom_center,
            nose_left_alar_out_tip=nose_left_alar_out_tip,
            nose_left_alar_top=nose_left_alar_top,
            nose_right_alar_out_tip=nose_right_alar_out_tip,
            nose_right_alar_top=nose_right_alar_top,
            nose_root_left=nose_root_left,
            nose_root_right=nose_root_right,
            upper_lip=upper_lip,
            under_lip=under_lip,
            under_lip_bottom=under_lip_bottom,
            under_lip_top=under_lip_top,
            upper_lip_bottom=upper_lip_bottom,
            upper_lip_top=upper_lip_top,
            mouth_center=mouth_center,
            mouth_top=mouth_top,
            mouth_bottom=mouth_bottom,
            left_ear_tragion=left_ear_tragion,
            right_ear_tragion=right_ear_tragion,
            forehead_glabella=forehead_glabella,
            chin_gnathion=chin_gnathion,
            chin_left_gonion=chin_left_gonion,
            chin_right_gonion=chin_right_gonion,
            upper_jawline_left=upper_jawline_left,
            mid_jawline_left=mid_jawline_left,
            mid_jawline_right=mid_jawline_right,
            upper_jawline_right=upper_jawline_right,
            left_cheek_center=left_cheek_center,
            right_cheek_center=right_cheek_center,
        )

        face_landmarks.additional_properties = d
        return face_landmarks

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
