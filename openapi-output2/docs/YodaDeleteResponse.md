# YodaDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'Done!']

## Example

```python
from openapi_client.models.yoda_delete_response import YodaDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of YodaDeleteResponse from a JSON string
yoda_delete_response_instance = YodaDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(YodaDeleteResponse.to_json())

# convert the object into a dict
yoda_delete_response_dict = yoda_delete_response_instance.to_dict()
# create an instance of YodaDeleteResponse from a dict
yoda_delete_response_form_dict = yoda_delete_response.from_dict(yoda_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


