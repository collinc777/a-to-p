# ResumeEducation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_years_education** | **int** |  | 
**entries** | [**List[ResumeEducationEntry]**](ResumeEducationEntry.md) |  | [optional] 

## Example

```python
from openapi_client.models.resume_education import ResumeEducation

# TODO update the JSON string below
json = "{}"
# create an instance of ResumeEducation from a JSON string
resume_education_instance = ResumeEducation.from_json(json)
# print the JSON string representation of the object
print(ResumeEducation.to_json())

# convert the object into a dict
resume_education_dict = resume_education_instance.to_dict()
# create an instance of ResumeEducation from a dict
resume_education_form_dict = resume_education.from_dict(resume_education_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


