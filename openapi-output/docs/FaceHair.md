# FaceHair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hair_color** | [**List[FaceHairColor]**](FaceHairColor.md) |  | [optional] 
**bald** | **int** |  | 
**invisible** | **bool** |  | 

## Example

```python
from openapi_client.models.face_hair import FaceHair

# TODO update the JSON string below
json = "{}"
# create an instance of FaceHair from a JSON string
face_hair_instance = FaceHair.from_json(json)
# print the JSON string representation of the object
print(FaceHair.to_json())

# convert the object into a dict
face_hair_dict = face_hair_instance.to_dict()
# create an instance of FaceHair from a dict
face_hair_form_dict = face_hair.from_dict(face_hair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


