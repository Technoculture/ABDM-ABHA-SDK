# abdm_gateway.PatientNotificationApi

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_patients_sms_notify_post**](PatientNotificationApi.md#v05_patients_sms_notify_post) | **POST** /v0.5/patients/sms/notify | API for HIP to send SMS notifications to patients
[**v05_patients_sms_on_notify_post**](PatientNotificationApi.md#v05_patients_sms_on_notify_post) | **POST** /v0.5/patients/sms/on-notify | Acknowledgment response for SMS notification sent to patient by HIP
[**v05_patients_status_notify_post**](PatientNotificationApi.md#v05_patients_status_notify_post) | **POST** /v0.5/patients/status/notify | Notification sent by Consent MAnager
[**v05_patients_status_on_notify_post**](PatientNotificationApi.md#v05_patients_status_on_notify_post) | **POST** /v0.5/patients/status/on-notify | Acknowledgment by HIP/HIU


# **v05_patients_sms_notify_post**
> v05_patients_sms_notify_post(authorization, x_cm_id, patient_sms_notifcation_request)

API for HIP to send SMS notifications to patients

API to send SMS notifications to patient with custom deeplink. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_sms_notifcation_request import PatientSMSNotifcationRequest
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
    api_instance = abdm_gateway.PatientNotificationApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_sms_notifcation_request = abdm_gateway.PatientSMSNotifcationRequest() # PatientSMSNotifcationRequest | 

    try:
        # API for HIP to send SMS notifications to patients
        api_instance.v05_patients_sms_notify_post(authorization, x_cm_id, patient_sms_notifcation_request)
    except Exception as e:
        print("Exception when calling PatientNotificationApi->v05_patients_sms_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **patient_sms_notifcation_request** | [**PatientSMSNotifcationRequest**](PatientSMSNotifcationRequest.md)|  | 

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
**202** | accepted |  -  |
**400** | **Causes:**   * required information not provided  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_patients_sms_on_notify_post**
> v05_patients_sms_on_notify_post(authorization, x_hip_id, patient_sms_notifcation_response)

Acknowledgment response for SMS notification sent to patient by HIP

If the SMS notification is successfully sent to patient then \"status\" will be \"ACKNOWLEDGED\" with no error. If the SMS notification is failed then \"status\" will be \"ERRORED\" with error. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_sms_notifcation_response import PatientSMSNotifcationResponse
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
    api_instance = abdm_gateway.PatientNotificationApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    patient_sms_notifcation_response = abdm_gateway.PatientSMSNotifcationResponse() # PatientSMSNotifcationResponse | 

    try:
        # Acknowledgment response for SMS notification sent to patient by HIP
        api_instance.v05_patients_sms_on_notify_post(authorization, x_hip_id, patient_sms_notifcation_response)
    except Exception as e:
        print("Exception when calling PatientNotificationApi->v05_patients_sms_on_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **patient_sms_notifcation_response** | [**PatientSMSNotifcationResponse**](PatientSMSNotifcationResponse.md)|  | 

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
**400** | Invalid request, required attributes not provided  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_patients_status_notify_post**
> v05_patients_status_notify_post(authorization, x_hip_id, x_hiu_id, patient_status_notification)

Notification sent by Consent MAnager

Status (ACTIVE/DEACTIVATED/DELETED) will be sent to HIP. Note in addition to the \"Authorization\" header, one of the following headers must be specified 1. **X-HIU-ID** if the requester is HIU . 2. **X-HIP-ID** if the requester is HIP . 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_status_notification import PatientStatusNotification
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
    api_instance = abdm_gateway.PatientNotificationApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    patient_status_notification = abdm_gateway.PatientStatusNotification() # PatientStatusNotification | 

    try:
        # Notification sent by Consent MAnager
        api_instance.v05_patients_status_notify_post(authorization, x_hip_id, x_hiu_id, patient_status_notification)
    except Exception as e:
        print("Exception when calling PatientNotificationApi->v05_patients_status_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **patient_status_notification** | [**PatientStatusNotification**](PatientStatusNotification.md)|  | 

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
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_patients_status_on_notify_post**
> v05_patients_status_on_notify_post(authorization, x_cm_id, gateway_patient_status_notification)

Acknowledgment by HIP/HIU

This API is to be called by HIU/HIP bridge after receiving patient status (Activation/Reactivation/Deletion). In case of successfully receiving the notification \"status\" should sent as \"OK\" with no error. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.gateway_patient_status_notification import GatewayPatientStatusNotification
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
    api_instance = abdm_gateway.PatientNotificationApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    gateway_patient_status_notification = abdm_gateway.GatewayPatientStatusNotification() # GatewayPatientStatusNotification | 

    try:
        # Acknowledgment by HIP/HIU
        api_instance.v05_patients_status_on_notify_post(authorization, x_cm_id, gateway_patient_status_notification)
    except Exception as e:
        print("Exception when calling PatientNotificationApi->v05_patients_status_on_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **gateway_patient_status_notification** | [**GatewayPatientStatusNotification**](GatewayPatientStatusNotification.md)|  | 

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
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

