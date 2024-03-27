# VideoText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**frames** | [**List[VideoTextFrames]**](VideoTextFrames.md) |  | [optional] 

## Example

```python
from openapi_client.models.video_text import VideoText

# TODO update the JSON string below
json = "{}"
# create an instance of VideoText from a JSON string
video_text_instance = VideoText.from_json(json)
# print the JSON string representation of the object
print(VideoText.to_json())

# convert the object into a dict
video_text_dict = video_text_instance.to_dict()
# create an instance of VideoText from a dict
video_text_form_dict = video_text.from_dict(video_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


