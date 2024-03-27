# FaceBoundingBox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x_min** | **int** |  | 
**x_max** | **int** |  | 
**y_min** | **int** |  | 
**y_max** | **int** |  | 

## Example

```python
from openapi_client.models.face_bounding_box import FaceBoundingBox

# TODO update the JSON string below
json = "{}"
# create an instance of FaceBoundingBox from a JSON string
face_bounding_box_instance = FaceBoundingBox.from_json(json)
# print the JSON string representation of the object
print(FaceBoundingBox.to_json())

# convert the object into a dict
face_bounding_box_dict = face_bounding_box_instance.to_dict()
# create an instance of FaceBoundingBox from a dict
face_bounding_box_form_dict = face_bounding_box.from_dict(face_bounding_box_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


