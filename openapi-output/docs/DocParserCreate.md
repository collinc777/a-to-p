# DocParserCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_name** | **str** | The project name | 
**structure_providers** | **Dict[str, object]** |  | [optional] 
**subfeature** | **str** |  | 

## Example

```python
from openapi_client.models.doc_parser_create import DocParserCreate

# TODO update the JSON string below
json = "{}"
# create an instance of DocParserCreate from a JSON string
doc_parser_create_instance = DocParserCreate.from_json(json)
# print the JSON string representation of the object
print(DocParserCreate.to_json())

# convert the object into a dict
doc_parser_create_dict = doc_parser_create_instance.to_dict()
# create an instance of DocParserCreate from a dict
doc_parser_create_form_dict = doc_parser_create.from_dict(doc_parser_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


