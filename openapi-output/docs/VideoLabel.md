# VideoLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**confidence** | **int** |  | 
**timestamp** | [**List[VideoLabelTimeStamp]**](VideoLabelTimeStamp.md) |  | [optional] 
**category** | **List[str]** |  | [optional] 
**bounding_box** | [**List[VideoLabelBoundingBox]**](VideoLabelBoundingBox.md) |  | [optional] 

## Example

```python
from openapi_client.models.video_label import VideoLabel

# TODO update the JSON string below
json = "{}"
# create an instance of VideoLabel from a JSON string
video_label_instance = VideoLabel.from_json(json)
# print the JSON string representation of the object
print(VideoLabel.to_json())

# convert the object into a dict
video_label_dict = video_label_instance.to_dict()
# create an instance of VideoLabel from a dict
video_label_form_dict = video_label.from_dict(video_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


