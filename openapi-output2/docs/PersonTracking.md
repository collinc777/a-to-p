# PersonTracking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | 
**attributes** | [**PersonAttributes**](PersonAttributes.md) |  | [optional] 
**landmarks** | [**PersonLandmarks**](PersonLandmarks.md) |  | [optional] 
**poses** | [**VideoPersonPoses**](VideoPersonPoses.md) |  | [optional] 
**quality** | [**VideoPersonQuality**](VideoPersonQuality.md) |  | [optional] 
**bounding_box** | [**VideoTrackingBoundingBox**](VideoTrackingBoundingBox.md) |  | 

## Example

```python
from openapi_client.models.person_tracking import PersonTracking

# TODO update the JSON string below
json = "{}"
# create an instance of PersonTracking from a JSON string
person_tracking_instance = PersonTracking.from_json(json)
# print the JSON string representation of the object
print(PersonTracking.to_json())

# convert the object into a dict
person_tracking_dict = person_tracking_instance.to_dict()
# create an instance of PersonTracking from a dict
person_tracking_form_dict = person_tracking.from_dict(person_tracking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


