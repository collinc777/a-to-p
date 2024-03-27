# FaceHairColor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | 
**confidence** | **int** |  | 

## Example

```python
from openapi_client.models.face_hair_color import FaceHairColor

# TODO update the JSON string below
json = "{}"
# create an instance of FaceHairColor from a JSON string
face_hair_color_instance = FaceHairColor.from_json(json)
# print the JSON string representation of the object
print(FaceHairColor.to_json())

# convert the object into a dict
face_hair_color_dict = face_hair_color_instance.to_dict()
# create an instance of FaceHairColor from a dict
face_hair_color_form_dict = face_hair_color.from_dict(face_hair_color_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


