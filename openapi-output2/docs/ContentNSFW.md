# ContentNSFW


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** |  | 
**confidence** | **int** |  | 
**category** | **str** |  | 

## Example

```python
from openapi_client.models.content_nsfw import ContentNSFW

# TODO update the JSON string below
json = "{}"
# create an instance of ContentNSFW from a JSON string
content_nsfw_instance = ContentNSFW.from_json(json)
# print the JSON string representation of the object
print(ContentNSFW.to_json())

# convert the object into a dict
content_nsfw_dict = content_nsfw_instance.to_dict()
# create an instance of ContentNSFW from a dict
content_nsfw_form_dict = content_nsfw.from_dict(content_nsfw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


