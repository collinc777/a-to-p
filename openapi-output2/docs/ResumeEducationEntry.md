# ResumeEducationEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**start_date** | **str** |  | 
**end_date** | **str** |  | 
**location** | [**ResumeLocation**](ResumeLocation.md) |  | 
**establishment** | **str** |  | 
**description** | **str** |  | 
**gpa** | **str** |  | 
**accreditation** | **str** |  | 

## Example

```python
from openapi_client.models.resume_education_entry import ResumeEducationEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ResumeEducationEntry from a JSON string
resume_education_entry_instance = ResumeEducationEntry.from_json(json)
# print the JSON string representation of the object
print(ResumeEducationEntry.to_json())

# convert the object into a dict
resume_education_entry_dict = resume_education_entry_instance.to_dict()
# create an instance of ResumeEducationEntry from a dict
resume_education_entry_form_dict = resume_education_entry.from_dict(resume_education_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


