# VideoFace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | 
**bounding_box** | [**VideoBoundingBox**](VideoBoundingBox.md) |  | 
**attributes** | [**FaceAttributes**](FaceAttributes.md) |  | 
**landmarks** | [**LandmarksVideo**](LandmarksVideo.md) |  | 

## Example

```python
from openapi_client.models.video_face import VideoFace

# TODO update the JSON string below
json = "{}"
# create an instance of VideoFace from a JSON string
video_face_instance = VideoFace.from_json(json)
# print the JSON string representation of the object
print(VideoFace.to_json())

# convert the object into a dict
video_face_dict = video_face_instance.to_dict()
# create an instance of VideoFace from a dict
video_face_form_dict = video_face.from_dict(video_face_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


