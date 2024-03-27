# ImageanonymizationAnonymizationDataClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** |  | 
**image_resource_url** | **str** |  | 
**items** | [**List[AnonymizationItem]**](AnonymizationItem.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**status** | [**StatusF43Enum**](StatusF43Enum.md) |  | 

## Example

```python
from openapi_client.models.imageanonymization_anonymization_data_class import ImageanonymizationAnonymizationDataClass

# TODO update the JSON string below
json = "{}"
# create an instance of ImageanonymizationAnonymizationDataClass from a JSON string
imageanonymization_anonymization_data_class_instance = ImageanonymizationAnonymizationDataClass.from_json(json)
# print the JSON string representation of the object
print(ImageanonymizationAnonymizationDataClass.to_json())

# convert the object into a dict
imageanonymization_anonymization_data_class_dict = imageanonymization_anonymization_data_class_instance.to_dict()
# create an instance of ImageanonymizationAnonymizationDataClass from a dict
imageanonymization_anonymization_data_class_form_dict = imageanonymization_anonymization_data_class.from_dict(imageanonymization_anonymization_data_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


