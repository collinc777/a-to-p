# SpeechDiarizationEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment** | **str** |  | 
**start_time** | **str** |  | 
**end_time** | **str** |  | 
**speaker** | **int** |  | 
**confidence** | **int** |  | 

## Example

```python
from openapi_client.models.speech_diarization_entry import SpeechDiarizationEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SpeechDiarizationEntry from a JSON string
speech_diarization_entry_instance = SpeechDiarizationEntry.from_json(json)
# print the JSON string representation of the object
print(SpeechDiarizationEntry.to_json())

# convert the object into a dict
speech_diarization_entry_dict = speech_diarization_entry_instance.to_dict()
# create an instance of SpeechDiarizationEntry from a dict
speech_diarization_entry_form_dict = speech_diarization_entry.from_dict(speech_diarization_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


