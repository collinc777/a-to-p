# Cell


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**row_index** | **int** |  | 
**col_index** | **int** |  | 
**row_span** | **int** |  | 
**col_span** | **int** |  | 
**confidence** | **int** |  | 
**bounding_box** | [**BoundixBoxOCRTable**](BoundixBoxOCRTable.md) |  | 
**is_header** | **bool** |  | [optional] [default to False]

## Example

```python
from openapi_client.models.cell import Cell

# TODO update the JSON string below
json = "{}"
# create an instance of Cell from a JSON string
cell_instance = Cell.from_json(json)
# print the JSON string representation of the object
print(Cell.to_json())

# convert the object into a dict
cell_dict = cell_instance.to_dict()
# create an instance of Cell from a dict
cell_form_dict = cell.from_dict(cell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


