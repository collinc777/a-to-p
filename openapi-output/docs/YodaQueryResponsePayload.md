# YodaQueryResponsePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | 
**page_content** | **str** |  | 

## Example

```python
from openapi_client.models.yoda_query_response_payload import YodaQueryResponsePayload

# TODO update the JSON string below
json = "{}"
# create an instance of YodaQueryResponsePayload from a JSON string
yoda_query_response_payload_instance = YodaQueryResponsePayload.from_json(json)
# print the JSON string representation of the object
print(YodaQueryResponsePayload.to_json())

# convert the object into a dict
yoda_query_response_payload_dict = yoda_query_response_payload_instance.to_dict()
# create an instance of YodaQueryResponsePayload from a dict
yoda_query_response_payload_form_dict = yoda_query_response_payload.from_dict(yoda_query_response_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


