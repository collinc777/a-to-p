# AutomlClassificationListProjectsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projects** | [**List[AutomlClassificationProject]**](AutomlClassificationProject.md) |  | 

## Example

```python
from openapi_client.models.automl_classification_list_projects_response import AutomlClassificationListProjectsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutomlClassificationListProjectsResponse from a JSON string
automl_classification_list_projects_response_instance = AutomlClassificationListProjectsResponse.from_json(json)
# print the JSON string representation of the object
print(AutomlClassificationListProjectsResponse.to_json())

# convert the object into a dict
automl_classification_list_projects_response_dict = automl_classification_list_projects_response_instance.to_dict()
# create an instance of AutomlClassificationListProjectsResponse from a dict
automl_classification_list_projects_response_form_dict = automl_classification_list_projects_response.from_dict(automl_classification_list_projects_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


