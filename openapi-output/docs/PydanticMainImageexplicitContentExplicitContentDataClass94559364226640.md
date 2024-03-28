# PydanticMainImageexplicitContentExplicitContentDataClass94559364226640


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nsfw_likelihood** | **int** |  | 
**nsfw_likelihood_score** | **int** |  | 
**items** | [**List[ExplicitItem]**](ExplicitItem.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**status** | [**StatusF43Enum**](StatusF43Enum.md) |  | 

## Example

```python
from openapi_client.models.pydantic_main_imageexplicit_content_explicit_content_data_class94559364226640 import PydanticMainImageexplicitContentExplicitContentDataClass94559364226640

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainImageexplicitContentExplicitContentDataClass94559364226640 from a JSON string
pydantic_main_imageexplicit_content_explicit_content_data_class94559364226640_instance = PydanticMainImageexplicitContentExplicitContentDataClass94559364226640.from_json(json)
# print the JSON string representation of the object
print(PydanticMainImageexplicitContentExplicitContentDataClass94559364226640.to_json())

# convert the object into a dict
pydantic_main_imageexplicit_content_explicit_content_data_class94559364226640_dict = pydantic_main_imageexplicit_content_explicit_content_data_class94559364226640_instance.to_dict()
# create an instance of PydanticMainImageexplicitContentExplicitContentDataClass94559364226640 from a dict
pydantic_main_imageexplicit_content_explicit_content_data_class94559364226640_form_dict = pydantic_main_imageexplicit_content_explicit_content_data_class94559364226640.from_dict(pydantic_main_imageexplicit_content_explicit_content_data_class94559364226640_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


