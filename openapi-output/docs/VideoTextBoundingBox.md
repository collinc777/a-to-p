# VideoTextBoundingBox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top** | **int** |  | 
**left** | **int** |  | 
**height** | **int** |  | 
**width** | **int** |  | 

## Example

```python
from openapi_client.models.video_text_bounding_box import VideoTextBoundingBox

# TODO update the JSON string below
json = "{}"
# create an instance of VideoTextBoundingBox from a JSON string
video_text_bounding_box_instance = VideoTextBoundingBox.from_json(json)
# print the JSON string representation of the object
print(VideoTextBoundingBox.to_json())

# convert the object into a dict
video_text_bounding_box_dict = video_text_bounding_box_instance.to_dict()
# create an instance of VideoTextBoundingBox from a dict
video_text_bounding_box_form_dict = video_text_bounding_box.from_dict(video_text_bounding_box_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


