# ResumeWorkExp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_years_experience** | **str** |  | 
**entries** | [**List[ResumeWorkExpEntry]**](ResumeWorkExpEntry.md) |  | [optional] 

## Example

```python
from openapi_client.models.resume_work_exp import ResumeWorkExp

# TODO update the JSON string below
json = "{}"
# create an instance of ResumeWorkExp from a JSON string
resume_work_exp_instance = ResumeWorkExp.from_json(json)
# print the JSON string representation of the object
print(ResumeWorkExp.to_json())

# convert the object into a dict
resume_work_exp_dict = resume_work_exp_instance.to_dict()
# create an instance of ResumeWorkExp from a dict
resume_work_exp_form_dict = resume_work_exp.from_dict(resume_work_exp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


