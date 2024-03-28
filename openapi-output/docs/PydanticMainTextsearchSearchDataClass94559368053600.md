# PydanticMainTextsearchSearchDataClass94559368053600


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[InfosSearchDataClass]**](InfosSearchDataClass.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**status** | [**StatusF43Enum**](StatusF43Enum.md) |  | 

## Example

```python
from openapi_client.models.pydantic_main_textsearch_search_data_class94559368053600 import PydanticMainTextsearchSearchDataClass94559368053600

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainTextsearchSearchDataClass94559368053600 from a JSON string
pydantic_main_textsearch_search_data_class94559368053600_instance = PydanticMainTextsearchSearchDataClass94559368053600.from_json(json)
# print the JSON string representation of the object
print(PydanticMainTextsearchSearchDataClass94559368053600.to_json())

# convert the object into a dict
pydantic_main_textsearch_search_data_class94559368053600_dict = pydantic_main_textsearch_search_data_class94559368053600_instance.to_dict()
# create an instance of PydanticMainTextsearchSearchDataClass94559368053600 from a dict
pydantic_main_textsearch_search_data_class94559368053600_form_dict = pydantic_main_textsearch_search_data_class94559368053600.from_dict(pydantic_main_textsearch_search_data_class94559368053600_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


