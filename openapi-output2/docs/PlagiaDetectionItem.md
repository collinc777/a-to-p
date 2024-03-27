# PlagiaDetectionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**candidates** | [**List[PlagiaDetectionCandidate]**](PlagiaDetectionCandidate.md) |  | [optional] 

## Example

```python
from openapi_client.models.plagia_detection_item import PlagiaDetectionItem

# TODO update the JSON string below
json = "{}"
# create an instance of PlagiaDetectionItem from a JSON string
plagia_detection_item_instance = PlagiaDetectionItem.from_json(json)
# print the JSON string representation of the object
print(PlagiaDetectionItem.to_json())

# convert the object into a dict
plagia_detection_item_dict = plagia_detection_item_instance.to_dict()
# create an instance of PlagiaDetectionItem from a dict
plagia_detection_item_form_dict = plagia_detection_item.from_dict(plagia_detection_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


