# TextsyntaxAnalysisResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ibm** | [**PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368818080**](PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368818080.md) |  | [optional] 
**emvista** | [**PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368302160**](PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368302160.md) |  | [optional] 
**google** | [**PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559367918032**](PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559367918032.md) |  | [optional] 
**amazon** | [**PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368306288**](PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368306288.md) |  | [optional] 
**lettria** | [**PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559367905728**](PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559367905728.md) |  | [optional] 
**eden_ai** | [**PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368788272**](PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368788272.md) |  | [optional] 

## Example

```python
from openapi_client.models.textsyntax_analysis_response_model import TextsyntaxAnalysisResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TextsyntaxAnalysisResponseModel from a JSON string
textsyntax_analysis_response_model_instance = TextsyntaxAnalysisResponseModel.from_json(json)
# print the JSON string representation of the object
print(TextsyntaxAnalysisResponseModel.to_json())

# convert the object into a dict
textsyntax_analysis_response_model_dict = textsyntax_analysis_response_model_instance.to_dict()
# create an instance of TextsyntaxAnalysisResponseModel from a dict
textsyntax_analysis_response_model_form_dict = textsyntax_analysis_response_model.from_dict(textsyntax_analysis_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


