# FaceMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **int** |  | 
**bounding_box** | [**FaceCompareBoundingBox**](FaceCompareBoundingBox.md) |  | 

## Example

```python
from openapi_client.models.face_match import FaceMatch

# TODO update the JSON string below
json = "{}"
# create an instance of FaceMatch from a JSON string
face_match_instance = FaceMatch.from_json(json)
# print the JSON string representation of the object
print(FaceMatch.to_json())

# convert the object into a dict
face_match_dict = face_match_instance.to_dict()
# create an instance of FaceMatch from a dict
face_match_form_dict = face_match.from_dict(face_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


