# PersonLandmarks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eye_left** | **List[int]** |  | [optional] 
**eye_right** | **List[int]** |  | [optional] 
**nose** | **List[int]** |  | [optional] 
**ear_left** | **List[int]** |  | [optional] 
**ear_right** | **List[int]** |  | [optional] 
**shoulder_left** | **List[int]** |  | [optional] 
**shoulder_right** | **List[int]** |  | [optional] 
**elbow_left** | **List[int]** |  | [optional] 
**elbow_right** | **List[int]** |  | [optional] 
**wrist_left** | **List[int]** |  | [optional] 
**wrist_right** | **List[int]** |  | [optional] 
**hip_left** | **List[int]** |  | [optional] 
**hip_right** | **List[int]** |  | [optional] 
**knee_left** | **List[int]** |  | [optional] 
**knee_right** | **List[int]** |  | [optional] 
**ankle_left** | **List[int]** |  | [optional] 
**ankle_right** | **List[int]** |  | [optional] 
**mouth_left** | **List[int]** |  | [optional] 
**mouth_right** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.person_landmarks import PersonLandmarks

# TODO update the JSON string below
json = "{}"
# create an instance of PersonLandmarks from a JSON string
person_landmarks_instance = PersonLandmarks.from_json(json)
# print the JSON string representation of the object
print(PersonLandmarks.to_json())

# convert the object into a dict
person_landmarks_dict = person_landmarks_instance.to_dict()
# create an instance of PersonLandmarks from a dict
person_landmarks_form_dict = person_landmarks.from_dict(person_landmarks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


