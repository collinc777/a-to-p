# Country


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**alpha2** | **str** |  | 
**alpha3** | **str** |  | 
**confidence** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.country import Country

# TODO update the JSON string below
json = "{}"
# create an instance of Country from a JSON string
country_instance = Country.from_json(json)
# print the JSON string representation of the object
print(Country.to_json())

# convert the object into a dict
country_dict = country_instance.to_dict()
# create an instance of Country from a dict
country_form_dict = country.from_dict(country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


