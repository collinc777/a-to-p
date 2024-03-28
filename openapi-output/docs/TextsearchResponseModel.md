# TextsearchResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cohere** | [**PydanticMainTextsearchSearchDataClass94559368053600**](PydanticMainTextsearchSearchDataClass94559368053600.md) |  | [optional] 
**openai** | [**PydanticMainTextsearchSearchDataClass94559368271696**](PydanticMainTextsearchSearchDataClass94559368271696.md) |  | [optional] 
**google** | [**PydanticMainTextsearchSearchDataClass94559368037760**](PydanticMainTextsearchSearchDataClass94559368037760.md) |  | [optional] 

## Example

```python
from openapi_client.models.textsearch_response_model import TextsearchResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TextsearchResponseModel from a JSON string
textsearch_response_model_instance = TextsearchResponseModel.from_json(json)
# print the JSON string representation of the object
print(TextsearchResponseModel.to_json())

# convert the object into a dict
textsearch_response_model_dict = textsearch_response_model_instance.to_dict()
# create an instance of TextsearchResponseModel from a dict
textsearch_response_model_form_dict = textsearch_response_model.from_dict(textsearch_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


