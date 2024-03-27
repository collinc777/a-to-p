# VideoTrackingPerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracked** | [**List[PersonTracking]**](PersonTracking.md) |  | [optional] 

## Example

```python
from openapi_client.models.video_tracking_person import VideoTrackingPerson

# TODO update the JSON string below
json = "{}"
# create an instance of VideoTrackingPerson from a JSON string
video_tracking_person_instance = VideoTrackingPerson.from_json(json)
# print the JSON string representation of the object
print(VideoTrackingPerson.to_json())

# convert the object into a dict
video_tracking_person_dict = video_tracking_person_instance.to_dict()
# create an instance of VideoTrackingPerson from a dict
video_tracking_person_form_dict = video_tracking_person.from_dict(video_tracking_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


