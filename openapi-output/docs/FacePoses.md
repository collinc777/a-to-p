# FacePoses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pitch** | **int** |  | 
**roll** | **int** |  | 
**yaw** | **int** |  | 

## Example

```python
from openapi_client.models.face_poses import FacePoses

# TODO update the JSON string below
json = "{}"
# create an instance of FacePoses from a JSON string
face_poses_instance = FacePoses.from_json(json)
# print the JSON string representation of the object
print(FacePoses.to_json())

# convert the object into a dict
face_poses_dict = face_poses_instance.to_dict()
# create an instance of FacePoses from a dict
face_poses_form_dict = face_poses.from_dict(face_poses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


