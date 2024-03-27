# ExplicitItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**likelihood** | **int** |  | 
**likelihood_score** | **int** |  | 
**category** | [**CategoryType**](CategoryType.md) |  | 
**subcategory** | [**Subcategory1**](Subcategory1.md) |  | 

## Example

```python
from openapi_client.models.explicit_item import ExplicitItem

# TODO update the JSON string below
json = "{}"
# create an instance of ExplicitItem from a JSON string
explicit_item_instance = ExplicitItem.from_json(json)
# print the JSON string representation of the object
print(ExplicitItem.to_json())

# convert the object into a dict
explicit_item_dict = explicit_item_instance.to_dict()
# create an instance of ExplicitItem from a dict
explicit_item_form_dict = explicit_item.from_dict(explicit_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


