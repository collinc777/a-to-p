# AnonymizationBoundingBox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x_min** | **int** |  | 
**x_max** | **int** |  | 
**y_min** | **int** |  | 
**y_max** | **int** |  | 

## Example

```python
from openapi_client.models.anonymization_bounding_box import AnonymizationBoundingBox

# TODO update the JSON string below
json = "{}"
# create an instance of AnonymizationBoundingBox from a JSON string
anonymization_bounding_box_instance = AnonymizationBoundingBox.from_json(json)
# print the JSON string representation of the object
print(AnonymizationBoundingBox.to_json())

# convert the object into a dict
anonymization_bounding_box_dict = anonymization_bounding_box_instance.to_dict()
# create an instance of AnonymizationBoundingBox from a dict
anonymization_bounding_box_form_dict = anonymization_bounding_box.from_dict(anonymization_bounding_box_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


