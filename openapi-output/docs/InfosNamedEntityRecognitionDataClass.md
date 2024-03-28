# InfosNamedEntityRecognitionDataClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** |  | 
**category** | **str** |  | 
**importance** | **int** |  | 

## Example

```python
from openapi_client.models.infos_named_entity_recognition_data_class import InfosNamedEntityRecognitionDataClass

# TODO update the JSON string below
json = "{}"
# create an instance of InfosNamedEntityRecognitionDataClass from a JSON string
infos_named_entity_recognition_data_class_instance = InfosNamedEntityRecognitionDataClass.from_json(json)
# print the JSON string representation of the object
print(InfosNamedEntityRecognitionDataClass.to_json())

# convert the object into a dict
infos_named_entity_recognition_data_class_dict = infos_named_entity_recognition_data_class_instance.to_dict()
# create an instance of InfosNamedEntityRecognitionDataClass from a dict
infos_named_entity_recognition_data_class_form_dict = infos_named_entity_recognition_data_class.from_dict(infos_named_entity_recognition_data_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


