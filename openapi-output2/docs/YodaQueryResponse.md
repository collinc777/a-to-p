# YodaQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[YodaQueryResponseItem]**](YodaQueryResponseItem.md) |  | 

## Example

```python
from openapi_client.models.yoda_query_response import YodaQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of YodaQueryResponse from a JSON string
yoda_query_response_instance = YodaQueryResponse.from_json(json)
# print the JSON string representation of the object
print(YodaQueryResponse.to_json())

# convert the object into a dict
yoda_query_response_dict = yoda_query_response_instance.to_dict()
# create an instance of YodaQueryResponse from a dict
yoda_query_response_form_dict = yoda_query_response.from_dict(yoda_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


