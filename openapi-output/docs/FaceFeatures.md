# FaceFeatures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eyes_open** | **int** |  | 
**smile** | **int** |  | 
**mouth_open** | **int** |  | 

## Example

```python
from openapi_client.models.face_features import FaceFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of FaceFeatures from a JSON string
face_features_instance = FaceFeatures.from_json(json)
# print the JSON string representation of the object
print(FaceFeatures.to_json())

# convert the object into a dict
face_features_dict = face_features_instance.to_dict()
# create an instance of FaceFeatures from a dict
face_features_form_dict = face_features.from_dict(face_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


