# PatchedUniversalTranslatorCreatetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_language** | **str** | The language code from which the text will be translated | [optional] 
**target_language** | **str** | The language code in which the text will be translated | [optional] 
**project_name** | **str** | The project name | [optional] 
**fall_back_providers** | **List[str]** |  | [optional] 
**provider** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.patched_universal_translator_createt_request import PatchedUniversalTranslatorCreatetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedUniversalTranslatorCreatetRequest from a JSON string
patched_universal_translator_createt_request_instance = PatchedUniversalTranslatorCreatetRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedUniversalTranslatorCreatetRequest.to_json())

# convert the object into a dict
patched_universal_translator_createt_request_dict = patched_universal_translator_createt_request_instance.to_dict()
# create an instance of PatchedUniversalTranslatorCreatetRequest from a dict
patched_universal_translator_createt_request_form_dict = patched_universal_translator_createt_request.from_dict(patched_universal_translator_createt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


