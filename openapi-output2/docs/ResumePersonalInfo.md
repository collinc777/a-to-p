# ResumePersonalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**ResumePersonalName**](ResumePersonalName.md) |  | 
**address** | [**ResumeLocation**](ResumeLocation.md) |  | 
**self_summary** | **str** |  | 
**objective** | **str** |  | 
**date_of_birth** | **str** |  | 
**place_of_birth** | **str** |  | 
**phones** | **List[str]** |  | [optional] 
**mails** | **List[str]** |  | [optional] 
**urls** | **List[str]** |  | [optional] 
**fax** | **List[str]** |  | [optional] 
**current_profession** | **str** |  | 
**gender** | **str** |  | 
**nationality** | **str** |  | 
**martial_status** | **str** |  | 
**current_salary** | **str** |  | 

## Example

```python
from openapi_client.models.resume_personal_info import ResumePersonalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResumePersonalInfo from a JSON string
resume_personal_info_instance = ResumePersonalInfo.from_json(json)
# print the JSON string representation of the object
print(ResumePersonalInfo.to_json())

# convert the object into a dict
resume_personal_info_dict = resume_personal_info_instance.to_dict()
# create an instance of ResumePersonalInfo from a dict
resume_personal_info_form_dict = resume_personal_info.from_dict(resume_personal_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


