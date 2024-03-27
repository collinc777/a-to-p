# openapi_client.QuestionAnswerApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_image_question_answer_create**](QuestionAnswerApi.md#image_image_question_answer_create) | **POST** /image/question_answer | Question Answer
[**text_text_question_answer_create**](QuestionAnswerApi.md#text_text_question_answer_create) | **POST** /text/question_answer | Question Answer


# **image_image_question_answer_create**
> ImagequestionAnswerResponseModel image_image_question_answer_create(imagequestion_answer_question_answer_request)

Question Answer

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**alephalpha**|**luminous-base**|`1.12.0`|0.02 (per 1 request)|1 request |**alephalpha**|**luminous-extended**|`1.12.0`|0.03 (per 1 request)|1 request |**alephalpha**|-|`1.12.0`|0.03 (per 1 request)|1 request |**openai**|-|`v1`|0.02 (per 1 request)|1 request |**google**|-|`v1`|0.01 (per 1 request)|1 request   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**English**|`en`| |**French**|`fr`| |**German**|`de`| |**Italian**|`it`| |**Spanish**|`es`|  </details><details><summary>Supported Models</summary><details><summary>alephalpha</summary>      |Name|Value| |----|-----| |**alephalpha**|`luminous-base`| ||`luminous-extended`|  </details><details><summary>openai</summary>      |Name|Value| |----|-----| |**openai**|`gpt-4-vision-preview`|  </details><details><summary>google</summary>      |Name|Value| |----|-----| |**google**|`gemini-pro-vision`| ||`imagen`|  </details>  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imagequestion_answer_question_answer_request import ImagequestionAnswerQuestionAnswerRequest
from openapi_client.models.imagequestion_answer_response_model import ImagequestionAnswerResponseModel
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.QuestionAnswerApi(api_client)
    imagequestion_answer_question_answer_request = {"providers":"openai,google,alephalpha","question":"What are the logos on the image ?","temperature":0,"max_tokens":64,"file_url":"http://edenai-resource-example.jpg"} # ImagequestionAnswerQuestionAnswerRequest | 

    try:
        # Question Answer
        api_response = api_instance.image_image_question_answer_create(imagequestion_answer_question_answer_request)
        print("The response of QuestionAnswerApi->image_image_question_answer_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionAnswerApi->image_image_question_answer_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imagequestion_answer_question_answer_request** | [**ImagequestionAnswerQuestionAnswerRequest**](ImagequestionAnswerQuestionAnswerRequest.md)|  | 

### Return type

[**ImagequestionAnswerResponseModel**](ImagequestionAnswerResponseModel.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_text_question_answer_create**
> TextquestionAnswerResponseModel text_text_question_answer_create(textquestion_answer_question_answer_request)

Question Answer

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token |**tenstorrent**|`v1.0.0`|10.0 (per 1000000 char)|1000 char   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textquestion_answer_question_answer_request import TextquestionAnswerQuestionAnswerRequest
from openapi_client.models.textquestion_answer_response_model import TextquestionAnswerResponseModel
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.QuestionAnswerApi(api_client)
    textquestion_answer_question_answer_request = {"providers":"tenstorrent,openai","texts":["The bar-shouldered dove (Geopelia humeralis) is a species of dove, in the family Columbidae, native to Australia and southern New Guinea. Its typical habitat consists of areas of thick vegetation where water is present, damp gullies, forests and gorges, mangroves, plantations, swamps, eucalyptus woodland, tropical and sub-tropical shrubland, and river margins. It can be found in both inland and coastal regions."],"question":"What is the scientific name of bar-shouldered dove?","temperature":0,"examples_context":"In 2017, U.S. life expectancy was 78.6 years.","examples":[["What is human life expectancy in the United States?","78 years."]]} # TextquestionAnswerQuestionAnswerRequest | 

    try:
        # Question Answer
        api_response = api_instance.text_text_question_answer_create(textquestion_answer_question_answer_request)
        print("The response of QuestionAnswerApi->text_text_question_answer_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionAnswerApi->text_text_question_answer_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **textquestion_answer_question_answer_request** | [**TextquestionAnswerQuestionAnswerRequest**](TextquestionAnswerQuestionAnswerRequest.md)|  | 

### Return type

[**TextquestionAnswerResponseModel**](TextquestionAnswerResponseModel.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

