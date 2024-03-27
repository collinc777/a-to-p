# BatchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**status** | [**StatusE80Enum**](StatusE80Enum.md) |  | [optional] 
**feature** | **str** |  | [readonly] 
**subfeature** | **str** |  | [readonly] 
**total_requests** | **int** |  | [readonly] 
**nb_processing** | **int** |  | [readonly] 
**nb_succeeded** | **int** |  | [readonly] 
**nb_failed** | **int** |  | [readonly] 
**get_response_url** | **str** |  | [readonly] 

## Example

```python
from openapi_client.models.batch_list import BatchList

# TODO update the JSON string below
json = "{}"
# create an instance of BatchList from a JSON string
batch_list_instance = BatchList.from_json(json)
# print the JSON string representation of the object
print(BatchList.to_json())

# convert the object into a dict
batch_list_dict = batch_list_instance.to_dict()
# create an instance of BatchList from a dict
batch_list_form_dict = batch_list.from_dict(batch_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


