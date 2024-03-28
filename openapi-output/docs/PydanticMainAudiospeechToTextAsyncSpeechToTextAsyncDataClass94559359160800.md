# PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559359160800


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
from openapi_client.models.pydantic_main_audiospeech_to_text_async_speech_to_text_async_data_class94559359160800 import PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559359160800

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559359160800 from a JSON string
pydantic_main_audiospeech_to_text_async_speech_to_text_async_data_class94559359160800_instance = PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559359160800.from_json(json)
# print the JSON string representation of the object
print(PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559359160800.to_json())

# convert the object into a dict
pydantic_main_audiospeech_to_text_async_speech_to_text_async_data_class94559359160800_dict = pydantic_main_audiospeech_to_text_async_speech_to_text_async_data_class94559359160800_instance.to_dict()
# create an instance of PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559359160800 from a dict
pydantic_main_audiospeech_to_text_async_speech_to_text_async_data_class94559359160800_form_dict = pydantic_main_audiospeech_to_text_async_speech_to_text_async_data_class94559359160800.from_dict(pydantic_main_audiospeech_to_text_async_speech_to_text_async_data_class94559359160800_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


