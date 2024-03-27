# DocParserList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_name** | **str** | The project name | 
**structure_providers** | **Dict[str, object]** |  | [optional] 
**subfeature** | **str** |  | [readonly] 
**project_id** | **str** |  | [readonly] 

## Example

```python
from openapi_client.models.doc_parser_list import DocParserList

# TODO update the JSON string below
json = "{}"
# create an instance of DocParserList from a JSON string
doc_parser_list_instance = DocParserList.from_json(json)
# print the JSON string representation of the object
print(DocParserList.to_json())

# convert the object into a dict
doc_parser_list_dict = doc_parser_list_instance.to_dict()
# create an instance of DocParserList from a dict
doc_parser_list_form_dict = doc_parser_list.from_dict(doc_parser_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


