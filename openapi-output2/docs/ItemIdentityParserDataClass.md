# ItemIdentityParserDataClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**confidence** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.item_identity_parser_data_class import ItemIdentityParserDataClass

# TODO update the JSON string below
json = "{}"
# create an instance of ItemIdentityParserDataClass from a JSON string
item_identity_parser_data_class_instance = ItemIdentityParserDataClass.from_json(json)
# print the JSON string representation of the object
print(ItemIdentityParserDataClass.to_json())

# convert the object into a dict
item_identity_parser_data_class_dict = item_identity_parser_data_class_instance.to_dict()
# create an instance of ItemIdentityParserDataClass from a dict
item_identity_parser_data_class_form_dict = item_identity_parser_data_class.from_dict(item_identity_parser_data_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


