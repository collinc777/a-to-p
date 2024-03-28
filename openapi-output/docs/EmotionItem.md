# EmotionItem

This class is used in EmotionAnalysisDataClass to list emotion analysed.     Args:         - emotion (EmotionEnum): emotion of the text         - emotion_score (float): score of the emotion     

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emotion** | **str** |  | 
**emotion_score** | **int** |  | 

## Example

```python
from openapi_client.models.emotion_item import EmotionItem

# TODO update the JSON string below
json = "{}"
# create an instance of EmotionItem from a JSON string
emotion_item_instance = EmotionItem.from_json(json)
# print the JSON string representation of the object
print(EmotionItem.to_json())

# convert the object into a dict
emotion_item_dict = emotion_item_instance.to_dict()
# create an instance of EmotionItem from a dict
emotion_item_form_dict = emotion_item.from_dict(emotion_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


