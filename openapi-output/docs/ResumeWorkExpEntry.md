# ResumeWorkExpEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**start_date** | **str** |  | 
**end_date** | **str** |  | 
**company** | **str** |  | 
**location** | [**ResumeLocation**](ResumeLocation.md) |  | 
**description** | **str** |  | 
**industry** | **str** |  | 

## Example

```python
from openapi_client.models.resume_work_exp_entry import ResumeWorkExpEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ResumeWorkExpEntry from a JSON string
resume_work_exp_entry_instance = ResumeWorkExpEntry.from_json(json)
# print the JSON string representation of the object
print(ResumeWorkExpEntry.to_json())

# convert the object into a dict
resume_work_exp_entry_dict = resume_work_exp_entry_instance.to_dict()
# create an instance of ResumeWorkExpEntry from a dict
resume_work_exp_entry_form_dict = resume_work_exp_entry.from_dict(resume_work_exp_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


