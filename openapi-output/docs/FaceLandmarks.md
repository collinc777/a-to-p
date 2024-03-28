# FaceLandmarks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_eye** | **List[int]** |  | [optional] 
**left_eye_top** | **List[int]** |  | [optional] 
**left_eye_right** | **List[int]** |  | [optional] 
**left_eye_bottom** | **List[int]** |  | [optional] 
**left_eye_left** | **List[int]** |  | [optional] 
**right_eye** | **List[int]** |  | [optional] 
**right_eye_top** | **List[int]** |  | [optional] 
**right_eye_right** | **List[int]** |  | [optional] 
**right_eye_bottom** | **List[int]** |  | [optional] 
**right_eye_left** | **List[int]** |  | [optional] 
**left_eyebrow_left** | **List[int]** |  | [optional] 
**left_eyebrow_right** | **List[int]** |  | [optional] 
**left_eyebrow_top** | **List[int]** |  | [optional] 
**right_eyebrow_left** | **List[int]** |  | [optional] 
**right_eyebrow_right** | **List[int]** |  | [optional] 
**left_pupil** | **List[int]** |  | [optional] 
**right_pupil** | **List[int]** |  | [optional] 
**nose_tip** | **List[int]** |  | [optional] 
**nose_bottom_right** | **List[int]** |  | [optional] 
**nose_bottom_left** | **List[int]** |  | [optional] 
**mouth_left** | **List[int]** |  | [optional] 
**mouth_right** | **List[int]** |  | [optional] 
**right_eyebrow_top** | **List[int]** |  | [optional] 
**midpoint_between_eyes** | **List[int]** |  | [optional] 
**nose_bottom_center** | **List[int]** |  | [optional] 
**nose_left_alar_out_tip** | **List[int]** |  | [optional] 
**nose_left_alar_top** | **List[int]** |  | [optional] 
**nose_right_alar_out_tip** | **List[int]** |  | [optional] 
**nose_right_alar_top** | **List[int]** |  | [optional] 
**nose_root_left** | **List[int]** |  | [optional] 
**nose_root_right** | **List[int]** |  | [optional] 
**upper_lip** | **List[int]** |  | [optional] 
**under_lip** | **List[int]** |  | [optional] 
**under_lip_bottom** | **List[int]** |  | [optional] 
**under_lip_top** | **List[int]** |  | [optional] 
**upper_lip_bottom** | **List[int]** |  | [optional] 
**upper_lip_top** | **List[int]** |  | [optional] 
**mouth_center** | **List[int]** |  | [optional] 
**mouth_top** | **List[int]** |  | [optional] 
**mouth_bottom** | **List[int]** |  | [optional] 
**left_ear_tragion** | **List[int]** |  | [optional] 
**right_ear_tragion** | **List[int]** |  | [optional] 
**forehead_glabella** | **List[int]** |  | [optional] 
**chin_gnathion** | **List[int]** |  | [optional] 
**chin_left_gonion** | **List[int]** |  | [optional] 
**chin_right_gonion** | **List[int]** |  | [optional] 
**upper_jawline_left** | **List[int]** |  | [optional] 
**mid_jawline_left** | **List[int]** |  | [optional] 
**mid_jawline_right** | **List[int]** |  | [optional] 
**upper_jawline_right** | **List[int]** |  | [optional] 
**left_cheek_center** | **List[int]** |  | [optional] 
**right_cheek_center** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.face_landmarks import FaceLandmarks

# TODO update the JSON string below
json = "{}"
# create an instance of FaceLandmarks from a JSON string
face_landmarks_instance = FaceLandmarks.from_json(json)
# print the JSON string representation of the object
print(FaceLandmarks.to_json())

# convert the object into a dict
face_landmarks_dict = face_landmarks_instance.to_dict()
# create an instance of FaceLandmarks from a dict
face_landmarks_form_dict = face_landmarks.from_dict(face_landmarks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


