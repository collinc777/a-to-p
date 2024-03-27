# AIProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [readonly] 
**project_name** | **str** |  | 
**project_type** | [**AIProjectProjectTypeEnum**](AIProjectProjectTypeEnum.md) |  | 
**created_at** | **datetime** |  | [readonly] 
**user** | **str** |  | 

## Example

```python
from openapi_client.models.ai_project import AIProject

# TODO update the JSON string below
json = "{}"
# create an instance of AIProject from a JSON string
ai_project_instance = AIProject.from_json(json)
# print the JSON string representation of the object
print(AIProject.to_json())

# convert the object into a dict
ai_project_dict = ai_project_instance.to_dict()
# create an instance of AIProject from a dict
ai_project_form_dict = ai_project.from_dict(ai_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


