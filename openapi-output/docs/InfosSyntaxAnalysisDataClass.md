# InfosSyntaxAnalysisDataClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**word** | **str** |  | 
**importance** | **int** |  | 
**tag** | **str** |  | 
**lemma** | **str** |  | 
**others** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.infos_syntax_analysis_data_class import InfosSyntaxAnalysisDataClass

# TODO update the JSON string below
json = "{}"
# create an instance of InfosSyntaxAnalysisDataClass from a JSON string
infos_syntax_analysis_data_class_instance = InfosSyntaxAnalysisDataClass.from_json(json)
# print the JSON string representation of the object
print(InfosSyntaxAnalysisDataClass.to_json())

# convert the object into a dict
infos_syntax_analysis_data_class_dict = infos_syntax_analysis_data_class_instance.to_dict()
# create an instance of InfosSyntaxAnalysisDataClass from a dict
infos_syntax_analysis_data_class_form_dict = infos_syntax_analysis_data_class.from_dict(infos_syntax_analysis_data_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


