# TextspellCheckResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sapling** | [**PydanticMainTextspellCheckSpellCheckDataClass94559369107088**](PydanticMainTextspellCheckSpellCheckDataClass94559369107088.md) |  | [optional] 
**microsoft** | [**PydanticMainTextspellCheckSpellCheckDataClass94559369172032**](PydanticMainTextspellCheckSpellCheckDataClass94559369172032.md) |  | [optional] 
**cohere** | [**PydanticMainTextspellCheckSpellCheckDataClass94559369163728**](PydanticMainTextspellCheckSpellCheckDataClass94559369163728.md) |  | [optional] 
**ai21labs** | [**PydanticMainTextspellCheckSpellCheckDataClass94559369164672**](PydanticMainTextspellCheckSpellCheckDataClass94559369164672.md) |  | [optional] 
**prowritingaid** | [**PydanticMainTextspellCheckSpellCheckDataClass94559369187248**](PydanticMainTextspellCheckSpellCheckDataClass94559369187248.md) |  | [optional] 
**nlpcloud** | [**PydanticMainTextspellCheckSpellCheckDataClass94559369190960**](PydanticMainTextspellCheckSpellCheckDataClass94559369190960.md) |  | [optional] 
**openai** | [**PydanticMainTextspellCheckSpellCheckDataClass94559369195264**](PydanticMainTextspellCheckSpellCheckDataClass94559369195264.md) |  | [optional] 

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


