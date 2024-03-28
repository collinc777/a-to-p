# YodaAskLlmResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | 
**llm_provider** | **str** |  | 
**llm_model** | **str** |  | 

## Example

```python
from openapi_client.models.yoda_ask_llm_response import YodaAskLlmResponse

# TODO update the JSON string below
json = "{}"
# create an instance of YodaAskLlmResponse from a JSON string
yoda_ask_llm_response_instance = YodaAskLlmResponse.from_json(json)
# print the JSON string representation of the object
print(YodaAskLlmResponse.to_json())

# convert the object into a dict
yoda_ask_llm_response_dict = yoda_ask_llm_response_instance.to_dict()
# create an instance of YodaAskLlmResponse from a dict
yoda_ask_llm_response_form_dict = yoda_ask_llm_response.from_dict(yoda_ask_llm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


