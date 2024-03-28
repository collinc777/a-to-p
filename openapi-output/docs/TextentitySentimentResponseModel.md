# TextentitySentimentResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amazon** | [**PydanticMainTextentitySentimentEntitySentimentDataClass94559369338896**](PydanticMainTextentitySentimentEntitySentimentDataClass94559369338896.md) |  | [optional] 
**google** | [**PydanticMainTextentitySentimentEntitySentimentDataClass94559369339840**](PydanticMainTextentitySentimentEntitySentimentDataClass94559369339840.md) |  | [optional] 

## Example

```python
from openapi_client.models.textentity_sentiment_response_model import TextentitySentimentResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TextentitySentimentResponseModel from a JSON string
textentity_sentiment_response_model_instance = TextentitySentimentResponseModel.from_json(json)
# print the JSON string representation of the object
print(TextentitySentimentResponseModel.to_json())

# convert the object into a dict
textentity_sentiment_response_model_dict = textentity_sentiment_response_model_instance.to_dict()
# create an instance of TextentitySentimentResponseModel from a dict
textentity_sentiment_response_model_form_dict = textentity_sentiment_response_model.from_dict(textentity_sentiment_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


