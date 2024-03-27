# YodaQueryResponseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version** | **int** |  | 
**score** | **int** |  | 
**payload** | [**YodaQueryResponsePayload**](YodaQueryResponsePayload.md) |  | 
**vector** | **object** |  | 

## Example

```python
from openapi_client.models.yoda_query_response_item import YodaQueryResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of YodaQueryResponseItem from a JSON string
yoda_query_response_item_instance = YodaQueryResponseItem.from_json(json)
# print the JSON string representation of the object
print(YodaQueryResponseItem.to_json())

# convert the object into a dict
yoda_query_response_item_dict = yoda_query_response_item_instance.to_dict()
# create an instance of YodaQueryResponseItem from a dict
yoda_query_response_item_form_dict = yoda_query_response_item.from_dict(yoda_query_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


