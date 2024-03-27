# TextsyntaxAnalysisResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ibm** | [**PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368820224**](PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368820224.md) |  | [optional] 
**emvista** | [**PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559367951472**](PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559367951472.md) |  | [optional] 
**google** | [**PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368792608**](PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368792608.md) |  | [optional] 
**amazon** | [**PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368807376**](PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368807376.md) |  | [optional] 
**lettria** | [**PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368813120**](PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368813120.md) |  | [optional] 
**eden_ai** | [**PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368794976**](PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368794976.md) |  | [optional] 

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


