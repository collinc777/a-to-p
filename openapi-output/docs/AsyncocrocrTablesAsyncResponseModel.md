# AsyncocrocrTablesAsyncResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**OcrocrTablesAsyncModel**](OcrocrTablesAsyncModel.md) |  | 
**error** | **str** |  | 
**public_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from openapi_client.models.asyncocrocr_tables_async_response_model import AsyncocrocrTablesAsyncResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncocrocrTablesAsyncResponseModel from a JSON string
asyncocrocr_tables_async_response_model_instance = AsyncocrocrTablesAsyncResponseModel.from_json(json)
# print the JSON string representation of the object
print(AsyncocrocrTablesAsyncResponseModel.to_json())

# convert the object into a dict
asyncocrocr_tables_async_response_model_dict = asyncocrocr_tables_async_response_model_instance.to_dict()
# create an instance of AsyncocrocrTablesAsyncResponseModel from a dict
asyncocrocr_tables_async_response_model_form_dict = asyncocrocr_tables_async_response_model.from_dict(asyncocrocr_tables_async_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


