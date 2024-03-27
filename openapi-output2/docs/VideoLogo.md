# VideoLogo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** |  | 
**bounding_box** | [**VideoLogoBoundingBox**](VideoLogoBoundingBox.md) |  | 
**confidence** | **int** |  | 

## Example

```python
from openapi_client.models.video_logo import VideoLogo

# TODO update the JSON string below
json = "{}"
# create an instance of VideoLogo from a JSON string
video_logo_instance = VideoLogo.from_json(json)
# print the JSON string representation of the object
print(VideoLogo.to_json())

# convert the object into a dict
video_logo_dict = video_logo_instance.to_dict()
# create an instance of VideoLogo from a dict
video_logo_form_dict = video_logo.from_dict(video_logo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


