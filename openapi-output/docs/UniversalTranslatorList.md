# UniversalTranslatorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_language** | **str** | The language code from which the text will be translated | [readonly] 
**target_language** | **str** | The language code in which the text will be translated | [readonly] 
**project_name** | **str** | The project name | [readonly] 
**fall_back_providers** | **str** | Providers to use in case of an error | [readonly] 
**provider** | **str** |  | [readonly] 
**project_id** | **str** |  | [readonly] 

## Example

```python
from openapi_client.models.universal_translator_list import UniversalTranslatorList

# TODO update the JSON string below
json = "{}"
# create an instance of UniversalTranslatorList from a JSON string
universal_translator_list_instance = UniversalTranslatorList.from_json(json)
# print the JSON string representation of the object
print(UniversalTranslatorList.to_json())

# convert the object into a dict
universal_translator_list_dict = universal_translator_list_instance.to_dict()
# create an instance of UniversalTranslatorList from a dict
universal_translator_list_form_dict = universal_translator_list.from_dict(universal_translator_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


