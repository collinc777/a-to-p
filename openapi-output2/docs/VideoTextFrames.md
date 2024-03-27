# VideoTextFrames


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **int** |  | 
**timestamp** | **int** |  | 
**bounding_box** | [**VideoTextBoundingBox**](VideoTextBoundingBox.md) |  | 

## Example

```python
from openapi_client.models.video_text_frames import VideoTextFrames

# TODO update the JSON string below
json = "{}"
# create an instance of VideoTextFrames from a JSON string
video_text_frames_instance = VideoTextFrames.from_json(json)
# print the JSON string representation of the object
print(VideoTextFrames.to_json())

# convert the object into a dict
video_text_frames_dict = video_text_frames_instance.to_dict()
# create an instance of VideoTextFrames from a dict
video_text_frames_form_dict = video_text_frames.from_dict(video_text_frames_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


