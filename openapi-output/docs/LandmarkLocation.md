# LandmarkLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat_lng** | [**LandmarkLatLng**](LandmarkLatLng.md) |  | 

## Example

```python
from openapi_client.models.landmark_location import LandmarkLocation

# TODO update the JSON string below
json = "{}"
# create an instance of LandmarkLocation from a JSON string
landmark_location_instance = LandmarkLocation.from_json(json)
# print the JSON string representation of the object
print(LandmarkLocation.to_json())

# convert the object into a dict
landmark_location_dict = landmark_location_instance.to_dict()
# create an instance of LandmarkLocation from a dict
landmark_location_form_dict = landmark_location.from_dict(landmark_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


