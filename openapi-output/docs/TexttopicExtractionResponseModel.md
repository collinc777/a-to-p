# TexttopicExtractionResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenstorrent** | [**PydanticMainTexttopicExtractionTopicExtractionDataClass94559369043040**](PydanticMainTexttopicExtractionTopicExtractionDataClass94559369043040.md) |  | [optional] 
**openai** | [**PydanticMainTexttopicExtractionTopicExtractionDataClass94559369043984**](PydanticMainTexttopicExtractionTopicExtractionDataClass94559369043984.md) |  | [optional] 
**ibm** | [**PydanticMainTexttopicExtractionTopicExtractionDataClass94559368028464**](PydanticMainTexttopicExtractionTopicExtractionDataClass94559368028464.md) |  | [optional] 
**google** | [**PydanticMainTexttopicExtractionTopicExtractionDataClass94559368086512**](PydanticMainTexttopicExtractionTopicExtractionDataClass94559368086512.md) |  | [optional] 
**eden_ai** | [**PydanticMainTexttopicExtractionTopicExtractionDataClass94559368087456**](PydanticMainTexttopicExtractionTopicExtractionDataClass94559368087456.md) |  | [optional] 

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


