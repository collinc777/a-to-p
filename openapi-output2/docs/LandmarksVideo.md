# LandmarksVideo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eye_left** | **List[int]** |  | [optional] 
**eye_right** | **List[int]** |  | [optional] 
**nose** | **List[int]** |  | [optional] 
**mouth_left** | **List[int]** |  | [optional] 
**mouth_right** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.landmarks_video import LandmarksVideo

# TODO update the JSON string below
json = "{}"
# create an instance of LandmarksVideo from a JSON string
landmarks_video_instance = LandmarksVideo.from_json(json)
# print the JSON string representation of the object
print(LandmarksVideo.to_json())

# convert the object into a dict
landmarks_video_dict = landmarks_video_instance.to_dict()
# create an instance of LandmarksVideo from a dict
landmarks_video_form_dict = landmarks_video.from_dict(landmarks_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


