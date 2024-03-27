# UniversalTranslatorCreatet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_language** | **str** | The language code from which the text will be translated | [optional] 
**target_language** | **str** | The language code in which the text will be translated | [optional] 
**project_name** | **str** | The project name | 
**fall_back_providers** | **List[str]** |  | [optional] 
**provider** | **str** |  | 

## Example

```python
from openapi_client.models.universal_translator_createt import UniversalTranslatorCreatet

# TODO update the JSON string below
json = "{}"
# create an instance of UniversalTranslatorCreatet from a JSON string
universal_translator_createt_instance = UniversalTranslatorCreatet.from_json(json)
# print the JSON string representation of the object
print(UniversalTranslatorCreatet.to_json())

# convert the object into a dict
universal_translator_createt_dict = universal_translator_createt_instance.to_dict()
# create an instance of UniversalTranslatorCreatet from a dict
universal_translator_createt_form_dict = universal_translator_createt.from_dict(universal_translator_createt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


