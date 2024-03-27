# ImageautomlClassificationAutomlClassificationCreateProjectDataClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**project_id** | **str** |  | 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**status** | [**StatusF43Enum**](StatusF43Enum.md) |  | 

## Example

```python
from openapi_client.models.imageautoml_classification_automl_classification_create_project_data_class import ImageautomlClassificationAutomlClassificationCreateProjectDataClass

# TODO update the JSON string below
json = "{}"
# create an instance of ImageautomlClassificationAutomlClassificationCreateProjectDataClass from a JSON string
imageautoml_classification_automl_classification_create_project_data_class_instance = ImageautomlClassificationAutomlClassificationCreateProjectDataClass.from_json(json)
# print the JSON string representation of the object
print(ImageautomlClassificationAutomlClassificationCreateProjectDataClass.to_json())

# convert the object into a dict
imageautoml_classification_automl_classification_create_project_data_class_dict = imageautoml_classification_automl_classification_create_project_data_class_instance.to_dict()
# create an instance of ImageautomlClassificationAutomlClassificationCreateProjectDataClass from a dict
imageautoml_classification_automl_classification_create_project_data_class_form_dict = imageautoml_classification_automl_classification_create_project_data_class.from_dict(imageautoml_classification_automl_classification_create_project_data_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


