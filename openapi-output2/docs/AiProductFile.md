# AiProductFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** |  | [readonly] 
**user** | **str** |  | [readonly] 
**project** | **str** |  | [readonly] 
**file_type** | **str** |  | 
**created_at** | **datetime** |  | [readonly] 
**status** | [**StatusE80Enum**](StatusE80Enum.md) |  | [optional] 

## Example

```python
from openapi_client.models.ai_product_file import AiProductFile

# TODO update the JSON string below
json = "{}"
# create an instance of AiProductFile from a JSON string
ai_product_file_instance = AiProductFile.from_json(json)
# print the JSON string representation of the object
print(AiProductFile.to_json())

# convert the object into a dict
ai_product_file_dict = ai_product_file_instance.to_dict()
# create an instance of AiProductFile from a dict
ai_product_file_form_dict = ai_product_file.from_dict(ai_product_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


