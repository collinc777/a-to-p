# NestedError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from openapi_client.models.nested_error import NestedError

# TODO update the JSON string below
json = "{}"
# create an instance of NestedError from a JSON string
nested_error_instance = NestedError.from_json(json)
# print the JSON string representation of the object
print(NestedError.to_json())

# convert the object into a dict
nested_error_dict = nested_error_instance.to_dict()
# create an instance of NestedError from a dict
nested_error_form_dict = nested_error.from_dict(nested_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


