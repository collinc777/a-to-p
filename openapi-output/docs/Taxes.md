# Taxes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxes** | **int** |  | [optional] 
**rate** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.taxes import Taxes

# TODO update the JSON string below
json = "{}"
# create an instance of Taxes from a JSON string
taxes_instance = Taxes.from_json(json)
# print the JSON string representation of the object
print(Taxes.to_json())

# convert the object into a dict
taxes_dict = taxes_instance.to_dict()
# create an instance of Taxes from a dict
taxes_form_dict = taxes.from_dict(taxes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


