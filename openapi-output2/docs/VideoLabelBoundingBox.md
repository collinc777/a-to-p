# VideoLabelBoundingBox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top** | **int** |  | 
**left** | **int** |  | 
**height** | **int** |  | 
**width** | **int** |  | 

## Example

```python
from openapi_client.models.video_label_bounding_box import VideoLabelBoundingBox

# TODO update the JSON string below
json = "{}"
# create an instance of VideoLabelBoundingBox from a JSON string
video_label_bounding_box_instance = VideoLabelBoundingBox.from_json(json)
# print the JSON string representation of the object
print(VideoLabelBoundingBox.to_json())

# convert the object into a dict
video_label_bounding_box_dict = video_label_bounding_box_instance.to_dict()
# create an instance of VideoLabelBoundingBox from a dict
video_label_bounding_box_form_dict = video_label_bounding_box.from_dict(video_label_bounding_box_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


