# AsyncvideologoDetectionAsyncResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**VideologoDetectionAsyncModel**](VideologoDetectionAsyncModel.md) |  | 
**error** | **str** |  | 
**public_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from openapi_client.models.asyncvideologo_detection_async_response_model import AsyncvideologoDetectionAsyncResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncvideologoDetectionAsyncResponseModel from a JSON string
asyncvideologo_detection_async_response_model_instance = AsyncvideologoDetectionAsyncResponseModel.from_json(json)
# print the JSON string representation of the object
print(AsyncvideologoDetectionAsyncResponseModel.to_json())

# convert the object into a dict
asyncvideologo_detection_async_response_model_dict = asyncvideologo_detection_async_response_model_instance.to_dict()
# create an instance of AsyncvideologoDetectionAsyncResponseModel from a dict
asyncvideologo_detection_async_response_model_form_dict = asyncvideologo_detection_async_response_model.from_dict(asyncvideologo_detection_async_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


