# TextspellCheckResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sapling** | [**PydanticMainTextspellCheckSpellCheckDataClass94559369168448**](PydanticMainTextspellCheckSpellCheckDataClass94559369168448.md) |  | [optional] 
**microsoft** | [**PydanticMainTextspellCheckSpellCheckDataClass94559369183552**](PydanticMainTextspellCheckSpellCheckDataClass94559369183552.md) |  | [optional] 
**cohere** | [**PydanticMainTextspellCheckSpellCheckDataClass94559369186720**](PydanticMainTextspellCheckSpellCheckDataClass94559369186720.md) |  | [optional] 
**ai21labs** | [**PydanticMainTextspellCheckSpellCheckDataClass94559369174816**](PydanticMainTextspellCheckSpellCheckDataClass94559369174816.md) |  | [optional] 
**prowritingaid** | [**PydanticMainTextspellCheckSpellCheckDataClass94559369190336**](PydanticMainTextspellCheckSpellCheckDataClass94559369190336.md) |  | [optional] 
**nlpcloud** | [**PydanticMainTextspellCheckSpellCheckDataClass94559369194640**](PydanticMainTextspellCheckSpellCheckDataClass94559369194640.md) |  | [optional] 
**openai** | [**PydanticMainTextspellCheckSpellCheckDataClass94559369198944**](PydanticMainTextspellCheckSpellCheckDataClass94559369198944.md) |  | [optional] 

## Example

```python
from openapi_client.models.textspell_check_response_model import TextspellCheckResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TextspellCheckResponseModel from a JSON string
textspell_check_response_model_instance = TextspellCheckResponseModel.from_json(json)
# print the JSON string representation of the object
print(TextspellCheckResponseModel.to_json())

# convert the object into a dict
textspell_check_response_model_dict = textspell_check_response_model_instance.to_dict()
# create an instance of TextspellCheckResponseModel from a dict
textspell_check_response_model_form_dict = textspell_check_response_model.from_dict(textspell_check_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


