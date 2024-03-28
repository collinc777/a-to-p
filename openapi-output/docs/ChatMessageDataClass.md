# ChatMessageDataClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from openapi_client.models.chat_message_data_class import ChatMessageDataClass

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessageDataClass from a JSON string
chat_message_data_class_instance = ChatMessageDataClass.from_json(json)
# print the JSON string representation of the object
print(ChatMessageDataClass.to_json())

# convert the object into a dict
chat_message_data_class_dict = chat_message_data_class_instance.to_dict()
# create an instance of ChatMessageDataClass from a dict
chat_message_data_class_form_dict = chat_message_data_class.from_dict(chat_message_data_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


