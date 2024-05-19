# abha.SearchApi

All URIs are relative to *http://healthidsbx.abdm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_user_by_account_using_post**](SearchApi.md#search_user_by_account_using_post) | **POST** /v1/search/searchByHealthId | Search a user by ABHA Number or ABHA Address. This API returns only Active or Deactive ABHA Number/ Address (Never returns Permanently Deleted ABHA Number/ Address)
[**search_user_by_mobile_using_post**](SearchApi.md#search_user_by_mobile_using_post) | **POST** /v1/search/searchByMobile | Search users with a mobile number
[**search_user_by_userid_using_post**](SearchApi.md#search_user_by_userid_using_post) | **POST** /v1/search/existsByHealthId | Check the ABHA Address in our system. This API checks if ABHA Address  is reserved/used which includes permanently deleted ABHA Address


# **search_user_by_account_using_post**
> SearchResponseSingle search_user_by_account_using_post(search_request, accept_language=accept_language)

Search a user by ABHA Number or ABHA Address. This API returns only Active or Deactive ABHA Number/ Address (Never returns Permanently Deleted ABHA Number/ Address)

<b>Explanation</b> - API checks <b>ABHA Number or ABHA Address</b> to <b>find User</b>.    <b>Request Body</b> - Required. Here healthId attribute means ABHA Address    <b>Response</b> - API checks <b>ABHA Number or ABHA Address</b> to <b>find User</b>. API returns only Active or Deactive ABHA Number/ Address (Never returns Permanently Deleted ABHA Number/Address)

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.search_by_health_id_request import SearchByHealthIdRequest
from abha.models.search_response_single import SearchResponseSingle
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.SearchApi(api_client)
    search_request = abha.SearchByHealthIdRequest() # SearchByHealthIdRequest | searchRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Search a user by ABHA Number or ABHA Address. This API returns only Active or Deactive ABHA Number/ Address (Never returns Permanently Deleted ABHA Number/ Address)
        api_response = api_instance.search_user_by_account_using_post(search_request, accept_language=accept_language)
        print("The response of SearchApi->search_user_by_account_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_user_by_account_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**SearchByHealthIdRequest**](SearchByHealthIdRequest.md)| searchRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**SearchResponseSingle**](SearchResponseSingle.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return Account Details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | No Details Found for Given ABHA number Excluding Permanently deleted HIDs. |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_user_by_mobile_using_post**
> SearchResponseSingle search_user_by_mobile_using_post(search_request, accept_language=accept_language)

Search users with a mobile number

<b>Explanation</b> - API checks <b>Mobile Number</b> to <b>find User</b>.    <b>Request Body</b> - Required    <b>Response</b> - API checks <b>Mobile Number</b> to <b>find User</b>. gives Error for Non-Registered.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.search_by_mobile_request import SearchByMobileRequest
from abha.models.search_response_single import SearchResponseSingle
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.SearchApi(api_client)
    search_request = abha.SearchByMobileRequest() # SearchByMobileRequest | searchRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Search users with a mobile number
        api_response = api_instance.search_user_by_mobile_using_post(search_request, accept_language=accept_language)
        print("The response of SearchApi->search_user_by_mobile_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_user_by_mobile_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**SearchByMobileRequest**](SearchByMobileRequest.md)| searchRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**SearchResponseSingle**](SearchResponseSingle.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return Account Details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not find Registered Account For Given mobile number |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_user_by_userid_using_post**
> ExistsbyHealthIdResponse search_user_by_userid_using_post(search_dto, accept_language=accept_language)

Check the ABHA Address in our system. This API checks if ABHA Address  is reserved/used which includes permanently deleted ABHA Address

<b>Explanation</b> - API Checks <b>ABHA Address</b> to <b>find User</b>.    <b>Request Body</b> - Required. Here healthId attribute means ABHA Address    <b>Response</b> - API checks <b>ABHA Address</b> to <b>find User</b>. API checks if ABHA Address is reserved/used which includes permanently deleted ABHA Addresses

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.existsby_health_id_response import ExistsbyHealthIdResponse
from abha.models.search_by_health_id_request import SearchByHealthIdRequest
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.SearchApi(api_client)
    search_dto = abha.SearchByHealthIdRequest() # SearchByHealthIdRequest | searchDTO
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Check the ABHA Address in our system. This API checks if ABHA Address  is reserved/used which includes permanently deleted ABHA Address
        api_response = api_instance.search_user_by_userid_using_post(search_dto, accept_language=accept_language)
        print("The response of SearchApi->search_user_by_userid_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_user_by_userid_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_dto** | [**SearchByHealthIdRequest**](SearchByHealthIdRequest.md)| searchDTO | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**ExistsbyHealthIdResponse**](ExistsbyHealthIdResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return Status true in MAP in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | No Details Found for Given ABHA number Including permanently deleted HIDs. |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

