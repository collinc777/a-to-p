# TextchatResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PydanticMainTextchatChatDataClass94559369249760**](PydanticMainTextchatChatDataClass94559369249760.md) |  | [optional] 
**google** | [**PydanticMainTextchatChatDataClass94559367720304**](PydanticMainTextchatChatDataClass94559367720304.md) |  | [optional] 
**cohere** | [**PydanticMainTextchatChatDataClass94559369255280**](PydanticMainTextchatChatDataClass94559369255280.md) |  | [optional] 
**mistral** | [**PydanticMainTextchatChatDataClass94559369272176**](PydanticMainTextchatChatDataClass94559369272176.md) |  | [optional] 
**replicate** | [**PydanticMainTextchatChatDataClass94559369275344**](PydanticMainTextchatChatDataClass94559369275344.md) |  | [optional] 
**perplexityai** | [**PydanticMainTextchatChatDataClass94559369279648**](PydanticMainTextchatChatDataClass94559369279648.md) |  | [optional] 
**openai** | [**PydanticMainTextchatChatDataClass94559369283952**](PydanticMainTextchatChatDataClass94559369283952.md) |  | [optional] 
**anthropic** | [**PydanticMainTextchatChatDataClass94559369288256**](PydanticMainTextchatChatDataClass94559369288256.md) |  | [optional] 

## Example

```python
from openapi_client.models.textchat_response_model import TextchatResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TextchatResponseModel from a JSON string
textchat_response_model_instance = TextchatResponseModel.from_json(json)
# print the JSON string representation of the object
print(TextchatResponseModel.to_json())

# convert the object into a dict
textchat_response_model_dict = textchat_response_model_instance.to_dict()
# create an instance of TextchatResponseModel from a dict
textchat_response_model_form_dict = textchat_response_model.from_dict(textchat_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


