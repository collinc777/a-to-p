# PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559367937600


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general_sentiment** | [**GeneralSentimentEnum**](GeneralSentimentEnum.md) |  | 
**general_sentiment_rate** | **int** |  | 
**items** | [**List[SegmentSentimentAnalysisDataClass]**](SegmentSentimentAnalysisDataClass.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**status** | [**StatusF43Enum**](StatusF43Enum.md) |  | 

## Example

```python
from openapi_client.models.pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559367937600 import PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559367937600

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559367937600 from a JSON string
pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559367937600_instance = PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559367937600.from_json(json)
# print the JSON string representation of the object
print(PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559367937600.to_json())

# convert the object into a dict
pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559367937600_dict = pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559367937600_instance.to_dict()
# create an instance of PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559367937600 from a dict
pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559367937600_form_dict = pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559367937600.from_dict(pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559367937600_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


