# abdm_gateway.DataFlowApi

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_health_information_cm_on_request_post**](DataFlowApi.md#v05_health_information_cm_on_request_post) | **POST** /v0.5/health-information/cm/on-request | Health information data request
[**v05_health_information_cm_request_post**](DataFlowApi.md#v05_health_information_cm_request_post) | **POST** /v0.5/health-information/cm/request | Health information data request
[**v05_health_information_hip_on_request_post**](DataFlowApi.md#v05_health_information_hip_on_request_post) | **POST** /v0.5/health-information/hip/on-request | Health information data request
[**v05_health_information_hip_request_post**](DataFlowApi.md#v05_health_information_hip_request_post) | **POST** /v0.5/health-information/hip/request | Health information data request
[**v05_health_information_notify_post**](DataFlowApi.md#v05_health_information_notify_post) | **POST** /v0.5/health-information/notify | Notifications corresponding to events during data flow


# **v05_health_information_cm_on_request_post**
> v05_health_information_cm_on_request_post(authorization, x_hiu_id, hiu_health_information_request_response)

Health information data request

Callback API for acknowledgement of Health information request of HIU. CM calls this API when it has validated the Health Information request given the consent id. Either the **hiRequest** or **error** would need to be specified. If the health info request was valid, then the ***hiRequest.transactionId*** specifies the transaction context against which HIP would send over the data.  Possible cases of errors are   1. **Invalid consent artefact id**   2. **Consent has expired**   3. **Date ranges are invalid** 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hiu_health_information_request_response import HIUHealthInformationRequestResponse
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
    api_instance = abdm_gateway.DataFlowApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    hiu_health_information_request_response = abdm_gateway.HIUHealthInformationRequestResponse() # HIUHealthInformationRequestResponse | 

    try:
        # Health information data request
        api_instance.v05_health_information_cm_on_request_post(authorization, x_hiu_id, hiu_health_information_request_response)
    except Exception as e:
        print("Exception when calling DataFlowApi->v05_health_information_cm_on_request_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **hiu_health_information_request_response** | [**HIUHealthInformationRequestResponse**](HIUHealthInformationRequestResponse.md)|  | 

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
**202** | Request Accepted |  -  |
**400** | **Causes:**   * Bad request  |  -  |
**401** | **Causes:**   * Token is invalid or Link has expired  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_health_information_cm_request_post**
> v05_health_information_cm_request_post(authorization, x_cm_id, hi_request)

Health information data request

Request for Health information against a consent id. CM would generate a transactionId against each consent and pass it as trnasaction context / correlation id to the HIP and also return the same to HIU via /on-request. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hi_request import HIRequest
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
    api_instance = abdm_gateway.DataFlowApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    hi_request = abdm_gateway.HIRequest() # HIRequest | 

    try:
        # Health information data request
        api_instance.v05_health_information_cm_request_post(authorization, x_cm_id, hi_request)
    except Exception as e:
        print("Exception when calling DataFlowApi->v05_health_information_cm_request_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **hi_request** | [**HIRequest**](HIRequest.md)|  | 

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
**202** | Request Accepted |  -  |
**400** | **Causes:**   * Bad request  |  -  |
**401** | **Causes:**   * Token is invalid or Link has expired  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_health_information_hip_on_request_post**
> v05_health_information_hip_on_request_post(authorization, x_cm_id, hip_health_information_request_acknowledgement)

Health information data request

API called by HIP to acknowledge Health information request receipt. Either the **hiRequest** or **error** must be specified. **hiRequest** element returns the same transactionId as before with a status indicating that the request is acknowledged. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hip_health_information_request_acknowledgement import HIPHealthInformationRequestAcknowledgement
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
    api_instance = abdm_gateway.DataFlowApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    hip_health_information_request_acknowledgement = abdm_gateway.HIPHealthInformationRequestAcknowledgement() # HIPHealthInformationRequestAcknowledgement | 

    try:
        # Health information data request
        api_instance.v05_health_information_hip_on_request_post(authorization, x_cm_id, hip_health_information_request_acknowledgement)
    except Exception as e:
        print("Exception when calling DataFlowApi->v05_health_information_hip_on_request_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **hip_health_information_request_acknowledgement** | [**HIPHealthInformationRequestAcknowledgement**](HIPHealthInformationRequestAcknowledgement.md)|  | 

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
**202** | Request accepted. |  -  |
**400** | **Causes:**   * Bad request  |  -  |
**401** | **Causes:**   * Token is invalid or Link has expired  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_health_information_hip_request_post**
> v05_health_information_hip_request_post(authorization, x_hip_id, hiphi_request)

Health information data request

API called by CM to request Health information from HIP against a validated consent artefact. The transactionId is the correlation id that HIP should use use when pushing data to the **dataPushUrl**. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hiphi_request import HIPHIRequest
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
    api_instance = abdm_gateway.DataFlowApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    hiphi_request = abdm_gateway.HIPHIRequest() # HIPHIRequest | 

    try:
        # Health information data request
        api_instance.v05_health_information_hip_request_post(authorization, x_hip_id, hiphi_request)
    except Exception as e:
        print("Exception when calling DataFlowApi->v05_health_information_hip_request_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **hiphi_request** | [**HIPHIRequest**](HIPHIRequest.md)|  | 

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
**202** | Request accepted. |  -  |
**400** | **Causes:**   * Bad request  |  -  |
**401** | **Causes:**   * Token is invalid or Link has expired  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_health_information_notify_post**
> v05_health_information_notify_post(authorization, x_cm_id, health_information_notification)

Notifications corresponding to events during data flow

API called by HIU and HIP during data-transfer.  1. HIP on transfer of data would send **sessionStatus** - one of [TRANSFERRED, FAILED] 2. HIP would also send **hiStatus** for each *careContextReference* - on of [DELIVERED, ERRORED] 3. HIU on receipt of data would send **sessionStatus** - one of [TRANSFERRED, FAILED]. For example, FAILED when if data was not sent or if invalid data was sent 4. HIU would also send **hiStatus** for each *careContextReference* - one of [OK, ERRORED] 

### Example


```python
import abdm_gateway
from abdm_gateway.models.health_information_notification import HealthInformationNotification
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
    api_instance = abdm_gateway.DataFlowApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    health_information_notification = abdm_gateway.HealthInformationNotification() # HealthInformationNotification | 

    try:
        # Notifications corresponding to events during data flow
        api_instance.v05_health_information_notify_post(authorization, x_cm_id, health_information_notification)
    except Exception as e:
        print("Exception when calling DataFlowApi->v05_health_information_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **health_information_notification** | [**HealthInformationNotification**](HealthInformationNotification.md)|  | 

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
**204** | Notification is Accepted |  -  |
**400** | **Causes:**   * Invalid Request  |  -  |
**401** | **Causes:**   * Expired/Invalid token.  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

