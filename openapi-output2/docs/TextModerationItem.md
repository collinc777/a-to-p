# TextModerationItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**likelihood** | **int** |  | 
**category** | [**CategoryType**](CategoryType.md) |  | 
**subcategory** | [**Subcategory1**](Subcategory1.md) |  | 
**likelihood_score** | **int** |  | 

## Example

```python
from openapi_client.models.text_moderation_item import TextModerationItem

# TODO update the JSON string below
json = "{}"
# create an instance of TextModerationItem from a JSON string
text_moderation_item_instance = TextModerationItem.from_json(json)
# print the JSON string representation of the object
print(TextModerationItem.to_json())

# convert the object into a dict
text_moderation_item_dict = text_moderation_item_instance.to_dict()
# create an instance of TextModerationItem from a dict
text_moderation_item_form_dict = text_moderation_item.from_dict(text_moderation_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


