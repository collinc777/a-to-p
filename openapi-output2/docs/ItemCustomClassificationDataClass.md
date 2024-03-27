# ItemCustomClassificationDataClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **str** |  | 
**label** | **str** |  | 
**confidence** | **int** |  | 

## Example

```python
from openapi_client.models.item_custom_classification_data_class import ItemCustomClassificationDataClass

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCustomClassificationDataClass from a JSON string
item_custom_classification_data_class_instance = ItemCustomClassificationDataClass.from_json(json)
# print the JSON string representation of the object
print(ItemCustomClassificationDataClass.to_json())

# convert the object into a dict
item_custom_classification_data_class_dict = item_custom_classification_data_class_instance.to_dict()
# create an instance of ItemCustomClassificationDataClass from a dict
item_custom_classification_data_class_form_dict = item_custom_classification_data_class.from_dict(item_custom_classification_data_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


