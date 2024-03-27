# ResumePersonalName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**raw_name** | **str** |  | 
**middle** | **str** |  | 
**title** | **str** |  | 
**prefix** | **str** |  | 
**sufix** | **str** |  | 

## Example

```python
from openapi_client.models.resume_personal_name import ResumePersonalName

# TODO update the JSON string below
json = "{}"
# create an instance of ResumePersonalName from a JSON string
resume_personal_name_instance = ResumePersonalName.from_json(json)
# print the JSON string representation of the object
print(ResumePersonalName.to_json())

# convert the object into a dict
resume_personal_name_dict = resume_personal_name_instance.to_dict()
# create an instance of ResumePersonalName from a dict
resume_personal_name_form_dict = resume_personal_name.from_dict(resume_personal_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


