# TextquestionAnswerResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenstorrent** | [**PydanticMainTextquestionAnswerQuestionAnswerDataClass94559368992208**](PydanticMainTextquestionAnswerQuestionAnswerDataClass94559368992208.md) |  | [optional] 
**huggingface** | [**PydanticMainTextquestionAnswerQuestionAnswerDataClass94559369027328**](PydanticMainTextquestionAnswerQuestionAnswerDataClass94559369027328.md) |  | [optional] 
**openai** | [**PydanticMainTextquestionAnswerQuestionAnswerDataClass94559368883120**](PydanticMainTextquestionAnswerQuestionAnswerDataClass94559368883120.md) |  | [optional] 
**eden_ai** | [**PydanticMainTextquestionAnswerQuestionAnswerDataClass94559363483456**](PydanticMainTextquestionAnswerQuestionAnswerDataClass94559363483456.md) |  | [optional] 

## Example

```python
from openapi_client.models.textquestion_answer_response_model import TextquestionAnswerResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TextquestionAnswerResponseModel from a JSON string
textquestion_answer_response_model_instance = TextquestionAnswerResponseModel.from_json(json)
# print the JSON string representation of the object
print(TextquestionAnswerResponseModel.to_json())

# convert the object into a dict
textquestion_answer_response_model_dict = textquestion_answer_response_model_instance.to_dict()
# create an instance of TextquestionAnswerResponseModel from a dict
textquestion_answer_response_model_form_dict = textquestion_answer_response_model.from_dict(textquestion_answer_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


