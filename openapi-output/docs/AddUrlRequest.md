# AddUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | **List[str]** | Add multiple urls into the database, it loads all the text from HTML webpages into a document format. | 
**metadata** | **List[Dict[str, object]]** |  | [optional] [default to []]

## Example

```python
from openapi_client.models.add_url_request import AddUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddUrlRequest from a JSON string
add_url_request_instance = AddUrlRequest.from_json(json)
# print the JSON string representation of the object
print(AddUrlRequest.to_json())

# convert the object into a dict
add_url_request_dict = add_url_request_instance.to_dict()
# create an instance of AddUrlRequest from a dict
add_url_request_form_dict = add_url_request.from_dict(add_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


