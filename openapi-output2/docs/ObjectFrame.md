# ObjectFrame


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** |  | 
**bounding_box** | [**VideoObjectBoundingBox**](VideoObjectBoundingBox.md) |  | 

## Example

```python
from openapi_client.models.object_frame import ObjectFrame

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectFrame from a JSON string
object_frame_instance = ObjectFrame.from_json(json)
# print the JSON string representation of the object
print(ObjectFrame.to_json())

# convert the object into a dict
object_frame_dict = object_frame_instance.to_dict()
# create an instance of ObjectFrame from a dict
object_frame_form_dict = object_frame.from_dict(object_frame_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


