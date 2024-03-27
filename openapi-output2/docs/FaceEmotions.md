# FaceEmotions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**joy** | **int** |  | 
**sorrow** | **int** |  | 
**anger** | **int** |  | 
**surprise** | **int** |  | 
**disgust** | **int** |  | 
**fear** | **int** |  | 
**confusion** | **int** |  | 
**calm** | **int** |  | 
**unknown** | **int** |  | 
**neutral** | **int** |  | 
**contempt** | **int** |  | 

## Example

```python
from openapi_client.models.face_emotions import FaceEmotions

# TODO update the JSON string below
json = "{}"
# create an instance of FaceEmotions from a JSON string
face_emotions_instance = FaceEmotions.from_json(json)
# print the JSON string representation of the object
print(FaceEmotions.to_json())

# convert the object into a dict
face_emotions_dict = face_emotions_instance.to_dict()
# create an instance of FaceEmotions from a dict
face_emotions_form_dict = face_emotions.from_dict(face_emotions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


