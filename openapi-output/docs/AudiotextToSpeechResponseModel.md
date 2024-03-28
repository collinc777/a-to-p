# AudiotextToSpeechResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**microsoft** | [**PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359106256**](PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359106256.md) |  | [optional] 
**ibm** | [**PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359105216**](PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359105216.md) |  | [optional] 
**google** | [**PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359104176**](PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359104176.md) |  | [optional] 
**amazon** | [**PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359103136**](PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359103136.md) |  | [optional] 
**elevenlabs** | [**PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359102096**](PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359102096.md) |  | [optional] 
**lovoai** | [**PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359101056**](PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359101056.md) |  | [optional] 
**openai** | [**PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359237264**](PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359237264.md) |  | [optional] 

## Example

```python
from openapi_client.models.audiotext_to_speech_response_model import AudiotextToSpeechResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AudiotextToSpeechResponseModel from a JSON string
audiotext_to_speech_response_model_instance = AudiotextToSpeechResponseModel.from_json(json)
# print the JSON string representation of the object
print(AudiotextToSpeechResponseModel.to_json())

# convert the object into a dict
audiotext_to_speech_response_model_dict = audiotext_to_speech_response_model_instance.to_dict()
# create an instance of AudiotextToSpeechResponseModel from a dict
audiotext_to_speech_response_model_form_dict = audiotext_to_speech_response_model.from_dict(audiotext_to_speech_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


