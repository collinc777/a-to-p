# DocParserUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_name** | **str** | The project name | [readonly] 
**structure_providers** | **Dict[str, object]** |  | [optional] 
**subfeature** | **str** |  | [readonly] 

## Example

```python
from openapi_client.models.doc_parser_update import DocParserUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of DocParserUpdate from a JSON string
doc_parser_update_instance = DocParserUpdate.from_json(json)
# print the JSON string representation of the object
print(DocParserUpdate.to_json())

# convert the object into a dict
doc_parser_update_dict = doc_parser_update_instance.to_dict()
# create an instance of DocParserUpdate from a dict
doc_parser_update_form_dict = doc_parser_update.from_dict(doc_parser_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


