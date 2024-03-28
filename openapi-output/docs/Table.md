# Table


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[Row]**](Row.md) |  | [optional] 
**num_rows** | **int** |  | 
**num_cols** | **int** |  | 

## Example

```python
from openapi_client.models.table import Table

# TODO update the JSON string below
json = "{}"
# create an instance of Table from a JSON string
table_instance = Table.from_json(json)
# print the JSON string representation of the object
print(Table.to_json())

# convert the object into a dict
table_dict = table_instance.to_dict()
# create an instance of Table from a dict
table_form_dict = table.from_dict(table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


