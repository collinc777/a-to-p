# ResumeLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formatted_location** | **str** |  | 
**postal_code** | **str** |  | 
**region** | **str** |  | 
**country** | **str** |  | 
**country_code** | **str** |  | 
**raw_input_location** | **str** |  | 
**street** | **str** |  | 
**street_number** | **str** |  | 
**appartment_number** | **str** |  | 
**city** | **str** |  | 

## Example

```python
from openapi_client.models.resume_location import ResumeLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ResumeLocation from a JSON string
resume_location_instance = ResumeLocation.from_json(json)
# print the JSON string representation of the object
print(ResumeLocation.to_json())

# convert the object into a dict
resume_location_dict = resume_location_instance.to_dict()
# create an instance of ResumeLocation from a dict
resume_location_form_dict = resume_location.from_dict(resume_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


