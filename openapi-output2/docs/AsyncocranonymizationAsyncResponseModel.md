# AsyncocranonymizationAsyncResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**OcranonymizationAsyncModel**](OcranonymizationAsyncModel.md) |  | 
**error** | **str** |  | 
**public_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from openapi_client.models.asyncocranonymization_async_response_model import AsyncocranonymizationAsyncResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncocranonymizationAsyncResponseModel from a JSON string
asyncocranonymization_async_response_model_instance = AsyncocranonymizationAsyncResponseModel.from_json(json)
# print the JSON string representation of the object
print(AsyncocranonymizationAsyncResponseModel.to_json())

# convert the object into a dict
asyncocranonymization_async_response_model_dict = asyncocranonymization_async_response_model_instance.to_dict()
# create an instance of AsyncocranonymizationAsyncResponseModel from a dict
asyncocranonymization_async_response_model_form_dict = asyncocranonymization_async_response_model.from_dict(asyncocranonymization_async_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


