# AsyncvideotextDetectionAsyncResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**VideotextDetectionAsyncModel**](VideotextDetectionAsyncModel.md) |  | 
**error** | **str** |  | 
**public_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from openapi_client.models.asyncvideotext_detection_async_response_model import AsyncvideotextDetectionAsyncResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncvideotextDetectionAsyncResponseModel from a JSON string
asyncvideotext_detection_async_response_model_instance = AsyncvideotextDetectionAsyncResponseModel.from_json(json)
# print the JSON string representation of the object
print(AsyncvideotextDetectionAsyncResponseModel.to_json())

# convert the object into a dict
asyncvideotext_detection_async_response_model_dict = asyncvideotext_detection_async_response_model_instance.to_dict()
# create an instance of AsyncvideotextDetectionAsyncResponseModel from a dict
asyncvideotext_detection_async_response_model_form_dict = asyncvideotext_detection_async_response_model.from_dict(asyncvideotext_detection_async_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


