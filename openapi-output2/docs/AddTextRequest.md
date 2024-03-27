# AddTextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**texts** | **List[str]** | LLM Query | 
**metadata** | **List[Dict[str, object]]** |  | [optional] [default to []]

## Example

```python
from openapi_client.models.add_text_request import AddTextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTextRequest from a JSON string
add_text_request_instance = AddTextRequest.from_json(json)
# print the JSON string representation of the object
print(AddTextRequest.to_json())

# convert the object into a dict
add_text_request_dict = add_text_request_instance.to_dict()
# create an instance of AddTextRequest from a dict
add_text_request_form_dict = add_text_request.from_dict(add_text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


