# MicrModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw** | **str** |  | 
**account_number** | **str** |  | 
**routing_number** | **str** |  | 
**serial_number** | **str** |  | 
**check_number** | **str** |  | 

## Example

```python
from openapi_client.models.micr_model import MicrModel

# TODO update the JSON string below
json = "{}"
# create an instance of MicrModel from a JSON string
micr_model_instance = MicrModel.from_json(json)
# print the JSON string representation of the object
print(MicrModel.to_json())

# convert the object into a dict
micr_model_dict = micr_model_instance.to_dict()
# create an instance of MicrModel from a dict
micr_model_form_dict = micr_model.from_dict(micr_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


