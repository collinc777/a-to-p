# openapi_client.InfosApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info_info_provider_subfeatures_list**](InfosApi.md#info_info_provider_subfeatures_list) | **GET** /info/provider_subfeatures | List Providers Subfeatures


# **info_info_provider_subfeatures_list**
> List[ProviderSubfeature] info_info_provider_subfeatures_list(feature__name=feature__name, gender=gender, is_working=is_working, language=language, phase__name=phase__name, provider__name=provider__name, subfeature__name=subfeature__name)

List Providers Subfeatures

List Provider and features relations : You can get a list of *all providers* for a *feature* or *all features* for a *given provider*.  You can have the detailed information on the **pricing**, **supported languages** as well as the **models** for providers who propose different models (eg: voice models available for a text to speech provider).  Example : If you want the detailed list of all providers that can analyse the sentiment of a text written in french, you'd need to set `feature__name=text`,  `subfeature__name=sentiment_analysis` and `languages=fr`.  Which will look like the following :   ```bash curl --request GET  https://api.edenai.run/v2/info/provider_subfeatures?subfeature__name=sentiment_analysis&feature__name=text&languages=fr ```

### Example


```python
import openapi_client
from openapi_client.models.provider_subfeature import ProviderSubfeature
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.edenai.run/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.edenai.run/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.InfosApi(api_client)
    feature__name = 'feature__name_example' # str |  (optional)
    gender = 'gender_example' # str | Accepts two values: either 'male' or 'female'. Used to                              filter models voices for the text_to_speech subfeature (optional)
    is_working = True # bool |  (optional)
    language = 'language_example' # str | languages [icontains] (optional)
    phase__name = 'phase__name_example' # str |  (optional)
    provider__name = 'provider__name_example' # str |  (optional)
    subfeature__name = 'subfeature__name_example' # str |  (optional)

    try:
        # List Providers Subfeatures
        api_response = api_instance.info_info_provider_subfeatures_list(feature__name=feature__name, gender=gender, is_working=is_working, language=language, phase__name=phase__name, provider__name=provider__name, subfeature__name=subfeature__name)
        print("The response of InfosApi->info_info_provider_subfeatures_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfosApi->info_info_provider_subfeatures_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature__name** | **str**|  | [optional] 
 **gender** | **str**| Accepts two values: either &#39;male&#39; or &#39;female&#39;. Used to                              filter models voices for the text_to_speech subfeature | [optional] 
 **is_working** | **bool**|  | [optional] 
 **language** | **str**| languages [icontains] | [optional] 
 **phase__name** | **str**|  | [optional] 
 **provider__name** | **str**|  | [optional] 
 **subfeature__name** | **str**|  | [optional] 

### Return type

[**List[ProviderSubfeature]**](ProviderSubfeature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

