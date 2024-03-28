# ObjectItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**confidence** | **int** |  | 
**x_min** | **int** |  | 
**x_max** | **int** |  | 
**y_min** | **int** |  | 
**y_max** | **int** |  | 

## Example

```python
from openapi_client.models.object_item import ObjectItem

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectItem from a JSON string
object_item_instance = ObjectItem.from_json(json)
# print the JSON string representation of the object
print(ObjectItem.to_json())

# convert the object into a dict
object_item_dict = object_item_instance.to_dict()
# create an instance of ObjectItem from a dict
object_item_form_dict = object_item.from_dict(object_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


