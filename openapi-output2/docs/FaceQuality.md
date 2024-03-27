# FaceQuality


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**noise** | **int** |  | 
**exposure** | **int** |  | 
**blur** | **int** |  | 
**brightness** | **int** |  | 
**sharpness** | **int** |  | 

## Example

```python
from openapi_client.models.face_quality import FaceQuality

# TODO update the JSON string below
json = "{}"
# create an instance of FaceQuality from a JSON string
face_quality_instance = FaceQuality.from_json(json)
# print the JSON string representation of the object
print(FaceQuality.to_json())

# convert the object into a dict
face_quality_dict = face_quality_instance.to_dict()
# create an instance of FaceQuality from a dict
face_quality_form_dict = face_quality.from_dict(face_quality_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


