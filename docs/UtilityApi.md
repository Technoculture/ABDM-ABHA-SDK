# abha.UtilityApi

All URIs are relative to *http://healthidsbx.abdm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_districts_in_state_using_get**](UtilityApi.md#get_districts_in_state_using_get) | **GET** /v1/ha/lgd/districts | Get a list of districts in a given  State as per LGD.
[**get_states_using_get**](UtilityApi.md#get_states_using_get) | **GET** /v1/ha/lgd/states | Get a list of states as per LGD.


# **get_districts_in_state_using_get**
> DistrictDTO get_districts_in_state_using_get(state_code, accept_language=accept_language)

Get a list of districts in a given  State as per LGD.

<b>Explanation</b> - Api Accepts <b>State Code</b> then returns List of District.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>State Code</b> then returns List of District.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.district_dto import DistrictDTO
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
    api_instance = abha.UtilityApi(api_client)
    state_code = '27' # str | stateCode
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Get a list of districts in a given  State as per LGD.
        api_response = api_instance.get_districts_in_state_using_get(state_code, accept_language=accept_language)
        print("The response of UtilityApi->get_districts_in_state_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilityApi->get_districts_in_state_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_code** | **str**| stateCode | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**DistrictDTO**](DistrictDTO.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a list of Districts in case of success |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not find Affiliated District for given State |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_states_using_get**
> StatesDTO get_states_using_get(accept_language=accept_language)

Get a list of states as per LGD.

<b>Explanation</b> - Api Returns <b>States</b> With its Districts.    <b>Request Body</b> - Required    <b>Responce</b> - Api Returns <b>States</b> With its Districts.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.states_dto import StatesDTO
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
    api_instance = abha.UtilityApi(api_client)
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Get a list of states as per LGD.
        api_response = api_instance.get_states_using_get(accept_language=accept_language)
        print("The response of UtilityApi->get_states_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilityApi->get_states_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**StatesDTO**](StatesDTO.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a list of states as per LGD. in case of success |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not find List of State |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

