# YodaInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_provider** | **str** |  | 
**embeddings_provider** | **str** |  | 
**llm_provider** | **str** |  | 
**llm_model** | **str** |  | 
**collection_size** | **int** |  | 

## Example

```python
from openapi_client.models.yoda_info_response import YodaInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of YodaInfoResponse from a JSON string
yoda_info_response_instance = YodaInfoResponse.from_json(json)
# print the JSON string representation of the object
print(YodaInfoResponse.to_json())

# convert the object into a dict
yoda_info_response_dict = yoda_info_response_instance.to_dict()
# create an instance of YodaInfoResponse from a dict
yoda_info_response_form_dict = yoda_info_response.from_dict(yoda_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


