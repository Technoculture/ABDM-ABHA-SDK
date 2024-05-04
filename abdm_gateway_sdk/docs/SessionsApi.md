# abdm_gateway.SessionsApi

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_certs_get**](SessionsApi.md#v05_certs_get) | **GET** /v0.5/certs | Get certs for JWT verification
[**v05_sessions_post**](SessionsApi.md#v05_sessions_post) | **POST** /v0.5/sessions | Get access token
[**v05_well_known_openid_configuration_get**](SessionsApi.md#v05_well_known_openid_configuration_get) | **GET** /v0.5/.well-known/openid-configuration | Get openid configuration


# **v05_certs_get**
> Certs v05_certs_get()

Get certs for JWT verification

### Example


```python
import abdm_gateway
from abdm_gateway.models.certs import Certs
from abdm_gateway.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dev.abdm.gov.in/gateway
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm_gateway.Configuration(
    host = "https://dev.abdm.gov.in/gateway"
)


# Enter a context with an instance of the API client
with abdm_gateway.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm_gateway.SessionsApi(api_client)

    try:
        # Get certs for JWT verification
        api_response = api_instance.v05_certs_get()
        print("The response of SessionsApi->v05_certs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->v05_certs_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Certs**](Certs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | **Causes:**   * Invalid consent request id  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_sessions_post**
> SessionResponse v05_sessions_post(session_request)

Get access token

### Example


```python
import abdm_gateway
from abdm_gateway.models.session_request import SessionRequest
from abdm_gateway.models.session_response import SessionResponse
from abdm_gateway.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dev.abdm.gov.in/gateway
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm_gateway.Configuration(
    host = "https://dev.abdm.gov.in/gateway"
)


# Enter a context with an instance of the API client
with abdm_gateway.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm_gateway.SessionsApi(api_client)
    session_request = abdm_gateway.SessionRequest() # SessionRequest | 

    try:
        # Get access token
        api_response = api_instance.v05_sessions_post(session_request)
        print("The response of SessionsApi->v05_sessions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->v05_sessions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_request** | [**SessionRequest**](SessionRequest.md)|  | 

### Return type

[**SessionResponse**](SessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | **Causes:**   * Invalid consent request id  |  -  |
**401** | **Causes:**   * Invalid client Id or secret.  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_well_known_openid_configuration_get**
> OpenIdConfiguration v05_well_known_openid_configuration_get()

Get openid configuration

### Example


```python
import abdm_gateway
from abdm_gateway.models.open_id_configuration import OpenIdConfiguration
from abdm_gateway.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dev.abdm.gov.in/gateway
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm_gateway.Configuration(
    host = "https://dev.abdm.gov.in/gateway"
)


# Enter a context with an instance of the API client
with abdm_gateway.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm_gateway.SessionsApi(api_client)

    try:
        # Get openid configuration
        api_response = api_instance.v05_well_known_openid_configuration_get()
        print("The response of SessionsApi->v05_well_known_openid_configuration_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->v05_well_known_openid_configuration_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenIdConfiguration**](OpenIdConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | **Causes:**   * Invalid consent request id  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

