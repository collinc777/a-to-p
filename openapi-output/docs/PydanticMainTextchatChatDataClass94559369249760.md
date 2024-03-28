# PydanticMainTextchatChatDataClass94559369249760


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generated_text** | **str** |  | 
**message** | [**List[ChatMessageDataClass]**](ChatMessageDataClass.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**status** | [**StatusF43Enum**](StatusF43Enum.md) |  | 

## Example

```python
from openapi_client.models.pydantic_main_textchat_chat_data_class94559369249760 import PydanticMainTextchatChatDataClass94559369249760

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainTextchatChatDataClass94559369249760 from a JSON string
pydantic_main_textchat_chat_data_class94559369249760_instance = PydanticMainTextchatChatDataClass94559369249760.from_json(json)
# print the JSON string representation of the object
print(PydanticMainTextchatChatDataClass94559369249760.to_json())

# convert the object into a dict
pydantic_main_textchat_chat_data_class94559369249760_dict = pydantic_main_textchat_chat_data_class94559369249760_instance.to_dict()
# create an instance of PydanticMainTextchatChatDataClass94559369249760 from a dict
pydantic_main_textchat_chat_data_class94559369249760_form_dict = pydantic_main_textchat_chat_data_class94559369249760.from_dict(pydantic_main_textchat_chat_data_class94559369249760_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


