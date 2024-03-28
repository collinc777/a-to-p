# PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559364450848


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**diarization** | [**SpeechDiarization**](SpeechDiarization.md) |  | 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**id** | **str** |  | 
**final_status** | [**FinalStatusEnum**](FinalStatusEnum.md) |  | 
**error** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.pydantic_main_audiospeech_to_text_async_speech_to_text_async_data_class94559364450848 import PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559364450848

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559364450848 from a JSON string
pydantic_main_audiospeech_to_text_async_speech_to_text_async_data_class94559364450848_instance = PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559364450848.from_json(json)
# print the JSON string representation of the object
print(PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559364450848.to_json())

# convert the object into a dict
pydantic_main_audiospeech_to_text_async_speech_to_text_async_data_class94559364450848_dict = pydantic_main_audiospeech_to_text_async_speech_to_text_async_data_class94559364450848_instance.to_dict()
# create an instance of PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559364450848 from a dict
pydantic_main_audiospeech_to_text_async_speech_to_text_async_data_class94559364450848_form_dict = pydantic_main_audiospeech_to_text_async_speech_to_text_async_data_class94559364450848.from_dict(pydantic_main_audiospeech_to_text_async_speech_to_text_async_data_class94559364450848_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


