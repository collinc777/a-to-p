# FaceAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headwear** | **int** |  | 
**frontal_gaze** | **int** |  | 
**eyes_visible** | **int** |  | 
**glasses** | **int** |  | 
**mouth_open** | **int** |  | 
**smiling** | **int** |  | 
**brightness** | **int** |  | 
**sharpness** | **int** |  | 
**pose** | [**VideoFacePoses**](VideoFacePoses.md) |  | 

## Example

```python
from openapi_client.models.face_attributes import FaceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of FaceAttributes from a JSON string
face_attributes_instance = FaceAttributes.from_json(json)
# print the JSON string representation of the object
print(FaceAttributes.to_json())

# convert the object into a dict
face_attributes_dict = face_attributes_instance.to_dict()
# create an instance of FaceAttributes from a dict
face_attributes_form_dict = face_attributes.from_dict(face_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


