# ItemLines


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**amount** | **int** |  | [optional] 
**unit_price** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.item_lines import ItemLines

# TODO update the JSON string below
json = "{}"
# create an instance of ItemLines from a JSON string
item_lines_instance = ItemLines.from_json(json)
# print the JSON string representation of the object
print(ItemLines.to_json())

# convert the object into a dict
item_lines_dict = item_lines_instance.to_dict()
# create an instance of ItemLines from a dict
item_lines_form_dict = item_lines.from_dict(item_lines_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


