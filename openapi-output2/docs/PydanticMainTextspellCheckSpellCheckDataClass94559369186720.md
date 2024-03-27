# PydanticMainTextspellCheckSpellCheckDataClass94559369186720


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**items** | [**List[SpellCheckItem]**](SpellCheckItem.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**status** | [**StatusF43Enum**](StatusF43Enum.md) |  | 

## Example

```python
from openapi_client.models.pydantic_main_textspell_check_spell_check_data_class94559369186720 import PydanticMainTextspellCheckSpellCheckDataClass94559369186720

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainTextspellCheckSpellCheckDataClass94559369186720 from a JSON string
pydantic_main_textspell_check_spell_check_data_class94559369186720_instance = PydanticMainTextspellCheckSpellCheckDataClass94559369186720.from_json(json)
# print the JSON string representation of the object
print(PydanticMainTextspellCheckSpellCheckDataClass94559369186720.to_json())

# convert the object into a dict
pydantic_main_textspell_check_spell_check_data_class94559369186720_dict = pydantic_main_textspell_check_spell_check_data_class94559369186720_instance.to_dict()
# create an instance of PydanticMainTextspellCheckSpellCheckDataClass94559369186720 from a dict
pydantic_main_textspell_check_spell_check_data_class94559369186720_form_dict = pydantic_main_textspell_check_spell_check_data_class94559369186720.from_dict(pydantic_main_textspell_check_spell_check_data_class94559369186720_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


