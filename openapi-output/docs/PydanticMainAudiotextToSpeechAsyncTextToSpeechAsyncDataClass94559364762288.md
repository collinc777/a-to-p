# PydanticMainAudiotextToSpeechAsyncTextToSpeechAsyncDataClass94559364762288


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio** | **str** |  | 
**voice_type** | **int** |  | 
**audio_resource_url** | **str** |  | 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**id** | **str** |  | 
**final_status** | [**FinalStatusEnum**](FinalStatusEnum.md) |  | 
**error** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.pydantic_main_audiotext_to_speech_async_text_to_speech_async_data_class94559364762288 import PydanticMainAudiotextToSpeechAsyncTextToSpeechAsyncDataClass94559364762288

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainAudiotextToSpeechAsyncTextToSpeechAsyncDataClass94559364762288 from a JSON string
pydantic_main_audiotext_to_speech_async_text_to_speech_async_data_class94559364762288_instance = PydanticMainAudiotextToSpeechAsyncTextToSpeechAsyncDataClass94559364762288.from_json(json)
# print the JSON string representation of the object
print(PydanticMainAudiotextToSpeechAsyncTextToSpeechAsyncDataClass94559364762288.to_json())

# convert the object into a dict
pydantic_main_audiotext_to_speech_async_text_to_speech_async_data_class94559364762288_dict = pydantic_main_audiotext_to_speech_async_text_to_speech_async_data_class94559364762288_instance.to_dict()
# create an instance of PydanticMainAudiotextToSpeechAsyncTextToSpeechAsyncDataClass94559364762288 from a dict
pydantic_main_audiotext_to_speech_async_text_to_speech_async_data_class94559364762288_form_dict = pydantic_main_audiotext_to_speech_async_text_to_speech_async_data_class94559364762288.from_dict(pydantic_main_audiotext_to_speech_async_text_to_speech_async_data_class94559364762288_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


