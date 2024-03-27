# SegmentSentimentAnalysisDataClass

This class is used in SentimentAnalysisDataClass to describe each segment analyzed.      Args:         - segment (str): The segment analyzed         - sentiment (Literal['Positve', 'Negative', 'Neutral']) (Case is ignore): Sentiment of segment         - sentiment_rate (float between 0 and 1): Rate of sentiment     

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment** | **str** |  | 
**sentiment** | [**SentimentB6eEnum**](SentimentB6eEnum.md) |  | 
**sentiment_rate** | **int** |  | 

## Example

```python
from openapi_client.models.segment_sentiment_analysis_data_class import SegmentSentimentAnalysisDataClass

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentSentimentAnalysisDataClass from a JSON string
segment_sentiment_analysis_data_class_instance = SegmentSentimentAnalysisDataClass.from_json(json)
# print the JSON string representation of the object
print(SegmentSentimentAnalysisDataClass.to_json())

# convert the object into a dict
segment_sentiment_analysis_data_class_dict = segment_sentiment_analysis_data_class_instance.to_dict()
# create an instance of SegmentSentimentAnalysisDataClass from a dict
segment_sentiment_analysis_data_class_form_dict = segment_sentiment_analysis_data_class.from_dict(segment_sentiment_analysis_data_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


