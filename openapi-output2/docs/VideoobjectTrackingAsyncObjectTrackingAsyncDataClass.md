# VideoobjectTrackingAsyncObjectTrackingAsyncDataClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ObjectTrack]**](ObjectTrack.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**id** | **str** |  | 
**final_status** | [**FinalStatusEnum**](FinalStatusEnum.md) |  | 
**error** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.videoobject_tracking_async_object_tracking_async_data_class import VideoobjectTrackingAsyncObjectTrackingAsyncDataClass

# TODO update the JSON string below
json = "{}"
# create an instance of VideoobjectTrackingAsyncObjectTrackingAsyncDataClass from a JSON string
videoobject_tracking_async_object_tracking_async_data_class_instance = VideoobjectTrackingAsyncObjectTrackingAsyncDataClass.from_json(json)
# print the JSON string representation of the object
print(VideoobjectTrackingAsyncObjectTrackingAsyncDataClass.to_json())

# convert the object into a dict
videoobject_tracking_async_object_tracking_async_data_class_dict = videoobject_tracking_async_object_tracking_async_data_class_instance.to_dict()
# create an instance of VideoobjectTrackingAsyncObjectTrackingAsyncDataClass from a dict
videoobject_tracking_async_object_tracking_async_data_class_form_dict = videoobject_tracking_async_object_tracking_async_data_class.from_dict(videoobject_tracking_async_object_tracking_async_data_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


