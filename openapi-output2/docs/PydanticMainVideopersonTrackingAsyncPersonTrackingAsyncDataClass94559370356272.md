# PydanticMainVideopersonTrackingAsyncPersonTrackingAsyncDataClass94559370356272


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**persons** | [**List[VideoTrackingPerson]**](VideoTrackingPerson.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**id** | **str** |  | 
**final_status** | [**FinalStatusEnum**](FinalStatusEnum.md) |  | 
**error** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.pydantic_main_videoperson_tracking_async_person_tracking_async_data_class94559370356272 import PydanticMainVideopersonTrackingAsyncPersonTrackingAsyncDataClass94559370356272

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainVideopersonTrackingAsyncPersonTrackingAsyncDataClass94559370356272 from a JSON string
pydantic_main_videoperson_tracking_async_person_tracking_async_data_class94559370356272_instance = PydanticMainVideopersonTrackingAsyncPersonTrackingAsyncDataClass94559370356272.from_json(json)
# print the JSON string representation of the object
print(PydanticMainVideopersonTrackingAsyncPersonTrackingAsyncDataClass94559370356272.to_json())

# convert the object into a dict
pydantic_main_videoperson_tracking_async_person_tracking_async_data_class94559370356272_dict = pydantic_main_videoperson_tracking_async_person_tracking_async_data_class94559370356272_instance.to_dict()
# create an instance of PydanticMainVideopersonTrackingAsyncPersonTrackingAsyncDataClass94559370356272 from a dict
pydantic_main_videoperson_tracking_async_person_tracking_async_data_class94559370356272_form_dict = pydantic_main_videoperson_tracking_async_person_tracking_async_data_class94559370356272.from_dict(pydantic_main_videoperson_tracking_async_person_tracking_async_data_class94559370356272_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


