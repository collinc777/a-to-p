# SpeechDiarization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_speakers** | **int** |  | 
**entries** | [**List[SpeechDiarizationEntry]**](SpeechDiarizationEntry.md) |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.speech_diarization import SpeechDiarization

# TODO update the JSON string below
json = "{}"
# create an instance of SpeechDiarization from a JSON string
speech_diarization_instance = SpeechDiarization.from_json(json)
# print the JSON string representation of the object
print(SpeechDiarization.to_json())

# convert the object into a dict
speech_diarization_dict = speech_diarization_instance.to_dict()
# create an instance of SpeechDiarization from a dict
speech_diarization_form_dict = speech_diarization.from_dict(speech_diarization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


