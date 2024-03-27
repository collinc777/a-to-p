# FaceCompareBoundingBox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top** | **int** |  | 
**left** | **int** |  | 
**height** | **int** |  | 
**width** | **int** |  | 

## Example

```python
from openapi_client.models.face_compare_bounding_box import FaceCompareBoundingBox

# TODO update the JSON string below
json = "{}"
# create an instance of FaceCompareBoundingBox from a JSON string
face_compare_bounding_box_instance = FaceCompareBoundingBox.from_json(json)
# print the JSON string representation of the object
print(FaceCompareBoundingBox.to_json())

# convert the object into a dict
face_compare_bounding_box_dict = face_compare_bounding_box_instance.to_dict()
# create an instance of FaceCompareBoundingBox from a dict
face_compare_bounding_box_form_dict = face_compare_bounding_box.from_dict(face_compare_bounding_box_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


