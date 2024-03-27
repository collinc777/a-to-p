# LogoItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounding_poly** | [**LogoBoundingPoly**](LogoBoundingPoly.md) |  | 
**description** | **str** |  | 
**score** | **int** |  | 

## Example

```python
from openapi_client.models.logo_item import LogoItem

# TODO update the JSON string below
json = "{}"
# create an instance of LogoItem from a JSON string
logo_item_instance = LogoItem.from_json(json)
# print the JSON string representation of the object
print(LogoItem.to_json())

# convert the object into a dict
logo_item_dict = logo_item_instance.to_dict()
# create an instance of LogoItem from a dict
logo_item_form_dict = logo_item.from_dict(logo_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


