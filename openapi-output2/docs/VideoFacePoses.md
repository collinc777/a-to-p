# VideoFacePoses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pitch** | **int** |  | 
**roll** | **int** |  | 
**yawn** | **int** |  | 

## Example

```python
from openapi_client.models.video_face_poses import VideoFacePoses

# TODO update the JSON string below
json = "{}"
# create an instance of VideoFacePoses from a JSON string
video_face_poses_instance = VideoFacePoses.from_json(json)
# print the JSON string representation of the object
print(VideoFacePoses.to_json())

# convert the object into a dict
video_face_poses_dict = video_face_poses_instance.to_dict()
# create an instance of VideoFacePoses from a dict
video_face_poses_form_dict = video_face_poses.from_dict(video_face_poses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


