# abha.HipLinkTokenApi

All URIs are relative to *https://healthidsbx.abdm.gov.in/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**link_token_1**](HipLinkTokenApi.md#link_token_1) | **POST** /[callback_url]/v3/hip/token/on-generate-token | This is a call back API of [{callback_url}/token/on-generate-token}]


# **link_token_1**
> link_token_1(link_token1_request)

This is a call back API of [{callback_url}/token/on-generate-token}]

This is a call back API of [{callback_url}/token/on-generate-token}] must be implemented at HIP.

### Example


```python
import abha
from abha.models.link_token1_request import LinkToken1Request
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
    api_instance = abha.HipLinkTokenApi(api_client)
    link_token1_request = abha.LinkToken1Request() # LinkToken1Request | 

    try:
        # This is a call back API of [{callback_url}/token/on-generate-token}]
        api_instance.link_token_1(link_token1_request)
    except Exception as e:
        print("Exception when calling HipLinkTokenApi->link_token_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_token1_request** | [**LinkToken1Request**](LinkToken1Request.md)|  | 

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

