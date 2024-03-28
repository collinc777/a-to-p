# openapi_client.WorkflowsApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pipeline_pipeline_create**](WorkflowsApi.md#pipeline_pipeline_create) | **POST** /pipeline/ | Launch a Workflow


# **pipeline_pipeline_create**
> WorklowResponseType pipeline_pipeline_create(description, text=text, texts=texts, file=file, return_only_last=return_only_last)

Launch a Workflow

 Workflow let you create a pipeline of subfeature by inputing an entry data, letting it pass through all the subfeatures and retreiving the result   **Note**: You can try Workflow on our [developer portal](https://app.edenai.run/bricks/workflows) and a `description` snippet will automatically get generated as you build your workflow  **Example:**  Schema: ocr --> automatic_translation --> summarize In this workflow we pass a file as input, ocr parse the text, pass it to translate, and summarize will return a summary of the translated text  **Inputs:**  Depending on the first subfeature you have three choice for the inital input data: `file`, `text` or `texts`.  To create a workflow you have to pass an object to the `description` parameter, the object should look like this:   ``` [   {     \"feature\": \"ocr\",     \"subfeature\": \"ocr\",     \"params\": {       \"language\": \"auto-detect\",       \"providers\": \"google\"     }   },   {     \"feature\": \"translation\",     \"subfeature\": \"automatic_translation\",     \"params\": {       \"source_language\": \"auto-detect\",       \"target_language\": \"fr\",       \"providers\": \"google\"     }   },   {     \"feature\": \"text\",     \"subfeature\": \"summarize\",     \"params\": {       \"providers\": \"openai\"     }   } ] ```  - `description` should be a list of *nodes* each node representing a subfeature.Inside each node, enter the desired feature and subfeature and its params. `params` are the parameters you should normally send to the subfeature as if you were doing a direct call but with a few constraints:     + `providers` should take only one provider name, if you input multiple providers, the response of all the other providers will be ignored     + `file`, `text`, `texts` shouldn't be present in `params` as these are initial inputs  **Important!**: description should be sent as a string since the content-type is a form-data  - `return_only_last` allows you to chose wether you want a list of all the response returned by each providers or just getting the last response. If set to `true` the response will be the last subfeature result, if set to `false` the reponse will be a list of all subfeature results.     

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.worklow_response_type import WorklowResponseType
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.edenai.run/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.edenai.run/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): FeatureApiAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WorkflowsApi(api_client)
    description = 'description_example' # str | 
    text = 'text_example' # str | The input text for the first feature of the pipeline (optional)
    texts = 'texts_example' # str | List of texts for the first feature of the pipeline (optional)
    file = None # bytearray | The input file for the first feature of the pipeline (optional)
    return_only_last = True # bool | This parameter allows user to choose to output only the final result or all the intermediate results. (optional) (default to True)

    try:
        # Launch a Workflow
        api_response = await api_instance.pipeline_pipeline_create(description, text=text, texts=texts, file=file, return_only_last=return_only_last)
        print("The response of WorkflowsApi->pipeline_pipeline_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->pipeline_pipeline_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**|  | 
 **text** | **str**| The input text for the first feature of the pipeline | [optional] 
 **texts** | **str**| List of texts for the first feature of the pipeline | [optional] 
 **file** | **bytearray**| The input file for the first feature of the pipeline | [optional] 
 **return_only_last** | **bool**| This parameter allows user to choose to output only the final result or all the intermediate results. | [optional] [default to True]

### Return type

[**WorklowResponseType**](WorklowResponseType.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

