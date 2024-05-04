# abdm_gateway.HiuFacingApi

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_consent_requests_init_post**](HiuFacingApi.md#v05_consent_requests_init_post) | **POST** /v0.5/consent-requests/init | Create consent request
[**v05_consent_requests_status_post**](HiuFacingApi.md#v05_consent_requests_status_post) | **POST** /v0.5/consent-requests/status | Get consent request status
[**v05_consents_fetch_post**](HiuFacingApi.md#v05_consents_fetch_post) | **POST** /v0.5/consents/fetch | Get consent artefact
[**v05_consents_hiu_on_notify_post**](HiuFacingApi.md#v05_consents_hiu_on_notify_post) | **POST** /v0.5/consents/hiu/on-notify | Consent notification
[**v05_health_information_cm_request_post**](HiuFacingApi.md#v05_health_information_cm_request_post) | **POST** /v0.5/health-information/cm/request | Health information data request
[**v05_health_information_notify_post**](HiuFacingApi.md#v05_health_information_notify_post) | **POST** /v0.5/health-information/notify | Notifications corresponding to events during data flow
[**v05_patients_find_post**](HiuFacingApi.md#v05_patients_find_post) | **POST** /v0.5/patients/find | Identify a patient by her consent-manager user-id
[**v05_patients_status_on_notify_post**](HiuFacingApi.md#v05_patients_status_on_notify_post) | **POST** /v0.5/patients/status/on-notify | Acknowledgment by HIP/HIU
[**v05_subscription_requests_cm_init_post**](HiuFacingApi.md#v05_subscription_requests_cm_init_post) | **POST** /v0.5/subscription-requests/cm/init | Request for subscription
[**v05_subscription_requests_hiu_on_notify_post**](HiuFacingApi.md#v05_subscription_requests_hiu_on_notify_post) | **POST** /v0.5/subscription-requests/hiu/on-notify | Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.
[**v05_subscriptions_hiu_on_notify_post**](HiuFacingApi.md#v05_subscriptions_hiu_on_notify_post) | **POST** /v0.5/subscriptions/hiu/on-notify | Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.
[**v05_users_auth_confirm_post**](HiuFacingApi.md#v05_users_auth_confirm_post) | **POST** /v0.5/users/auth/confirm | Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation
[**v05_users_auth_fetch_modes_post**](HiuFacingApi.md#v05_users_auth_fetch_modes_post) | **POST** /v0.5/users/auth/fetch-modes | Get a patient&#39;s authentication modes relevant to specified purpose
[**v05_users_auth_init_post**](HiuFacingApi.md#v05_users_auth_init_post) | **POST** /v0.5/users/auth/init | Initialize authentication from HIP
[**v05_users_auth_on_notify_post**](HiuFacingApi.md#v05_users_auth_on_notify_post) | **POST** /v0.5/users/auth/on-notify | callback API by HIU/HIPs as acknowledgement of auth notification


# **v05_consent_requests_init_post**
> v05_consent_requests_init_post(authorization, x_cm_id, consent_request)

Create consent request

Creates a consent request to get data about a patient by HIU user.

### Example


```python
import abdm_gateway
from abdm_gateway.models.consent_request import ConsentRequest
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
    api_instance = abdm_gateway.HiuFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    consent_request = abdm_gateway.ConsentRequest() # ConsentRequest | 

    try:
        # Create consent request
        api_instance.v05_consent_requests_init_post(authorization, x_cm_id, consent_request)
    except Exception as e:
        print("Exception when calling HiuFacingApi->v05_consent_requests_init_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **consent_request** | [**ConsentRequest**](ConsentRequest.md)|  | 

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
**400** | **Causes:**   * Invalid data sent    * Required attributes not mentioned  |  -  |
**401** | **Causes:**   * Expired/Invalid token.  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_consent_requests_status_post**
> v05_consent_requests_status_post(authorization, x_cm_id, consent_request_status_request)

Get consent request status

Get status of consent request done previously

### Example


```python
import abdm_gateway
from abdm_gateway.models.consent_request_status_request import ConsentRequestStatusRequest
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
    api_instance = abdm_gateway.HiuFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    consent_request_status_request = abdm_gateway.ConsentRequestStatusRequest() # ConsentRequestStatusRequest | 

    try:
        # Get consent request status
        api_instance.v05_consent_requests_status_post(authorization, x_cm_id, consent_request_status_request)
    except Exception as e:
        print("Exception when calling HiuFacingApi->v05_consent_requests_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **consent_request_status_request** | [**ConsentRequestStatusRequest**](ConsentRequestStatusRequest.md)|  | 

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
**400** | **Causes:**   * Invalid data sent  |  -  |
**401** | **Causes:**   * Expired/Invalid token.  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_consents_fetch_post**
> v05_consents_fetch_post(authorization, x_cm_id, consent_fetch_request)

Get consent artefact

### Example


```python
import abdm_gateway
from abdm_gateway.models.consent_fetch_request import ConsentFetchRequest
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
    api_instance = abdm_gateway.HiuFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    consent_fetch_request = abdm_gateway.ConsentFetchRequest() # ConsentFetchRequest | 

    try:
        # Get consent artefact
        api_instance.v05_consents_fetch_post(authorization, x_cm_id, consent_fetch_request)
    except Exception as e:
        print("Exception when calling HiuFacingApi->v05_consents_fetch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **consent_fetch_request** | [**ConsentFetchRequest**](ConsentFetchRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted |  -  |
**400** | **Causes:**   * Invalid data sent  |  -  |
**401** | **Causes:**   * Expired/Invalid token.  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_consents_hiu_on_notify_post**
> v05_consents_hiu_on_notify_post(authorization, x_cm_id, hiu_consent_notification_response)

Consent notification

This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hiu_consent_notification_response import HIUConsentNotificationResponse
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
    api_instance = abdm_gateway.HiuFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    hiu_consent_notification_response = abdm_gateway.HIUConsentNotificationResponse() # HIUConsentNotificationResponse | 

    try:
        # Consent notification
        api_instance.v05_consents_hiu_on_notify_post(authorization, x_cm_id, hiu_consent_notification_response)
    except Exception as e:
        print("Exception when calling HiuFacingApi->v05_consents_hiu_on_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **hiu_consent_notification_response** | [**HIUConsentNotificationResponse**](HIUConsentNotificationResponse.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted. |  -  |
**401** | **Causes:**   * Invalid/Expired/Empty token.  |  -  |
**500** | **Causes:**   * Downstream services are down  |  -  |

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
    api_instance = abdm_gateway.HiuFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    hi_request = abdm_gateway.HIRequest() # HIRequest | 

    try:
        # Health information data request
        api_instance.v05_health_information_cm_request_post(authorization, x_cm_id, hi_request)
    except Exception as e:
        print("Exception when calling HiuFacingApi->v05_health_information_cm_request_post: %s\n" % e)
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
    api_instance = abdm_gateway.HiuFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    health_information_notification = abdm_gateway.HealthInformationNotification() # HealthInformationNotification | 

    try:
        # Notifications corresponding to events during data flow
        api_instance.v05_health_information_notify_post(authorization, x_cm_id, health_information_notification)
    except Exception as e:
        print("Exception when calling HiuFacingApi->v05_health_information_notify_post: %s\n" % e)
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

# **v05_patients_find_post**
> v05_patients_find_post(authorization, x_cm_id, patient_identification_request)

Identify a patient by her consent-manager user-id

This API is meant for identify to patient given her consent-manager-user-id 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_identification_request import PatientIdentificationRequest
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
    api_instance = abdm_gateway.HiuFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_identification_request = abdm_gateway.PatientIdentificationRequest() # PatientIdentificationRequest | 

    try:
        # Identify a patient by her consent-manager user-id
        api_instance.v05_patients_find_post(authorization, x_cm_id, patient_identification_request)
    except Exception as e:
        print("Exception when calling HiuFacingApi->v05_patients_find_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **patient_identification_request** | [**PatientIdentificationRequest**](PatientIdentificationRequest.md)|  | 

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
    api_instance = abdm_gateway.HiuFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    gateway_patient_status_notification = abdm_gateway.GatewayPatientStatusNotification() # GatewayPatientStatusNotification | 

    try:
        # Acknowledgment by HIP/HIU
        api_instance.v05_patients_status_on_notify_post(authorization, x_cm_id, gateway_patient_status_notification)
    except Exception as e:
        print("Exception when calling HiuFacingApi->v05_patients_status_on_notify_post: %s\n" % e)
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

# **v05_subscription_requests_cm_init_post**
> v05_subscription_requests_cm_init_post(authorization, x_cm_id, subscription_request)

Request for subscription

creates a request for subscription. The subscription categories can be for care-contexts linkages or availability of data against existing care-contexts. Note that the requester must have HIU role

### Example


```python
import abdm_gateway
from abdm_gateway.models.subscription_request import SubscriptionRequest
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
    api_instance = abdm_gateway.HiuFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    subscription_request = abdm_gateway.SubscriptionRequest() # SubscriptionRequest | 

    try:
        # Request for subscription
        api_instance.v05_subscription_requests_cm_init_post(authorization, x_cm_id, subscription_request)
    except Exception as e:
        print("Exception when calling HiuFacingApi->v05_subscription_requests_cm_init_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **subscription_request** | [**SubscriptionRequest**](SubscriptionRequest.md)|  | 

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
**400** | **Causes:**   * Invalid data sent    * Required attributes not mentioned  |  -  |
**401** | **Causes:**   * Expired/Invalid token.  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_subscription_requests_hiu_on_notify_post**
> v05_subscription_requests_hiu_on_notify_post(authorization, x_cm_id, hiu_subscription_request_notification_acknowledgement)

Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.

This API is called by HIU as acknowledgement to subscription request relevant notifications. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hiu_subscription_request_notification_acknowledgement import HIUSubscriptionRequestNotificationAcknowledgement
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
    api_instance = abdm_gateway.HiuFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    hiu_subscription_request_notification_acknowledgement = abdm_gateway.HIUSubscriptionRequestNotificationAcknowledgement() # HIUSubscriptionRequestNotificationAcknowledgement | 

    try:
        # Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.
        api_instance.v05_subscription_requests_hiu_on_notify_post(authorization, x_cm_id, hiu_subscription_request_notification_acknowledgement)
    except Exception as e:
        print("Exception when calling HiuFacingApi->v05_subscription_requests_hiu_on_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **hiu_subscription_request_notification_acknowledgement** | [**HIUSubscriptionRequestNotificationAcknowledgement**](HIUSubscriptionRequestNotificationAcknowledgement.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted. |  -  |
**401** | **Causes:**   * Invalid/Expired/Empty token.  |  -  |
**500** | **Causes:**   * Downstream services are down  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_subscriptions_hiu_on_notify_post**
> v05_subscriptions_hiu_on_notify_post(authorization, x_cm_id, hiu_subscription_notification_acknowledgment)

Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.

This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hiu_subscription_notification_acknowledgment import HIUSubscriptionNotificationAcknowledgment
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
    api_instance = abdm_gateway.HiuFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    hiu_subscription_notification_acknowledgment = abdm_gateway.HIUSubscriptionNotificationAcknowledgment() # HIUSubscriptionNotificationAcknowledgment | 

    try:
        # Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.
        api_instance.v05_subscriptions_hiu_on_notify_post(authorization, x_cm_id, hiu_subscription_notification_acknowledgment)
    except Exception as e:
        print("Exception when calling HiuFacingApi->v05_subscriptions_hiu_on_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **hiu_subscription_notification_acknowledgment** | [**HIUSubscriptionNotificationAcknowledgment**](HIUSubscriptionNotificationAcknowledgment.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted. |  -  |
**401** | **Causes:**   * Invalid/Expired/Empty token.  |  -  |
**500** | **Causes:**   * Downstream services are down  |  -  |

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
    api_instance = abdm_gateway.HiuFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_auth_confirm_request = abdm_gateway.PatientAuthConfirmRequest() # PatientAuthConfirmRequest | 

    try:
        # Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation
        api_instance.v05_users_auth_confirm_post(authorization, x_cm_id, patient_auth_confirm_request)
    except Exception as e:
        print("Exception when calling HiuFacingApi->v05_users_auth_confirm_post: %s\n" % e)
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
    api_instance = abdm_gateway.HiuFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_auth_mode_query_request = abdm_gateway.PatientAuthModeQueryRequest() # PatientAuthModeQueryRequest | 

    try:
        # Get a patient's authentication modes relevant to specified purpose
        api_instance.v05_users_auth_fetch_modes_post(authorization, x_cm_id, patient_auth_mode_query_request)
    except Exception as e:
        print("Exception when calling HiuFacingApi->v05_users_auth_fetch_modes_post: %s\n" % e)
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
    api_instance = abdm_gateway.HiuFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_auth_init_request = abdm_gateway.PatientAuthInitRequest() # PatientAuthInitRequest | 

    try:
        # Initialize authentication from HIP
        api_instance.v05_users_auth_init_post(authorization, x_cm_id, patient_auth_init_request)
    except Exception as e:
        print("Exception when calling HiuFacingApi->v05_users_auth_init_post: %s\n" % e)
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
    api_instance = abdm_gateway.HiuFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_auth_notification_acknowledgement = abdm_gateway.PatientAuthNotificationAcknowledgement() # PatientAuthNotificationAcknowledgement | 

    try:
        # callback API by HIU/HIPs as acknowledgement of auth notification
        api_instance.v05_users_auth_on_notify_post(authorization, x_cm_id, patient_auth_notification_acknowledgement)
    except Exception as e:
        print("Exception when calling HiuFacingApi->v05_users_auth_on_notify_post: %s\n" % e)
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

