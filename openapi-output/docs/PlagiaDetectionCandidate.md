# PlagiaDetectionCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**plagia_score** | **int** |  | 
**prediction** | **str** |  | 
**plagiarized_text** | **str** |  | 

## Example

```python
from openapi_client.models.plagia_detection_candidate import PlagiaDetectionCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of PlagiaDetectionCandidate from a JSON string
plagia_detection_candidate_instance = PlagiaDetectionCandidate.from_json(json)
# print the JSON string representation of the object
print(PlagiaDetectionCandidate.to_json())

# convert the object into a dict
plagia_detection_candidate_dict = plagia_detection_candidate_instance.to_dict()
# create an instance of PlagiaDetectionCandidate from a dict
plagia_detection_candidate_form_dict = plagia_detection_candidate.from_dict(plagia_detection_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


