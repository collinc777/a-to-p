# AsyncvideopersonTrackingAsyncResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**VideopersonTrackingAsyncModel**](VideopersonTrackingAsyncModel.md) |  | 
**error** | **str** |  | 
**public_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from openapi_client.models.asyncvideoperson_tracking_async_response_model import AsyncvideopersonTrackingAsyncResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncvideopersonTrackingAsyncResponseModel from a JSON string
asyncvideoperson_tracking_async_response_model_instance = AsyncvideopersonTrackingAsyncResponseModel.from_json(json)
# print the JSON string representation of the object
print(AsyncvideopersonTrackingAsyncResponseModel.to_json())

# convert the object into a dict
asyncvideoperson_tracking_async_response_model_dict = asyncvideoperson_tracking_async_response_model_instance.to_dict()
# create an instance of AsyncvideopersonTrackingAsyncResponseModel from a dict
asyncvideoperson_tracking_async_response_model_form_dict = asyncvideoperson_tracking_async_response_model.from_dict(asyncvideoperson_tracking_async_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


