# AsyncvideofaceDetectionAsyncResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**VideofaceDetectionAsyncModel**](VideofaceDetectionAsyncModel.md) |  | 
**error** | **str** |  | 
**public_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from openapi_client.models.asyncvideoface_detection_async_response_model import AsyncvideofaceDetectionAsyncResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncvideofaceDetectionAsyncResponseModel from a JSON string
asyncvideoface_detection_async_response_model_instance = AsyncvideofaceDetectionAsyncResponseModel.from_json(json)
# print the JSON string representation of the object
print(AsyncvideofaceDetectionAsyncResponseModel.to_json())

# convert the object into a dict
asyncvideoface_detection_async_response_model_dict = asyncvideoface_detection_async_response_model_instance.to_dict()
# create an instance of AsyncvideofaceDetectionAsyncResponseModel from a dict
asyncvideoface_detection_async_response_model_form_dict = asyncvideoface_detection_async_response_model.from_dict(asyncvideoface_detection_async_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


