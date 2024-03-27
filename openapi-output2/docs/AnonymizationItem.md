# AnonymizationItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**confidence** | **int** |  | 
**bounding_boxes** | [**AnonymizationBoundingBox**](AnonymizationBoundingBox.md) |  | 

## Example

```python
from openapi_client.models.anonymization_item import AnonymizationItem

# TODO update the JSON string below
json = "{}"
# create an instance of AnonymizationItem from a JSON string
anonymization_item_instance = AnonymizationItem.from_json(json)
# print the JSON string representation of the object
print(AnonymizationItem.to_json())

# convert the object into a dict
anonymization_item_dict = anonymization_item_instance.to_dict()
# create an instance of AnonymizationItem from a dict
anonymization_item_form_dict = anonymization_item.from_dict(anonymization_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


