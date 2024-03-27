# LandmarkItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**confidence** | **int** |  | 
**bounding_box** | [**List[LandmarkVertice]**](LandmarkVertice.md) |  | [optional] 
**locations** | [**List[LandmarkLocation]**](LandmarkLocation.md) |  | [optional] 

## Example

```python
from openapi_client.models.landmark_item import LandmarkItem

# TODO update the JSON string below
json = "{}"
# create an instance of LandmarkItem from a JSON string
landmark_item_instance = LandmarkItem.from_json(json)
# print the JSON string representation of the object
print(LandmarkItem.to_json())

# convert the object into a dict
landmark_item_dict = landmark_item_instance.to_dict()
# create an instance of LandmarkItem from a dict
landmark_item_form_dict = landmark_item.from_dict(landmark_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


