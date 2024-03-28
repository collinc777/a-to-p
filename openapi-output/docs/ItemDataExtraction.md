# ItemDataExtraction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | **object** |  | 
**bounding_box** | [**BoundingBox**](BoundingBox.md) |  | 
**confidence_score** | **int** |  | 

## Example

```python
from openapi_client.models.item_data_extraction import ItemDataExtraction

# TODO update the JSON string below
json = "{}"
# create an instance of ItemDataExtraction from a JSON string
item_data_extraction_instance = ItemDataExtraction.from_json(json)
# print the JSON string representation of the object
print(ItemDataExtraction.to_json())

# convert the object into a dict
item_data_extraction_dict = item_data_extraction_instance.to_dict()
# create an instance of ItemDataExtraction from a dict
item_data_extraction_form_dict = item_data_extraction.from_dict(item_data_extraction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


