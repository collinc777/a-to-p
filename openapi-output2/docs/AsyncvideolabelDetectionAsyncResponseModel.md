# AsyncvideolabelDetectionAsyncResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**VideolabelDetectionAsyncModel**](VideolabelDetectionAsyncModel.md) |  | 
**error** | **str** |  | 
**public_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from openapi_client.models.asyncvideolabel_detection_async_response_model import AsyncvideolabelDetectionAsyncResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncvideolabelDetectionAsyncResponseModel from a JSON string
asyncvideolabel_detection_async_response_model_instance = AsyncvideolabelDetectionAsyncResponseModel.from_json(json)
# print the JSON string representation of the object
print(AsyncvideolabelDetectionAsyncResponseModel.to_json())

# convert the object into a dict
asyncvideolabel_detection_async_response_model_dict = asyncvideolabel_detection_async_response_model_instance.to_dict()
# create an instance of AsyncvideolabelDetectionAsyncResponseModel from a dict
asyncvideolabel_detection_async_response_model_form_dict = asyncvideolabel_detection_async_response_model.from_dict(asyncvideolabel_detection_async_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


