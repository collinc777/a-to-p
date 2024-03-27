# ObjectTrack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**confidence** | **int** |  | 
**frames** | [**List[ObjectFrame]**](ObjectFrame.md) |  | [optional] 

## Example

```python
from openapi_client.models.object_track import ObjectTrack

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectTrack from a JSON string
object_track_instance = ObjectTrack.from_json(json)
# print the JSON string representation of the object
print(ObjectTrack.to_json())

# convert the object into a dict
object_track_dict = object_track_instance.to_dict()
# create an instance of ObjectTrack from a dict
object_track_form_dict = object_track.from_dict(object_track_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


