# PydanticMainTextemotionDetectionEmotionDetectionDataClass94559370079616


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**items** | [**List[EmotionItem]**](EmotionItem.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**status** | [**StatusF43Enum**](StatusF43Enum.md) |  | 

## Example

```python
from openapi_client.models.pydantic_main_textemotion_detection_emotion_detection_data_class94559370079616 import PydanticMainTextemotionDetectionEmotionDetectionDataClass94559370079616

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainTextemotionDetectionEmotionDetectionDataClass94559370079616 from a JSON string
pydantic_main_textemotion_detection_emotion_detection_data_class94559370079616_instance = PydanticMainTextemotionDetectionEmotionDetectionDataClass94559370079616.from_json(json)
# print the JSON string representation of the object
print(PydanticMainTextemotionDetectionEmotionDetectionDataClass94559370079616.to_json())

# convert the object into a dict
pydantic_main_textemotion_detection_emotion_detection_data_class94559370079616_dict = pydantic_main_textemotion_detection_emotion_detection_data_class94559370079616_instance.to_dict()
# create an instance of PydanticMainTextemotionDetectionEmotionDetectionDataClass94559370079616 from a dict
pydantic_main_textemotion_detection_emotion_detection_data_class94559370079616_form_dict = pydantic_main_textemotion_detection_emotion_detection_data_class94559370079616.from_dict(pydantic_main_textemotion_detection_emotion_detection_data_class94559370079616_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


