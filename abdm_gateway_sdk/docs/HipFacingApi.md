# abdm_gateway.HipFacingApi

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_consents_hip_on_notify_post**](HipFacingApi.md#v05_consents_hip_on_notify_post) | **POST** /v0.5/consents/hip/on-notify | Consent notification
[**v05_health_information_hip_on_request_post**](HipFacingApi.md#v05_health_information_hip_on_request_post) | **POST** /v0.5/health-information/hip/on-request | Health information data request
[**v05_health_information_notify_post**](HipFacingApi.md#v05_health_information_notify_post) | **POST** /v0.5/health-information/notify | Notifications corresponding to events during data flow
[**v05_links_context_notify_post**](HipFacingApi.md#v05_links_context_notify_post) | **POST** /v0.5/links/context/notify | This API is meant to be called by HIPs when there is new health data generated for a patient, against a care context that is already linked to patient&#39;s ABDM account.
[**v05_links_link_add_contexts_post**](HipFacingApi.md#v05_links_link_add_contexts_post) | **POST** /v0.5/links/link/add-contexts | API for HIP initiated care-context linking for patient
[**v05_links_link_on_confirm_post**](HipFacingApi.md#v05_links_link_on_confirm_post) | **POST** /v0.5/links/link/on-confirm | Token authenticated by HIP, indicating completion of linkage of care-contexts
[**v05_links_link_on_init_post**](HipFacingApi.md#v05_links_link_on_init_post) | **POST** /v0.5/links/link/on-init | Response to patient&#39;s care context link request
[**v05_patients_sms_notify_post**](HipFacingApi.md#v05_patients_sms_notify_post) | **POST** /v0.5/patients/sms/notify | API for HIP to send SMS notifications to patients
[**v05_patients_status_on_notify_post**](HipFacingApi.md#v05_patients_status_on_notify_post) | **POST** /v0.5/patients/status/on-notify | Acknowledgment by HIP/HIU
[**v05_users_auth_confirm_post**](HipFacingApi.md#v05_users_auth_confirm_post) | **POST** /v0.5/users/auth/confirm | Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation
[**v05_users_auth_fetch_modes_post**](HipFacingApi.md#v05_users_auth_fetch_modes_post) | **POST** /v0.5/users/auth/fetch-modes | Get a patient&#39;s authentication modes relevant to specified purpose
[**v05_users_auth_init_post**](HipFacingApi.md#v05_users_auth_init_post) | **POST** /v0.5/users/auth/init | Initialize authentication from HIP
[**v05_users_auth_on_notify_post**](HipFacingApi.md#v05_users_auth_on_notify_post) | **POST** /v0.5/users/auth/on-notify | callback API by HIU/HIPs as acknowledgement of auth notification


# **v05_consents_hip_on_notify_post**
> v05_consents_hip_on_notify_post(authorization, x_cm_id, hip_consent_notification_response)

Consent notification

This API is called by HIP as acknowledgement to notification of consents, in cases of consent revocation and expiration. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hip_consent_notification_response import HIPConsentNotificationResponse
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
    api_instance = abdm_gateway.HipFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    hip_consent_notification_response = abdm_gateway.HIPConsentNotificationResponse() # HIPConsentNotificationResponse | 

    try:
        # Consent notification
        api_instance.v05_consents_hip_on_notify_post(authorization, x_cm_id, hip_consent_notification_response)
    except Exception as e:
        print("Exception when calling HipFacingApi->v05_consents_hip_on_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **hip_consent_notification_response** | [**HIPConsentNotificationResponse**](HIPConsentNotificationResponse.md)|  | 

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
**401** | **Causes:**   * Invalid/Expired/Empty token.  |  -  |
**500** | **Causes:**   * Downstream services are down  |  -  |

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
    api_instance = abdm_gateway.HipFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    hip_health_information_request_acknowledgement = abdm_gateway.HIPHealthInformationRequestAcknowledgement() # HIPHealthInformationRequestAcknowledgement | 

    try:
        # Health information data request
        api_instance.v05_health_information_hip_on_request_post(authorization, x_cm_id, hip_health_information_request_acknowledgement)
    except Exception as e:
        print("Exception when calling HipFacingApi->v05_health_information_hip_on_request_post: %s\n" % e)
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
    api_instance = abdm_gateway.HipFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    health_information_notification = abdm_gateway.HealthInformationNotification() # HealthInformationNotification | 

    try:
        # Notifications corresponding to events during data flow
        api_instance.v05_health_information_notify_post(authorization, x_cm_id, health_information_notification)
    except Exception as e:
        print("Exception when calling HipFacingApi->v05_health_information_notify_post: %s\n" % e)
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

# **v05_links_context_notify_post**
> v05_links_context_notify_post(authorization, x_cm_id, hip_data_notification_request)

This API is meant to be called by HIPs when there is new health data generated for a patient, against a care context that is already linked to patient's ABDM account.

This API is called by HIP only when there is new health data is added/created for a patient and under a care context that is already linked with patient's Health Account.  HIP can send following things in this API to notify the Consent Manager about the new health data added:   1. **Patient's Identifier for which the new health data is added (It can be ABDM id or ABDM number)**   2. **Care Context reference under which the new health data is added**   3. **Patient's reference (An identifier with which the patient is registered on HIP)**   4. **Types of health information documents that have been added**   5. **A date when the health information was created/added on the HIP** Note: This API shouldn't be called if the new heath data of is added/created under new care context. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hip_data_notification_request import HipDataNotificationRequest
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
    api_instance = abdm_gateway.HipFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    hip_data_notification_request = abdm_gateway.HipDataNotificationRequest() # HipDataNotificationRequest | 

    try:
        # This API is meant to be called by HIPs when there is new health data generated for a patient, against a care context that is already linked to patient's ABDM account.
        api_instance.v05_links_context_notify_post(authorization, x_cm_id, hip_data_notification_request)
    except Exception as e:
        print("Exception when calling HipFacingApi->v05_links_context_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **hip_data_notification_request** | [**HipDataNotificationRequest**](HipDataNotificationRequest.md)|  | 

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
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_links_link_add_contexts_post**
> v05_links_link_add_contexts_post(authorization, x_cm_id, patient_care_context_link_request)

API for HIP initiated care-context linking for patient

API to submit care-context to CM for HIP initiated linking. The API must accompany the \"accessToken\" fetched in the users/auth process.     1. subsequent usage for accessToken may be invalid if it was meant for one-time usage or if it expired 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_care_context_link_request import PatientCareContextLinkRequest
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
    api_instance = abdm_gateway.HipFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_care_context_link_request = abdm_gateway.PatientCareContextLinkRequest() # PatientCareContextLinkRequest | 

    try:
        # API for HIP initiated care-context linking for patient
        api_instance.v05_links_link_add_contexts_post(authorization, x_cm_id, patient_care_context_link_request)
    except Exception as e:
        print("Exception when calling HipFacingApi->v05_links_link_add_contexts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **patient_care_context_link_request** | [**PatientCareContextLinkRequest**](PatientCareContextLinkRequest.md)|  | 

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

# **v05_links_link_on_confirm_post**
> v05_links_link_on_confirm_post(authorization, x_cm_id, patient_link_result)

Token authenticated by HIP, indicating completion of linkage of care-contexts

Returns a list of linked care contexts with patient reference number.   1. **Validated and linked account reference number**   2. **Validated that the token sent from Consent Manager is same as the one generated by HIP**   3. **Verified that same Consent Manager which made the link request is sending the token**   4. **Results of unmasked linked care contexts with patient reference number** 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_link_result import PatientLinkResult
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
    api_instance = abdm_gateway.HipFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_link_result = abdm_gateway.PatientLinkResult() # PatientLinkResult | 

    try:
        # Token authenticated by HIP, indicating completion of linkage of care-contexts
        api_instance.v05_links_link_on_confirm_post(authorization, x_cm_id, patient_link_result)
    except Exception as e:
        print("Exception when calling HipFacingApi->v05_links_link_on_confirm_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **patient_link_result** | [**PatientLinkResult**](PatientLinkResult.md)|  | 

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
**400** | **Causes:**   * resp not specified   * atleast patient or error should be specified  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_links_link_on_init_post**
> v05_links_link_on_init_post(authorization, x_cm_id, patient_link_reference_result)

Response to patient's care context link request

Result of patient care-context link request from HIP end. This happens in context of previous discovery of patient found at HIP end, therefore the link requests ought to be in reference to the patient reference and care-context references previously returned by the HIP. The correlation of discovery and link request is maintained through the transactionId. HIP should have   1. **Validated transactionId in the request to check whether there was a discovery done previously, and the link request corresponds to returned patient care care context references**   2. **Before returning the response, HIP should have sent an authentication request to the patient(eg: OTP verification)**   3. **HIP should communicate the mode of authentication of a successful request**   4. **HIP subsequently should expect the token passed via /link/confirm against the link.referenceNumber passed in this call**  The error section in the body, represents the potential errors that may have occurred. Possible reasons:   1. **Patient reference number is invalid**   2. **Care context reference numbers are invalid** 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_link_reference_result import PatientLinkReferenceResult
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
    api_instance = abdm_gateway.HipFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_link_reference_result = abdm_gateway.PatientLinkReferenceResult() # PatientLinkReferenceResult | 

    try:
        # Response to patient's care context link request
        api_instance.v05_links_link_on_init_post(authorization, x_cm_id, patient_link_reference_result)
    except Exception as e:
        print("Exception when calling HipFacingApi->v05_links_link_on_init_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **patient_link_reference_result** | [**PatientLinkReferenceResult**](PatientLinkReferenceResult.md)|  | 

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
    api_instance = abdm_gateway.HipFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_sms_notifcation_request = abdm_gateway.PatientSMSNotifcationRequest() # PatientSMSNotifcationRequest | 

    try:
        # API for HIP to send SMS notifications to patients
        api_instance.v05_patients_sms_notify_post(authorization, x_cm_id, patient_sms_notifcation_request)
    except Exception as e:
        print("Exception when calling HipFacingApi->v05_patients_sms_notify_post: %s\n" % e)
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
    api_instance = abdm_gateway.HipFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    gateway_patient_status_notification = abdm_gateway.GatewayPatientStatusNotification() # GatewayPatientStatusNotification | 

    try:
        # Acknowledgment by HIP/HIU
        api_instance.v05_patients_status_on_notify_post(authorization, x_cm_id, gateway_patient_status_notification)
    except Exception as e:
        print("Exception when calling HipFacingApi->v05_patients_status_on_notify_post: %s\n" % e)
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

# **v05_users_auth_confirm_post**
> v05_users_auth_confirm_post(authorization, x_cm_id, patient_auth_confirm_request)

Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation

This API is called by HIP/HIUs to confirm authentication of users. The transactionId returned by the previous callback API /users/auth/on-init must be sent. If Authentication is successful the callback API will send an \"access token\" for subsequent purpose specific API calls. Note only **credential.authCode** or **credential.demographic** should be sent   1. demographic details are only required for  demographic auth as of now.    2. demographic details are required only in MEDIATED cases and if the **auth.mode** so demands. e.g. if **auth.mode** is DEMOGRAPHICS. Usually for demographic authentication, the name, gender and DOB must be exactly as specified in User Account.   3. demographic.identifier is optional, however maybe required if authentication so mandates.    4. credential.authCode is required for other MEDIATED authentication like MOBILE_OTP, AADHAAR_OTP. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_auth_confirm_request import PatientAuthConfirmRequest
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
    api_instance = abdm_gateway.HipFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_auth_confirm_request = abdm_gateway.PatientAuthConfirmRequest() # PatientAuthConfirmRequest | 

    try:
        # Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation
        api_instance.v05_users_auth_confirm_post(authorization, x_cm_id, patient_auth_confirm_request)
    except Exception as e:
        print("Exception when calling HipFacingApi->v05_users_auth_confirm_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **patient_auth_confirm_request** | [**PatientAuthConfirmRequest**](PatientAuthConfirmRequest.md)|  | 

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
**400** | **Causes:**   * transaction id is not provided or invalid   * token or other auth confirmation details not provided or invalid  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_users_auth_fetch_modes_post**
> v05_users_auth_fetch_modes_post(authorization, x_cm_id, patient_auth_mode_query_request)

Get a patient's authentication modes relevant to specified purpose

This API is meant for identify supported authentication modes for a patient given a specific purpose 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_auth_mode_query_request import PatientAuthModeQueryRequest
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
    api_instance = abdm_gateway.HipFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_auth_mode_query_request = abdm_gateway.PatientAuthModeQueryRequest() # PatientAuthModeQueryRequest | 

    try:
        # Get a patient's authentication modes relevant to specified purpose
        api_instance.v05_users_auth_fetch_modes_post(authorization, x_cm_id, patient_auth_mode_query_request)
    except Exception as e:
        print("Exception when calling HipFacingApi->v05_users_auth_fetch_modes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **patient_auth_mode_query_request** | [**PatientAuthModeQueryRequest**](PatientAuthModeQueryRequest.md)|  | 

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

# **v05_users_auth_init_post**
> v05_users_auth_init_post(authorization, x_cm_id, patient_auth_init_request)

Initialize authentication from HIP

This API is called by HIPs to initiate authentication of users. A transactionId is retuned by the corresponding callback API for confirmation of user auth. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_auth_init_request import PatientAuthInitRequest
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
    api_instance = abdm_gateway.HipFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_auth_init_request = abdm_gateway.PatientAuthInitRequest() # PatientAuthInitRequest | 

    try:
        # Initialize authentication from HIP
        api_instance.v05_users_auth_init_post(authorization, x_cm_id, patient_auth_init_request)
    except Exception as e:
        print("Exception when calling HipFacingApi->v05_users_auth_init_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **patient_auth_init_request** | [**PatientAuthInitRequest**](PatientAuthInitRequest.md)|  | 

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
**400** | **Causes:**   * patient id is not provided  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_users_auth_on_notify_post**
> v05_users_auth_on_notify_post(authorization, x_cm_id, patient_auth_notification_acknowledgement)

callback API by HIU/HIPs as acknowledgement of auth notification

This API is called by HIU/HIPs to confirm acknowledgement for receipt of auth notification is case of DIRECT authentication. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_auth_notification_acknowledgement import PatientAuthNotificationAcknowledgement
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
    api_instance = abdm_gateway.HipFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_auth_notification_acknowledgement = abdm_gateway.PatientAuthNotificationAcknowledgement() # PatientAuthNotificationAcknowledgement | 

    try:
        # callback API by HIU/HIPs as acknowledgement of auth notification
        api_instance.v05_users_auth_on_notify_post(authorization, x_cm_id, patient_auth_notification_acknowledgement)
    except Exception as e:
        print("Exception when calling HipFacingApi->v05_users_auth_on_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **patient_auth_notification_acknowledgement** | [**PatientAuthNotificationAcknowledgement**](PatientAuthNotificationAcknowledgement.md)|  | 

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
**400** | **Causes:**   * required details not provided   * neither auth nor error specified  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

