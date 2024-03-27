# AskLLMRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Enter your question or query about the data. The large language model (LLM) will provide a response. | 
**llm_provider** | **str** | Select a provider for the large language model for processing. Leave empty for default. | [optional] [default to 'openai']
**llm_model** | **str** | Specify the model to use for language processing. Leave empty for default. | [optional] 
**k** | **int** | How many results chunk you want to return | [optional] [default to 3]
**history** | **List[Dict[str, object]]** | A list containing all the previous conversations between the user and the chatbot AI. Each item in the list should be a dictionary with two keys: &#39;user&#39; and &#39;assistant&#39;. | [optional] [default to []]
**chatbot_global_action** | **str** | A system message that helps set the behavior of the assistant. | [optional] 
**filter_documents** | **Dict[str, object]** | Filter uploaded documents based on their metadata. Specify key-value pairs where the key represents the metadata field and the value is the desired metadata value. Please ensure that the provided metadata keys are available in your database. | [optional] 
**temperature** | **float** | Higher values mean the model will take more risks and value 0 (argmax sampling) works better for scenarios with a well-defined answer. | [optional] [default to 0.0]
**max_tokens** | **int** | The maximum number of tokens to generate in the completion. The token count of your prompt plus max_tokens cannot exceed the model&#39;s context length. | [optional] [default to 100]

## Example

```python
from openapi_client.models.ask_llm_request import AskLLMRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AskLLMRequest from a JSON string
ask_llm_request_instance = AskLLMRequest.from_json(json)
# print the JSON string representation of the object
print(AskLLMRequest.to_json())

# convert the object into a dict
ask_llm_request_dict = ask_llm_request_instance.to_dict()
# create an instance of AskLLMRequest from a dict
ask_llm_request_form_dict = ask_llm_request.from_dict(ask_llm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


