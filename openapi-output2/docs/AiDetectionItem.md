# AiDetectionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**prediction** | **str** |  | 
**ai_score** | **int** |  | 
**ai_score_detail** | **int** |  | 

## Example

```python
from openapi_client.models.ai_detection_item import AiDetectionItem

# TODO update the JSON string below
json = "{}"
# create an instance of AiDetectionItem from a JSON string
ai_detection_item_instance = AiDetectionItem.from_json(json)
# print the JSON string representation of the object
print(AiDetectionItem.to_json())

# convert the object into a dict
ai_detection_item_dict = ai_detection_item_instance.to_dict()
# create an instance of AiDetectionItem from a dict
ai_detection_item_form_dict = ai_detection_item.from_dict(ai_detection_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


