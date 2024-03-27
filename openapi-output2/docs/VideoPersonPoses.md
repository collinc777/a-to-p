# VideoPersonPoses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pitch** | **int** |  | 
**roll** | **int** |  | 
**yaw** | **int** |  | 

## Example

```python
from openapi_client.models.video_person_poses import VideoPersonPoses

# TODO update the JSON string below
json = "{}"
# create an instance of VideoPersonPoses from a JSON string
video_person_poses_instance = VideoPersonPoses.from_json(json)
# print the JSON string representation of the object
print(VideoPersonPoses.to_json())

# convert the object into a dict
video_person_poses_dict = video_person_poses_instance.to_dict()
# create an instance of VideoPersonPoses from a dict
video_person_poses_form_dict = video_person_poses.from_dict(video_person_poses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


