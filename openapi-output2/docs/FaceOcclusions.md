# FaceOcclusions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eye_occluded** | **bool** |  | 
**forehead_occluded** | **bool** |  | 
**mouth_occluded** | **bool** |  | 

## Example

```python
from openapi_client.models.face_occlusions import FaceOcclusions

# TODO update the JSON string below
json = "{}"
# create an instance of FaceOcclusions from a JSON string
face_occlusions_instance = FaceOcclusions.from_json(json)
# print the JSON string representation of the object
print(FaceOcclusions.to_json())

# convert the object into a dict
face_occlusions_dict = face_occlusions_instance.to_dict()
# create an instance of FaceOcclusions from a dict
face_occlusions_form_dict = face_occlusions.from_dict(face_occlusions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


