# AsyncaudiospeechToTextAsyncResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**AudiospeechToTextAsyncModel**](AudiospeechToTextAsyncModel.md) |  | 
**error** | **str** |  | 
**public_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from openapi_client.models.asyncaudiospeech_to_text_async_response_model import AsyncaudiospeechToTextAsyncResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncaudiospeechToTextAsyncResponseModel from a JSON string
asyncaudiospeech_to_text_async_response_model_instance = AsyncaudiospeechToTextAsyncResponseModel.from_json(json)
# print the JSON string representation of the object
print(AsyncaudiospeechToTextAsyncResponseModel.to_json())

# convert the object into a dict
asyncaudiospeech_to_text_async_response_model_dict = asyncaudiospeech_to_text_async_response_model_instance.to_dict()
# create an instance of AsyncaudiospeechToTextAsyncResponseModel from a dict
asyncaudiospeech_to_text_async_response_model_form_dict = asyncaudiospeech_to_text_async_response_model.from_dict(asyncaudiospeech_to_text_async_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


