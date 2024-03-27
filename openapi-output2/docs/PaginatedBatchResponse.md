# PaginatedBatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total requests made | 
**current_page** | **int** | Current page number | 
**last_page** | **int** |  | 
**per_page** | **int** | Number of requests per page | 
**var_from** | **int** |  | 
**to** | **int** |  | 
**prev_page_url** | **str** |  | [optional] 
**next_page_url** | **str** |  | [optional] 
**requests** | [**List[BatchResponseRequest]**](BatchResponseRequest.md) |  | 
**status** | [**StatusE80Enum**](StatusE80Enum.md) |  | [optional] 
**created** | **datetime** |  | [readonly] 
**updated** | **datetime** |  | [readonly] 

## Example

```python
from openapi_client.models.paginated_batch_response import PaginatedBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBatchResponse from a JSON string
paginated_batch_response_instance = PaginatedBatchResponse.from_json(json)
# print the JSON string representation of the object
print(PaginatedBatchResponse.to_json())

# convert the object into a dict
paginated_batch_response_dict = paginated_batch_response_instance.to_dict()
# create an instance of PaginatedBatchResponse from a dict
paginated_batch_response_form_dict = paginated_batch_response.from_dict(paginated_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


