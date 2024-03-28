# NestedBadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**message** | [**FieldError**](FieldError.md) |  | 

## Example

```python
from openapi_client.models.nested_bad_request import NestedBadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NestedBadRequest from a JSON string
nested_bad_request_instance = NestedBadRequest.from_json(json)
# print the JSON string representation of the object
print(NestedBadRequest.to_json())

# convert the object into a dict
nested_bad_request_dict = nested_bad_request_instance.to_dict()
# create an instance of NestedBadRequest from a dict
nested_bad_request_form_dict = nested_bad_request.from_dict(nested_bad_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


