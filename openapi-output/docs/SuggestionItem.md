# SuggestionItem

     Represents a suggestion for a misspelled word.      Args:         suggestion (str): The suggested text.         score (float, optional): The score of the suggested text (between 0 and 1).      Raises:         ValueError: If the score is not between 0 and 1.      Returns:         SuggestionItem: An instance of the SuggestionItem class.     

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggestion** | **str** |  | 
**score** | **int** |  | 

## Example

```python
from openapi_client.models.suggestion_item import SuggestionItem

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestionItem from a JSON string
suggestion_item_instance = SuggestionItem.from_json(json)
# print the JSON string representation of the object
print(SuggestionItem.to_json())

# convert the object into a dict
suggestion_item_dict = suggestion_item_instance.to_dict()
# create an instance of SuggestionItem from a dict
suggestion_item_form_dict = suggestion_item.from_dict(suggestion_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


