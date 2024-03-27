# AsyncvideoobjectTrackingAsyncResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**VideoobjectTrackingAsyncModel**](VideoobjectTrackingAsyncModel.md) |  | 
**error** | **str** |  | 
**public_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from openapi_client.models.asyncvideoobject_tracking_async_response_model import AsyncvideoobjectTrackingAsyncResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncvideoobjectTrackingAsyncResponseModel from a JSON string
asyncvideoobject_tracking_async_response_model_instance = AsyncvideoobjectTrackingAsyncResponseModel.from_json(json)
# print the JSON string representation of the object
print(AsyncvideoobjectTrackingAsyncResponseModel.to_json())

# convert the object into a dict
asyncvideoobject_tracking_async_response_model_dict = asyncvideoobject_tracking_async_response_model_instance.to_dict()
# create an instance of AsyncvideoobjectTrackingAsyncResponseModel from a dict
asyncvideoobject_tracking_async_response_model_form_dict = asyncvideoobject_tracking_async_response_model.from_dict(asyncvideoobject_tracking_async_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


