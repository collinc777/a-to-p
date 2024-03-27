# TextembeddingsResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jina** | [**PydanticMainTextembeddingsEmbeddingsDataClass94559369236560**](PydanticMainTextembeddingsEmbeddingsDataClass94559369236560.md) |  | [optional] 
**google** | [**PydanticMainTextembeddingsEmbeddingsDataClass94559369211600**](PydanticMainTextembeddingsEmbeddingsDataClass94559369211600.md) |  | [optional] 
**cohere** | [**PydanticMainTextembeddingsEmbeddingsDataClass94559369214768**](PydanticMainTextembeddingsEmbeddingsDataClass94559369214768.md) |  | [optional] 
**mistral** | [**PydanticMainTextembeddingsEmbeddingsDataClass94559369220208**](PydanticMainTextembeddingsEmbeddingsDataClass94559369220208.md) |  | [optional] 
**ai21labs** | [**PydanticMainTextembeddingsEmbeddingsDataClass94559369223376**](PydanticMainTextembeddingsEmbeddingsDataClass94559369223376.md) |  | [optional] 
**openai** | [**PydanticMainTextembeddingsEmbeddingsDataClass94559369227088**](PydanticMainTextembeddingsEmbeddingsDataClass94559369227088.md) |  | [optional] 

## Example

```python
from openapi_client.models.textembeddings_response_model import TextembeddingsResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TextembeddingsResponseModel from a JSON string
textembeddings_response_model_instance = TextembeddingsResponseModel.from_json(json)
# print the JSON string representation of the object
print(TextembeddingsResponseModel.to_json())

# convert the object into a dict
textembeddings_response_model_dict = textembeddings_response_model_instance.to_dict()
# create an instance of TextembeddingsResponseModel from a dict
textembeddings_response_model_form_dict = textembeddings_response_model.from_dict(textembeddings_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


