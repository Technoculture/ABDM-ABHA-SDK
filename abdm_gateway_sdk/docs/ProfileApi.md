# abdm_gateway.ProfileApi

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_patients_profile_on_share_post**](ProfileApi.md#v05_patients_profile_on_share_post) | **POST** /v0.5/patients/profile/on-share | Response to patient&#39;s share profile request
[**v05_patients_profile_share_post**](ProfileApi.md#v05_patients_profile_share_post) | **POST** /v0.5/patients/profile/share | Share patient profile details
[**v10_patients_profile_on_share_post**](ProfileApi.md#v10_patients_profile_on_share_post) | **POST** /v1.0/patients/profile/on-share | Response to patient&#39;s share profile request
[**v10_patients_profile_share_post**](ProfileApi.md#v10_patients_profile_share_post) | **POST** /v1.0/patients/profile/share | Share patient profile details


# **v05_patients_profile_on_share_post**
> v05_patients_profile_on_share_post(authorization, x_cm_id, share_profile_result)

Response to patient's share profile request

Result of patient share profile request at HIP end. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.share_profile_result import ShareProfileResult
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
    api_instance = abdm_gateway.ProfileApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    share_profile_result = abdm_gateway.ShareProfileResult() # ShareProfileResult | 

    try:
        # Response to patient's share profile request
        api_instance.v05_patients_profile_on_share_post(authorization, x_cm_id, share_profile_result)
    except Exception as e:
        print("Exception when calling ProfileApi->v05_patients_profile_on_share_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **share_profile_result** | [**ShareProfileResult**](ShareProfileResult.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted |  -  |
**400** | **Causes:**   * Format mismatch of any of attributes.  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_patients_profile_share_post**
> v05_patients_profile_share_post(authorization, x_hip_id, share_profile_request)

Share patient profile details

Request for sharing patient's profile details to HIP 

### Example


```python
import abdm_gateway
from abdm_gateway.models.share_profile_request import ShareProfileRequest
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
    api_instance = abdm_gateway.ProfileApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    share_profile_request = abdm_gateway.ShareProfileRequest() # ShareProfileRequest | 

    try:
        # Share patient profile details
        api_instance.v05_patients_profile_share_post(authorization, x_hip_id, share_profile_request)
    except Exception as e:
        print("Exception when calling ProfileApi->v05_patients_profile_share_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **share_profile_request** | [**ShareProfileRequest**](ShareProfileRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted |  -  |
**400** | **Causes:**   * Invalid Request  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_patients_profile_on_share_post**
> v10_patients_profile_on_share_post(authorization, x_cm_id, share_profile_result1)

Response to patient's share profile request

Result of patient share profile request at HIP end. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.share_profile_result1 import ShareProfileResult1
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
    api_instance = abdm_gateway.ProfileApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    share_profile_result1 = abdm_gateway.ShareProfileResult1() # ShareProfileResult1 | 

    try:
        # Response to patient's share profile request
        api_instance.v10_patients_profile_on_share_post(authorization, x_cm_id, share_profile_result1)
    except Exception as e:
        print("Exception when calling ProfileApi->v10_patients_profile_on_share_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **share_profile_result1** | [**ShareProfileResult1**](ShareProfileResult1.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted |  -  |
**400** | **Causes:**   * Format mismatch of any of attributes.  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v10_patients_profile_share_post**
> v10_patients_profile_share_post(authorization, x_hip_id, share_profile_request1)

Share patient profile details

Request for sharing patient's profile details to HIP 

### Example


```python
import abdm_gateway
from abdm_gateway.models.share_profile_request1 import ShareProfileRequest1
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
    api_instance = abdm_gateway.ProfileApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    share_profile_request1 = abdm_gateway.ShareProfileRequest1() # ShareProfileRequest1 | 

    try:
        # Share patient profile details
        api_instance.v10_patients_profile_share_post(authorization, x_hip_id, share_profile_request1)
    except Exception as e:
        print("Exception when calling ProfileApi->v10_patients_profile_share_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **share_profile_request1** | [**ShareProfileRequest1**](ShareProfileRequest1.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted |  -  |
**400** | **Causes:**   * Invalid Request  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

