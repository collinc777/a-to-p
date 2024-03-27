# PromptTextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**feature** | **str** |  | 
**subfeature** | **str** |  | 
**provider** | **str** |  | 
**model** | **str** |  | [optional] 
**params** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openapi_client.models.prompt_text_request import PromptTextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PromptTextRequest from a JSON string
prompt_text_request_instance = PromptTextRequest.from_json(json)
# print the JSON string representation of the object
print(PromptTextRequest.to_json())

# convert the object into a dict
prompt_text_request_dict = prompt_text_request_instance.to_dict()
# create an instance of PromptTextRequest from a dict
prompt_text_request_form_dict = prompt_text_request.from_dict(prompt_text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


