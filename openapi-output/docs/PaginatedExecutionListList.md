# PaginatedExecutionListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ExecutionList]**](ExecutionList.md) |  | [optional] 

## Example

```python
from openapi_client.models.paginated_execution_list_list import PaginatedExecutionListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedExecutionListList from a JSON string
paginated_execution_list_list_instance = PaginatedExecutionListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedExecutionListList.to_json())

# convert the object into a dict
paginated_execution_list_list_dict = paginated_execution_list_list_instance.to_dict()
# create an instance of PaginatedExecutionListList from a dict
paginated_execution_list_list_form_dict = paginated_execution_list_list.from_dict(paginated_execution_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


