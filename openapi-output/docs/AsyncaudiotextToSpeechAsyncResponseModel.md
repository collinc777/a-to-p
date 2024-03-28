# AsyncaudiotextToSpeechAsyncResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**AudiotextToSpeechAsyncModel**](AudiotextToSpeechAsyncModel.md) |  | 
**error** | **str** |  | 
**public_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from openapi_client.models.asyncaudiotext_to_speech_async_response_model import AsyncaudiotextToSpeechAsyncResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncaudiotextToSpeechAsyncResponseModel from a JSON string
asyncaudiotext_to_speech_async_response_model_instance = AsyncaudiotextToSpeechAsyncResponseModel.from_json(json)
# print the JSON string representation of the object
print(AsyncaudiotextToSpeechAsyncResponseModel.to_json())

# convert the object into a dict
asyncaudiotext_to_speech_async_response_model_dict = asyncaudiotext_to_speech_async_response_model_instance.to_dict()
# create an instance of AsyncaudiotextToSpeechAsyncResponseModel from a dict
asyncaudiotext_to_speech_async_response_model_form_dict = asyncaudiotext_to_speech_async_response_model.from_dict(asyncaudiotext_to_speech_async_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


