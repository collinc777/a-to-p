# ResumeExtractedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**personal_infos** | [**ResumePersonalInfo**](ResumePersonalInfo.md) |  | 
**education** | [**ResumeEducation**](ResumeEducation.md) |  | 
**work_experience** | [**ResumeWorkExp**](ResumeWorkExp.md) |  | 
**languages** | [**List[ResumeLang]**](ResumeLang.md) |  | [optional] 
**skills** | [**List[ResumeSkill]**](ResumeSkill.md) |  | [optional] 
**certifications** | [**List[ResumeSkill]**](ResumeSkill.md) |  | [optional] 
**courses** | [**List[ResumeSkill]**](ResumeSkill.md) |  | [optional] 
**publications** | [**List[ResumeSkill]**](ResumeSkill.md) |  | [optional] 
**interests** | [**List[ResumeSkill]**](ResumeSkill.md) |  | [optional] 

## Example

```python
from openapi_client.models.resume_extracted_data import ResumeExtractedData

# TODO update the JSON string below
json = "{}"
# create an instance of ResumeExtractedData from a JSON string
resume_extracted_data_instance = ResumeExtractedData.from_json(json)
# print the JSON string representation of the object
print(ResumeExtractedData.to_json())

# convert the object into a dict
resume_extracted_data_dict = resume_extracted_data_instance.to_dict()
# create an instance of ResumeExtractedData from a dict
resume_extracted_data_form_dict = resume_extracted_data.from_dict(resume_extracted_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


