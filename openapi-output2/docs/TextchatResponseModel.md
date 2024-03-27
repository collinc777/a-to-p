# TextchatResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PydanticMainTextchatChatDataClass94559369250272**](PydanticMainTextchatChatDataClass94559369250272.md) |  | [optional] 
**google** | [**PydanticMainTextchatChatDataClass94559369272672**](PydanticMainTextchatChatDataClass94559369272672.md) |  | [optional] 
**cohere** | [**PydanticMainTextchatChatDataClass94559369245232**](PydanticMainTextchatChatDataClass94559369245232.md) |  | [optional] 
**mistral** | [**PydanticMainTextchatChatDataClass94559369287168**](PydanticMainTextchatChatDataClass94559369287168.md) |  | [optional] 
**replicate** | [**PydanticMainTextchatChatDataClass94559369254976**](PydanticMainTextchatChatDataClass94559369254976.md) |  | [optional] 
**perplexityai** | [**PydanticMainTextchatChatDataClass94559369294544**](PydanticMainTextchatChatDataClass94559369294544.md) |  | [optional] 
**openai** | [**PydanticMainTextchatChatDataClass94559369298256**](PydanticMainTextchatChatDataClass94559369298256.md) |  | [optional] 
**anthropic** | [**PydanticMainTextchatChatDataClass94559369303152**](PydanticMainTextchatChatDataClass94559369303152.md) |  | [optional] 

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


