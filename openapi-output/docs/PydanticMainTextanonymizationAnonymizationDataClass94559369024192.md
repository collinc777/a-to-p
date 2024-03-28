# PydanticMainTextanonymizationAnonymizationDataClass94559369024192


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | 
**entities** | [**List[AnonymizationEntity]**](AnonymizationEntity.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**status** | [**StatusF43Enum**](StatusF43Enum.md) |  | 

## Example

```python
from openapi_client.models.pydantic_main_textanonymization_anonymization_data_class94559369024192 import PydanticMainTextanonymizationAnonymizationDataClass94559369024192

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainTextanonymizationAnonymizationDataClass94559369024192 from a JSON string
pydantic_main_textanonymization_anonymization_data_class94559369024192_instance = PydanticMainTextanonymizationAnonymizationDataClass94559369024192.from_json(json)
# print the JSON string representation of the object
print(PydanticMainTextanonymizationAnonymizationDataClass94559369024192.to_json())

# convert the object into a dict
pydantic_main_textanonymization_anonymization_data_class94559369024192_dict = pydantic_main_textanonymization_anonymization_data_class94559369024192_instance.to_dict()
# create an instance of PydanticMainTextanonymizationAnonymizationDataClass94559369024192 from a dict
pydantic_main_textanonymization_anonymization_data_class94559369024192_form_dict = pydantic_main_textanonymization_anonymization_data_class94559369024192.from_dict(pydantic_main_textanonymization_anonymization_data_class94559369024192_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


