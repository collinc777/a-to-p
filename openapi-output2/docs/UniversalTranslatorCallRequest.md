# UniversalTranslatorCallRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text to analyze | 
**source_language** | **str** | Source language code (ex: en, fr) | [optional] 
**target_language** | **str** | Target language code (ex: en, fr) | 

## Example

```python
from openapi_client.models.universal_translator_call_request import UniversalTranslatorCallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UniversalTranslatorCallRequest from a JSON string
universal_translator_call_request_instance = UniversalTranslatorCallRequest.from_json(json)
# print the JSON string representation of the object
print(UniversalTranslatorCallRequest.to_json())

# convert the object into a dict
universal_translator_call_request_dict = universal_translator_call_request_instance.to_dict()
# create an instance of UniversalTranslatorCallRequest from a dict
universal_translator_call_request_form_dict = universal_translator_call_request.from_dict(universal_translator_call_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


