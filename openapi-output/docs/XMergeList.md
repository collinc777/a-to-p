# XMergeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_name** | **str** |  | [readonly] 
**project_type** | [**XMergeListProjectTypeEnum**](XMergeListProjectTypeEnum.md) |  | 
**created** | **datetime** |  | [readonly] 
**subfeature** | **str** |  | [readonly] 
**project_id** | **str** |  | [readonly] 

## Example

```python
from openapi_client.models.x_merge_list import XMergeList

# TODO update the JSON string below
json = "{}"
# create an instance of XMergeList from a JSON string
x_merge_list_instance = XMergeList.from_json(json)
# print the JSON string representation of the object
print(XMergeList.to_json())

# convert the object into a dict
x_merge_list_dict = x_merge_list_instance.to_dict()
# create an instance of XMergeList from a dict
x_merge_list_form_dict = x_merge_list.from_dict(x_merge_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


