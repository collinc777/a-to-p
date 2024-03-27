# SpellCheckItem

Represents a spell check item with suggestions.      Args:         text (str): The text to spell check.         type (str, optional): The type of the text.         offset (int): The offset of the text.         length (int): The length of the text.         suggestions (Sequence[SuggestionItem], optional): The list of suggestions for the misspelled text.      Raises:         ValueError: If the offset or length is not positive.      Returns:         SpellCheckItem: An instance of the SpellCheckItem class.     

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**type** | **str** |  | 
**offset** | **int** |  | 
**length** | **int** |  | 
**suggestions** | [**List[SuggestionItem]**](SuggestionItem.md) |  | [optional] 

## Example

```python
from openapi_client.models.spell_check_item import SpellCheckItem

# TODO update the JSON string below
json = "{}"
# create an instance of SpellCheckItem from a JSON string
spell_check_item_instance = SpellCheckItem.from_json(json)
# print the JSON string representation of the object
print(SpellCheckItem.to_json())

# convert the object into a dict
spell_check_item_dict = spell_check_item_instance.to_dict()
# create an instance of SpellCheckItem from a dict
spell_check_item_form_dict = spell_check_item.from_dict(spell_check_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


