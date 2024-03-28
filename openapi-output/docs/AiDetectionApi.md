# openapi_client.AiDetectionApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_text_ai_detection_create**](AiDetectionApi.md#text_text_ai_detection_create) | **POST** /text/ai_detection | AI Content Detection


# **text_text_ai_detection_create**
> TextaiDetectionResponseModel text_text_ai_detection_create(textai_detection_ai_detection_request)

AI Content Detection

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**originalityai**|`v1`|0.01 (per 400 char)|400 char |**sapling**|`v1`|5.0 (per 1000000 char)|1000 char |**winstonai**|`v2`|14.0 (per 1000000 char)|1 char   </details>  <details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`|  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textai_detection_ai_detection_request import TextaiDetectionAiDetectionRequest
from openapi_client.models.textai_detection_response_model import TextaiDetectionResponseModel
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
    api_instance = openapi_client.AiDetectionApi(api_client)
    textai_detection_ai_detection_request = {"providers":"sapling,winstonai,originalityai","text":"The panther, also known as the black panther, is a magnificent and enigmatic creature that captivates the imagination of many. It is not a distinct species itself, but rather a melanistic variant of leopards and jaguars. The mesmerizing black coat of the panther is a result of a genetic mutation that increases the production of dark pigment, melanin.         Panthers are highly adaptable predators, found primarily in dense forests and jungles across Africa, Asia, and the Americas. Their stealthy nature and exceptional agility make them formidable hunters. They are solitary creatures, preferring to roam alone in their vast territories, which can span over a hundred square miles.         Equipped with incredible strength and sharp retractable claws, panthers are skilled climbers and swimmers. Their keen senses, including sharp vision and acute hearing, aid them in locating prey, often stalking their victims from the cover of trees or thick underbrush before launching a precise and powerful attack.         The diet of a panther consists mainly of deer, wild boar, and smaller mammals. However, they are opportunistic hunters and can also target livestock and domestic animals in areas where their habitats overlap with human settlements. Unfortunately, this sometimes leads to conflicts with humans, resulting in the panther being perceived as a threat.         Despite their association with darkness and mystery, panthers play a vital role in maintaining the balance of ecosystems. As apex predators, they help control populations of herbivores, preventing overgrazing and maintaining healthy prey dynamics.         Conservation efforts are crucial to the survival of panther populations worldwide. Habitat loss, poaching, and illegal wildlife trade pose significant threats to their existence. Various organizations and governments are working tirelessly to protect these magnificent creatures through initiatives such as establishing protected areas, promoting sustainable land use practices, and raising awareness about their importance in the natural world."} # TextaiDetectionAiDetectionRequest | 

    try:
        # AI Content Detection
        api_response = await api_instance.text_text_ai_detection_create(textai_detection_ai_detection_request)
        print("The response of AiDetectionApi->text_text_ai_detection_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiDetectionApi->text_text_ai_detection_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **textai_detection_ai_detection_request** | [**TextaiDetectionAiDetectionRequest**](TextaiDetectionAiDetectionRequest.md)|  | 

### Return type

[**TextaiDetectionResponseModel**](TextaiDetectionResponseModel.md)

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

