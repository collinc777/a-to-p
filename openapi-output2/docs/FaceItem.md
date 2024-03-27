# FaceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **int** |  | 
**landmarks** | [**FaceLandmarks**](FaceLandmarks.md) |  | 
**emotions** | [**FaceEmotions**](FaceEmotions.md) |  | 
**poses** | [**FacePoses**](FacePoses.md) |  | 
**age** | **int** |  | 
**gender** | **str** |  | 
**bounding_box** | [**FaceBoundingBox**](FaceBoundingBox.md) |  | 
**hair** | [**FaceHair**](FaceHair.md) |  | 
**facial_hair** | [**FaceFacialHair**](FaceFacialHair.md) |  | 
**quality** | [**FaceQuality**](FaceQuality.md) |  | 
**makeup** | [**FaceMakeup**](FaceMakeup.md) |  | 
**accessories** | [**FaceAccessories**](FaceAccessories.md) |  | 
**occlusions** | [**FaceOcclusions**](FaceOcclusions.md) |  | 
**features** | [**FaceFeatures**](FaceFeatures.md) |  | 

## Example

```python
from openapi_client.models.face_item import FaceItem

# TODO update the JSON string below
json = "{}"
# create an instance of FaceItem from a JSON string
face_item_instance = FaceItem.from_json(json)
# print the JSON string representation of the object
print(FaceItem.to_json())

# convert the object into a dict
face_item_dict = face_item_instance.to_dict()
# create an instance of FaceItem from a dict
face_item_form_dict = face_item.from_dict(face_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


