# AskYourDataProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | **str** | The credential resource name | [optional] 
**asset** | **str** | The asset sub_resource name | [optional] 
**ocr_provider** | **str** |  | 
**speech_to_text_provider** | **str** |  | 
**llm_provider** | **str** | Select a default LLM provider to use in your project. | [optional] 
**llm_model** | **str** | Select a default Model for LLM provider to use in your project | [optional] 
**chunk_size** | **int** |  | [optional] 
**chunk_separators** | **List[str]** |  | [optional] 
**project_name** | **str** | Project name | 
**collection_name** | **str** | Database Collection Name | 
**db_provider** | [**DbProviderEnum**](DbProviderEnum.md) | Database Provider  * &#x60;qdrant&#x60; - qdrant * &#x60;supabase&#x60; - supabase | [optional] 
**embeddings_provider** | **str** | Select an embedding provider to use in your search database. Leave empty for default. | [optional] [default to 'cohere']

## Example

```python
from openapi_client.models.ask_your_data_project_request import AskYourDataProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AskYourDataProjectRequest from a JSON string
ask_your_data_project_request_instance = AskYourDataProjectRequest.from_json(json)
# print the JSON string representation of the object
print(AskYourDataProjectRequest.to_json())

# convert the object into a dict
ask_your_data_project_request_dict = ask_your_data_project_request_instance.to_dict()
# create an instance of AskYourDataProjectRequest from a dict
ask_your_data_project_request_form_dict = ask_your_data_project_request.from_dict(ask_your_data_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


