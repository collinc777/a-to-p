# FaceAccessories


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sunglasses** | **int** |  | 
**reading_glasses** | **int** |  | 
**swimming_goggles** | **int** |  | 
**face_mask** | **int** |  | 
**eyeglasses** | **int** |  | 
**headwear** | **int** |  | 

## Example

```python
from openapi_client.models.face_accessories import FaceAccessories

# TODO update the JSON string below
json = "{}"
# create an instance of FaceAccessories from a JSON string
face_accessories_instance = FaceAccessories.from_json(json)
# print the JSON string representation of the object
print(FaceAccessories.to_json())

# convert the object into a dict
face_accessories_dict = face_accessories_instance.to_dict()
# create an instance of FaceAccessories from a dict
face_accessories_form_dict = face_accessories.from_dict(face_accessories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


