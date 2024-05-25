# abha.AbdmLinkTokenApi

All URIs are relative to *https://healthidsbx.abdm.gov.in/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abdm_link_token_1**](AbdmLinkTokenApi.md#abdm_link_token_1) | **POST** /v3/token/generate-token | API used to generate link token


# **abdm_link_token_1**
> abdm_link_token_1(abdm_link_token1_request)

API used to generate link token

This is an API used to generate a link token of maximum validity [6 months], which can be used for HIP Initiated Linking.

### Example


```python
import abha
from abha.models.abdm_link_token1_request import AbdmLinkToken1Request
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://healthidsbx.abdm.gov.in/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "https://healthidsbx.abdm.gov.in/api/v1"
)


# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.AbdmLinkTokenApi(api_client)
    abdm_link_token1_request = abha.AbdmLinkToken1Request() # AbdmLinkToken1Request | 

    try:
        # API used to generate link token
        api_instance.abdm_link_token_1(abdm_link_token1_request)
    except Exception as e:
        print("Exception when calling AbdmLinkTokenApi->abdm_link_token_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **abdm_link_token1_request** | [**AbdmLinkToken1Request**](AbdmLinkToken1Request.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | server cannot find the requested resource |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

