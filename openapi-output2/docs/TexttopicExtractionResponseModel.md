# TexttopicExtractionResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenstorrent** | [**PydanticMainTexttopicExtractionTopicExtractionDataClass94559368983312**](PydanticMainTexttopicExtractionTopicExtractionDataClass94559368983312.md) |  | [optional] 
**openai** | [**PydanticMainTexttopicExtractionTopicExtractionDataClass94559369040736**](PydanticMainTexttopicExtractionTopicExtractionDataClass94559369040736.md) |  | [optional] 
**ibm** | [**PydanticMainTexttopicExtractionTopicExtractionDataClass94559369041680**](PydanticMainTexttopicExtractionTopicExtractionDataClass94559369041680.md) |  | [optional] 
**google** | [**PydanticMainTexttopicExtractionTopicExtractionDataClass94559368993536**](PydanticMainTexttopicExtractionTopicExtractionDataClass94559368993536.md) |  | [optional] 
**eden_ai** | [**PydanticMainTexttopicExtractionTopicExtractionDataClass94559368996704**](PydanticMainTexttopicExtractionTopicExtractionDataClass94559368996704.md) |  | [optional] 

## Example

```python
from openapi_client.models.texttopic_extraction_response_model import TexttopicExtractionResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TexttopicExtractionResponseModel from a JSON string
texttopic_extraction_response_model_instance = TexttopicExtractionResponseModel.from_json(json)
# print the JSON string representation of the object
print(TexttopicExtractionResponseModel.to_json())

# convert the object into a dict
texttopic_extraction_response_model_dict = texttopic_extraction_response_model_instance.to_dict()
# create an instance of TexttopicExtractionResponseModel from a dict
texttopic_extraction_response_model_form_dict = texttopic_extraction_response_model.from_dict(texttopic_extraction_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


