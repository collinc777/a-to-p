# AutomlClassificationProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**name** | **str** |  | 
**provider** | **str** |  | 

## Example

```python
from openapi_client.models.automl_classification_project import AutomlClassificationProject

# TODO update the JSON string below
json = "{}"
# create an instance of AutomlClassificationProject from a JSON string
automl_classification_project_instance = AutomlClassificationProject.from_json(json)
# print the JSON string representation of the object
print(AutomlClassificationProject.to_json())

# convert the object into a dict
automl_classification_project_dict = automl_classification_project_instance.to_dict()
# create an instance of AutomlClassificationProject from a dict
automl_classification_project_form_dict = automl_classification_project.from_dict(automl_classification_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


