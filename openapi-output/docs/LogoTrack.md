# LogoTrack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**tracking** | [**List[VideoLogo]**](VideoLogo.md) |  | [optional] 

## Example

```python
from openapi_client.models.logo_track import LogoTrack

# TODO update the JSON string below
json = "{}"
# create an instance of LogoTrack from a JSON string
logo_track_instance = LogoTrack.from_json(json)
# print the JSON string representation of the object
print(LogoTrack.to_json())

# convert the object into a dict
logo_track_dict = logo_track_instance.to_dict()
# create an instance of LogoTrack from a dict
logo_track_form_dict = logo_track.from_dict(logo_track_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


