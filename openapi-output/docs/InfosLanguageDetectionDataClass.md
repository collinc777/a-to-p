# InfosLanguageDetectionDataClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** |  | 
**display_name** | **str** |  | 
**confidence** | **int** |  | 

## Example

```python
from openapi_client.models.infos_language_detection_data_class import InfosLanguageDetectionDataClass

# TODO update the JSON string below
json = "{}"
# create an instance of InfosLanguageDetectionDataClass from a JSON string
infos_language_detection_data_class_instance = InfosLanguageDetectionDataClass.from_json(json)
# print the JSON string representation of the object
print(InfosLanguageDetectionDataClass.to_json())

# convert the object into a dict
infos_language_detection_data_class_dict = infos_language_detection_data_class_instance.to_dict()
# create an instance of InfosLanguageDetectionDataClass from a dict
infos_language_detection_data_class_form_dict = infos_language_detection_data_class.from_dict(infos_language_detection_data_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


