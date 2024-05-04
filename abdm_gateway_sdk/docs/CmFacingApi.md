# abdm_gateway.CmFacingApi

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_care_contexts_discover_post**](CmFacingApi.md#v05_care_contexts_discover_post) | **POST** /v0.5/care-contexts/discover | Discover patient&#39;s accounts
[**v05_care_contexts_on_discover_post**](CmFacingApi.md#v05_care_contexts_on_discover_post) | **POST** /v0.5/care-contexts/on-discover | Response to patient&#39;s account discovery request
[**v05_consent_requests_on_init_post**](CmFacingApi.md#v05_consent_requests_on_init_post) | **POST** /v0.5/consent-requests/on-init | Response to consent request
[**v05_consent_requests_on_status_post**](CmFacingApi.md#v05_consent_requests_on_status_post) | **POST** /v0.5/consent-requests/on-status | Result of consent request status
[**v05_consents_hip_notify_post**](CmFacingApi.md#v05_consents_hip_notify_post) | **POST** /v0.5/consents/hip/notify | Consent notification
[**v05_consents_hiu_notify_post**](CmFacingApi.md#v05_consents_hiu_notify_post) | **POST** /v0.5/consents/hiu/notify | Consent notification
[**v05_consents_on_fetch_post**](CmFacingApi.md#v05_consents_on_fetch_post) | **POST** /v0.5/consents/on-fetch | Result of fetch request for a consent artefact
[**v05_health_information_cm_on_request_post**](CmFacingApi.md#v05_health_information_cm_on_request_post) | **POST** /v0.5/health-information/cm/on-request | Health information data request
[**v05_health_information_hip_request_post**](CmFacingApi.md#v05_health_information_hip_request_post) | **POST** /v0.5/health-information/hip/request | Health information data request
[**v05_links_context_on_notify_post**](CmFacingApi.md#v05_links_context_on_notify_post) | **POST** /v0.5/links/context/on-notify | Acknowledgement sent by Consent Manager to HIP for data notification.
[**v05_links_link_confirm_post**](CmFacingApi.md#v05_links_link_confirm_post) | **POST** /v0.5/links/link/confirm | Token submission by Consent Manager for link confirmation
[**v05_links_link_init_post**](CmFacingApi.md#v05_links_link_init_post) | **POST** /v0.5/links/link/init | Link patient&#39;s care contexts
[**v05_links_link_on_add_contexts_post**](CmFacingApi.md#v05_links_link_on_add_contexts_post) | **POST** /v0.5/links/link/on-add-contexts | callback API for HIP initiated patient linking /link/add-context
[**v05_patients_on_find_post**](CmFacingApi.md#v05_patients_on_find_post) | **POST** /v0.5/patients/on-find | Identification result for a consent-manager user-id
[**v05_patients_profile_share_post**](CmFacingApi.md#v05_patients_profile_share_post) | **POST** /v0.5/patients/profile/share | Share patient profile details
[**v05_patients_sms_on_notify_post**](CmFacingApi.md#v05_patients_sms_on_notify_post) | **POST** /v0.5/patients/sms/on-notify | Acknowledgment response for SMS notification sent to patient by HIP
[**v05_patients_status_notify_post**](CmFacingApi.md#v05_patients_status_notify_post) | **POST** /v0.5/patients/status/notify | Notification sent by Consent MAnager
[**v05_subscription_requests_cm_on_init_post**](CmFacingApi.md#v05_subscription_requests_cm_on_init_post) | **POST** /v0.5/subscription-requests/cm/on-init | callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.
[**v05_subscription_requests_hiu_notify_post**](CmFacingApi.md#v05_subscription_requests_hiu_notify_post) | **POST** /v0.5/subscription-requests/hiu/notify | Notification for subscription grant/deny/revoke
[**v05_subscriptions_hiu_notify_post**](CmFacingApi.md#v05_subscriptions_hiu_notify_post) | **POST** /v0.5/subscriptions/hiu/notify | Notification to HIU on basis of a granted subscription
[**v05_users_auth_notify_post**](CmFacingApi.md#v05_users_auth_notify_post) | **POST** /v0.5/users/auth/notify | notification API in case of DIRECT mode of authentication by the CM
[**v05_users_auth_on_confirm_post**](CmFacingApi.md#v05_users_auth_on_confirm_post) | **POST** /v0.5/users/auth/on-confirm | callback API for /auth/confirm (in case of MEDIATED auth) to confirm user authentication or not
[**v05_users_auth_on_fetch_modes_post**](CmFacingApi.md#v05_users_auth_on_fetch_modes_post) | **POST** /v0.5/users/auth/on-fetch-modes | Identification result for a consent-manager user-id
[**v05_users_auth_on_init_post**](CmFacingApi.md#v05_users_auth_on_init_post) | **POST** /v0.5/users/auth/on-init | Response to user authentication initialization from HIP


# **v05_care_contexts_discover_post**
> v05_care_contexts_discover_post(authorization, x_hip_id, patient_discovery_request)

Discover patient's accounts

Request for patient care context discover, made by CM for a specific HIP. It is expected that HIP will subsequently return either zero or one patient record with (potentially masked) associated care contexts   1. **At least one of the verified identifier matches**   2. **Name (fuzzy), gender matches**   3. **If YoB was given, age band(+-2) matches**   4. **If unverified identifiers were given, one of them matches**   5. **If more than one patient records would be found after aforementioned steps, then patient who matches most verified and unverified identifiers would be returned.**   6. **If there would be still more than one patients (after ranking) error would be returned**   7. **Intended HIP should be able to resolve and identify results returned in the subsequent link confirmation request via the specified transactionId**   8. **Intended HIP should store the discovery results with transactionId and care contexts discovered for subsequent link initiation** 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_discovery_request import PatientDiscoveryRequest
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    patient_discovery_request = abdm_gateway.PatientDiscoveryRequest() # PatientDiscoveryRequest | 

    try:
        # Discover patient's accounts
        api_instance.v05_care_contexts_discover_post(authorization, x_hip_id, patient_discovery_request)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_care_contexts_discover_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **patient_discovery_request** | [**PatientDiscoveryRequest**](PatientDiscoveryRequest.md)|  | 

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
**400** | **Causes:**   * Empty verified identifiers.   * Format mismatch of any of attributes.     | type   | Format/Allowed Values|     | ------- | ----------------    |     | gender  | M/F/O/U |     | MOBILE  | valid mobile number with proper country code |  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_care_contexts_on_discover_post**
> v05_care_contexts_on_discover_post(authorization, x_cm_id, patient_discovery_result)

Response to patient's account discovery request

Result of patient care-context discovery request at HIP end. If a matching patient found with zero or more care contexts associated, it is specified as result attribute. If the prior discovery request, resulted in errors then it is specified in the error attribute. Reasons of errors can be    1. **more than one definitive match for the given request**    2. **no verified identifer was specified** 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_discovery_result import PatientDiscoveryResult
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_discovery_result = abdm_gateway.PatientDiscoveryResult() # PatientDiscoveryResult | 

    try:
        # Response to patient's account discovery request
        api_instance.v05_care_contexts_on_discover_post(authorization, x_cm_id, patient_discovery_result)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_care_contexts_on_discover_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **patient_discovery_result** | [**PatientDiscoveryResult**](PatientDiscoveryResult.md)|  | 

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

# **v05_consent_requests_on_init_post**
> v05_consent_requests_on_init_post(authorization, x_hiu_id, consent_request_init_response)

Response to consent request

Result of consent request creation for a patient. **consentRequest.id** represents the consentrequest id created by CM. The result must contain either **consentRequest** or the **error** caused. <br/>   Reasons for error may be   * Invalid references (e.g patient id, hiu id), purpose, hiTypes, ranges, persmission 

### Example


```python
import abdm_gateway
from abdm_gateway.models.consent_request_init_response import ConsentRequestInitResponse
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    consent_request_init_response = abdm_gateway.ConsentRequestInitResponse() # ConsentRequestInitResponse | 

    try:
        # Response to consent request
        api_instance.v05_consent_requests_on_init_post(authorization, x_hiu_id, consent_request_init_response)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_consent_requests_on_init_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **consent_request_init_response** | [**ConsentRequestInitResponse**](ConsentRequestInitResponse.md)|  | 

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

# **v05_consent_requests_on_status_post**
> v05_consent_requests_on_status_post(authorization, x_hiu_id, hiu_consent_request_status)

Result of consent request status

Result of consent request done previously. Status of request can be GRANTED,  DENIED, EXPIRED. If the request was GRANTED, then 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hiu_consent_request_status import HIUConsentRequestStatus
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    hiu_consent_request_status = abdm_gateway.HIUConsentRequestStatus() # HIUConsentRequestStatus | 

    try:
        # Result of consent request status
        api_instance.v05_consent_requests_on_status_post(authorization, x_hiu_id, hiu_consent_request_status)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_consent_requests_on_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **hiu_consent_request_status** | [**HIUConsentRequestStatus**](HIUConsentRequestStatus.md)|  | 

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

# **v05_consents_hip_notify_post**
> v05_consents_hip_notify_post(authorization, x_hip_id, hip_consent_notification)

Consent notification

Notification of consents to health information providers consent request granted, consent revoked, consent expired. Only the GRANTED, REVOKED and EXPIRED status notifications will be sent to HIP.   1. If consent is granted, status=GRANTED, then consentDetail contains the consent artefact details and signature is available.    2. If consent is revoked, then status=REVOKED, and consentId specifes which consent artefact is revoked.    3. If the consent has expired, then status=EXPIRED, and consentId specifies which consent artefact has expired. Note, this is also responsibility of the HIP to keep track of consent expiry. Any data request on expired consent artefact must not be done. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hip_consent_notification import HIPConsentNotification
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    hip_consent_notification = abdm_gateway.HIPConsentNotification() # HIPConsentNotification | 

    try:
        # Consent notification
        api_instance.v05_consents_hip_notify_post(authorization, x_hip_id, hip_consent_notification)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_consents_hip_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **hip_consent_notification** | [**HIPConsentNotification**](HIPConsentNotification.md)|  | 

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

# **v05_consents_hiu_notify_post**
> v05_consents_hiu_notify_post(authorization, x_hiu_id, hiu_consent_notification_event)

Consent notification

Health information user will get notified about the consent request granted or denied, consent revoked, consent expired.  1. For consent request grant, status=GRANTED, consentRequestId=<consent-request-id>, and consentArtefacts is an array of generated consent artefact Ids. 2. For consent request expiry, status=EXPIRED, consentRequestId=<consent-request-id> 3. For consent request denied, status=DENIED, consentRequestId=<consent-request-id> 4. For consent revocation, status=REVOKED, consentArtefacts is an array of revoked consent artefact ids 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hiu_consent_notification_event import HIUConsentNotificationEvent
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    hiu_consent_notification_event = abdm_gateway.HIUConsentNotificationEvent() # HIUConsentNotificationEvent | 

    try:
        # Consent notification
        api_instance.v05_consents_hiu_notify_post(authorization, x_hiu_id, hiu_consent_notification_event)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_consents_hiu_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **hiu_consent_notification_event** | [**HIUConsentNotificationEvent**](HIUConsentNotificationEvent.md)|  | 

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

# **v05_consents_on_fetch_post**
> v05_consents_on_fetch_post(authorization, x_hiu_id, consent_artefact_response)

Result of fetch request for a consent artefact

Must contain either consentDetail or error. Possible reason of errors are  1. consentId passed through /fetch is invalid 

### Example


```python
import abdm_gateway
from abdm_gateway.models.consent_artefact_response import ConsentArtefactResponse
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    consent_artefact_response = abdm_gateway.ConsentArtefactResponse() # ConsentArtefactResponse | 

    try:
        # Result of fetch request for a consent artefact
        api_instance.v05_consents_on_fetch_post(authorization, x_hiu_id, consent_artefact_response)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_consents_on_fetch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **consent_artefact_response** | [**ConsentArtefactResponse**](ConsentArtefactResponse.md)|  | 

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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    hiu_health_information_request_response = abdm_gateway.HIUHealthInformationRequestResponse() # HIUHealthInformationRequestResponse | 

    try:
        # Health information data request
        api_instance.v05_health_information_cm_on_request_post(authorization, x_hiu_id, hiu_health_information_request_response)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_health_information_cm_on_request_post: %s\n" % e)
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    hiphi_request = abdm_gateway.HIPHIRequest() # HIPHIRequest | 

    try:
        # Health information data request
        api_instance.v05_health_information_hip_request_post(authorization, x_hip_id, hiphi_request)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_health_information_hip_request_post: %s\n" % e)
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

# **v05_links_context_on_notify_post**
> v05_links_context_on_notify_post(authorization, x_hip_id, hip_data_notification_acknowledgement)

Acknowledgement sent by Consent Manager to HIP for data notification.

CM sends back acknowledgement of receiving data notification by HIPs. CM may return errors if in following scenarios:   1. **Patient id sent by HIP in the data notification is incorrect**   2. **Carecontext sent by HIP in the data notification is not linked or incorrect.** 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hip_data_notification_acknowledgement import HipDataNotificationAcknowledgement
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    hip_data_notification_acknowledgement = abdm_gateway.HipDataNotificationAcknowledgement() # HipDataNotificationAcknowledgement | 

    try:
        # Acknowledgement sent by Consent Manager to HIP for data notification.
        api_instance.v05_links_context_on_notify_post(authorization, x_hip_id, hip_data_notification_acknowledgement)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_links_context_on_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **hip_data_notification_acknowledgement** | [**HipDataNotificationAcknowledgement**](HipDataNotificationAcknowledgement.md)|  | 

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
**400** | **Causes:**   * resp not specified   * atleast acknowledgement or error should be specified  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_links_link_confirm_post**
> v05_links_link_confirm_post(authorization, x_hip_id, link_confirmation_request)

Token submission by Consent Manager for link confirmation

API to submit the token that was sent by HIP during the link request. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.link_confirmation_request import LinkConfirmationRequest
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    link_confirmation_request = abdm_gateway.LinkConfirmationRequest() # LinkConfirmationRequest | 

    try:
        # Token submission by Consent Manager for link confirmation
        api_instance.v05_links_link_confirm_post(authorization, x_hip_id, link_confirmation_request)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_links_link_confirm_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **link_confirmation_request** | [**LinkConfirmationRequest**](LinkConfirmationRequest.md)|  | 

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
**400** | **Causes:**   * Token is not provided  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_links_link_init_post**
> v05_links_link_init_post(authorization, x_hip_id, patient_link_reference_request)

Link patient's care contexts

Request from CM to links care contexts associated with only one patient   1. **Validate account reference number and care context reference number**   2. **Validate transactionId in the request with discovery request entry to check whether there was a discovery       and were these care contexts discovered or not for a given patient**   3. **Before eventual link confirmation, HIP needs to authenticate the request with the patient(eg: OTP verification)**   4. **HIP should communicate the mode of authentication of a successful request to Consent Manager** 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_link_reference_request import PatientLinkReferenceRequest
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    patient_link_reference_request = abdm_gateway.PatientLinkReferenceRequest() # PatientLinkReferenceRequest | 

    try:
        # Link patient's care contexts
        api_instance.v05_links_link_init_post(authorization, x_hip_id, patient_link_reference_request)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_links_link_init_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **patient_link_reference_request** | [**PatientLinkReferenceRequest**](PatientLinkReferenceRequest.md)|  | 

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
**400** | **Causes:**   * Consent manager user id is not provided   * Patient reference number is not provided   * Care context references are not provided  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_links_link_on_add_contexts_post**
> v05_links_link_on_add_contexts_post(authorization, x_hip_id, patient_care_context_link_response)

callback API for HIP initiated patient linking /link/add-context

If the accessToken is valid for purpose of linking, and specified details provided, CM will send \"acknoweldgement.status\" as SUCCESS. If any error occcurred, for example invalid token, or other required patient or care-context information not provided, then \"error\" attribute conveys so.    1. **accessToken must be valid and must be for the purpose of linking** 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_care_context_link_response import PatientCareContextLinkResponse
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    patient_care_context_link_response = abdm_gateway.PatientCareContextLinkResponse() # PatientCareContextLinkResponse | 

    try:
        # callback API for HIP initiated patient linking /link/add-context
        api_instance.v05_links_link_on_add_contexts_post(authorization, x_hip_id, patient_care_context_link_response)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_links_link_on_add_contexts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **patient_care_context_link_response** | [**PatientCareContextLinkResponse**](PatientCareContextLinkResponse.md)|  | 

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
**400** | **Causes:**   * resp not specified   * atleast acknowledgement or error should be specified  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_patients_on_find_post**
> v05_patients_on_find_post(authorization, patient_identification_response)

Identification result for a consent-manager user-id

If a patient is found then patient.name contains the patients name.  Otherwise, patient is not provided, and possibly error is raised for invalid requests Note in addition to the \"Authorization\" header, one of the following headers must be specified 1. specify **X-HIU-ID** if the requester is HIU (identified from /find requester.id) 2. specify **X-HIP-ID** if the requester is HIP (identified from /find requester.id) 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_identification_response import PatientIdentificationResponse
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    patient_identification_response = abdm_gateway.PatientIdentificationResponse() # PatientIdentificationResponse | 

    try:
        # Identification result for a consent-manager user-id
        api_instance.v05_patients_on_find_post(authorization, patient_identification_response)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_patients_on_find_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **patient_identification_response** | [**PatientIdentificationResponse**](PatientIdentificationResponse.md)|  | 

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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    share_profile_request = abdm_gateway.ShareProfileRequest() # ShareProfileRequest | 

    try:
        # Share patient profile details
        api_instance.v05_patients_profile_share_post(authorization, x_hip_id, share_profile_request)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_patients_profile_share_post: %s\n" % e)
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    patient_sms_notifcation_response = abdm_gateway.PatientSMSNotifcationResponse() # PatientSMSNotifcationResponse | 

    try:
        # Acknowledgment response for SMS notification sent to patient by HIP
        api_instance.v05_patients_sms_on_notify_post(authorization, x_hip_id, patient_sms_notifcation_response)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_patients_sms_on_notify_post: %s\n" % e)
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    patient_status_notification = abdm_gateway.PatientStatusNotification() # PatientStatusNotification | 

    try:
        # Notification sent by Consent MAnager
        api_instance.v05_patients_status_notify_post(authorization, x_hip_id, x_hiu_id, patient_status_notification)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_patients_status_notify_post: %s\n" % e)
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

# **v05_subscription_requests_cm_on_init_post**
> v05_subscription_requests_cm_on_init_post(authorization, x_hiu_id, hiu_subscription_request_receipt)

callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.

This callback API acknowledges the request for subscription from a HIU, and sends back a \"id\" that will be used when the patient/user approves or denies the subscription. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hiu_subscription_request_receipt import HIUSubscriptionRequestReceipt
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    hiu_subscription_request_receipt = abdm_gateway.HIUSubscriptionRequestReceipt() # HIUSubscriptionRequestReceipt | 

    try:
        # callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.
        api_instance.v05_subscription_requests_cm_on_init_post(authorization, x_hiu_id, hiu_subscription_request_receipt)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_subscription_requests_cm_on_init_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **hiu_subscription_request_receipt** | [**HIUSubscriptionRequestReceipt**](HIUSubscriptionRequestReceipt.md)|  | 

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

# **v05_subscription_requests_hiu_notify_post**
> v05_subscription_requests_hiu_notify_post(authorization, x_hiu_id, subscription_approval_notification)

Notification for subscription grant/deny/revoke

This API is used by CM to notify a HIU to grant or deny a request for subscription, and also to notify that in case an existing subscription is revoked or expired. For notifying that a particular subscription request was GRANTED or DENIED, the **subscriptionRequestId** is passed. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.subscription_approval_notification import SubscriptionApprovalNotification
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    subscription_approval_notification = abdm_gateway.SubscriptionApprovalNotification() # SubscriptionApprovalNotification | 

    try:
        # Notification for subscription grant/deny/revoke
        api_instance.v05_subscription_requests_hiu_notify_post(authorization, x_hiu_id, subscription_approval_notification)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_subscription_requests_hiu_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **subscription_approval_notification** | [**SubscriptionApprovalNotification**](SubscriptionApprovalNotification.md)|  | 

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

# **v05_subscriptions_hiu_notify_post**
> v05_subscriptions_hiu_notify_post(authorization, x_hiu_id, hiu_subscription_notification)

Notification to HIU on basis of a granted subscription

This API is used by CM to notify a HIU for notification relevant to subscription. Notifications are sent to subscribed HIUs whenever a new care-context is linked or new data is available on an existing linked care-context.  1. if event.category = LINK, then only care-contexts are passed when new care-contexts are linked for patient.  2. If event.category = DATA, then hiTypes are passed. Care-context is passed only if the subscribed HIU has any valid consent for that care-context 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hiu_subscription_notification import HIUSubscriptionNotification
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    hiu_subscription_notification = abdm_gateway.HIUSubscriptionNotification() # HIUSubscriptionNotification | 

    try:
        # Notification to HIU on basis of a granted subscription
        api_instance.v05_subscriptions_hiu_notify_post(authorization, x_hiu_id, hiu_subscription_notification)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_subscriptions_hiu_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **hiu_subscription_notification** | [**HIUSubscriptionNotification**](HIUSubscriptionNotification.md)|  | 

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

# **v05_users_auth_notify_post**
> v05_users_auth_notify_post(authorization, x_hip_id, x_hiu_id, patient_auth_notification)

notification API in case of DIRECT mode of authentication by the CM

This API is called by CM to confirm authentication of users. The transactionId returned is same as that passed in /auth/on-init. The \"auth.status\" conveys whether the request was GRANTED or DENIED.    1. **auth.accessToken** - is specific to the purpose mentioned in the /auth/init. This token needs to be used for initiating the intended action. For example for HIP initiated linking of care-contexts   2. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.   3. The payload is conditional to the purpose of auth. If purpose specified in /auth/init is KYC or KYC_AND_LINK, then patient details are passed. **auth.accessToken** is passed only if the purpose is LINK or KYC_AND_LINK. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_auth_notification import PatientAuthNotification
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    patient_auth_notification = abdm_gateway.PatientAuthNotification() # PatientAuthNotification | 

    try:
        # notification API in case of DIRECT mode of authentication by the CM
        api_instance.v05_users_auth_notify_post(authorization, x_hip_id, x_hiu_id, patient_auth_notification)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_users_auth_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **patient_auth_notification** | [**PatientAuthNotification**](PatientAuthNotification.md)|  | 

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

# **v05_users_auth_on_confirm_post**
> v05_users_auth_on_confirm_post(authorization, x_hip_id, x_hiu_id, patient_auth_confirm_response)

callback API for /auth/confirm (in case of MEDIATED auth) to confirm user authentication or not

This API is called by CM to confirm authentication of users.    1. **auth.accessToken** - is specific to the purpose mentioned in the /auth/init. This token needs to be used for initiating the intended action. For example for HIP initiated linking of care-contexts   2. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_auth_confirm_response import PatientAuthConfirmResponse
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    patient_auth_confirm_response = abdm_gateway.PatientAuthConfirmResponse() # PatientAuthConfirmResponse | 

    try:
        # callback API for /auth/confirm (in case of MEDIATED auth) to confirm user authentication or not
        api_instance.v05_users_auth_on_confirm_post(authorization, x_hip_id, x_hiu_id, patient_auth_confirm_response)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_users_auth_on_confirm_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **patient_auth_confirm_response** | [**PatientAuthConfirmResponse**](PatientAuthConfirmResponse.md)|  | 

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

# **v05_users_auth_on_fetch_modes_post**
> v05_users_auth_on_fetch_modes_post(authorization, x_hip_id, x_hiu_id, patient_auth_mode_query_response)

Identification result for a consent-manager user-id

If a patient is found then **auth** attribute contains the supported modes for the specified purpose.  Otherwise, error is raised for invalid requests or for non-existent id. Note in addition to the \"Authorization\" header, one of the following headers must be specified 1. **X-HIU-ID** if the requester is HIU (identified from /auth/fetch-modes requester.id) 2. **X-HIP-ID** if the requester is HIP (identified from /auth/fetch-modes requester.id) 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_auth_mode_query_response import PatientAuthModeQueryResponse
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    patient_auth_mode_query_response = abdm_gateway.PatientAuthModeQueryResponse() # PatientAuthModeQueryResponse | 

    try:
        # Identification result for a consent-manager user-id
        api_instance.v05_users_auth_on_fetch_modes_post(authorization, x_hip_id, x_hiu_id, patient_auth_mode_query_response)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_users_auth_on_fetch_modes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **patient_auth_mode_query_response** | [**PatientAuthModeQueryResponse**](PatientAuthModeQueryResponse.md)|  | 

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

# **v05_users_auth_on_init_post**
> v05_users_auth_on_init_post(authorization, x_hip_id, x_hiu_id, patient_auth_init_response)

Response to user authentication initialization from HIP

If the patient's id is valid, CM will return a transactionId as initialization of user auth. If the request is valid, then 'auth.mode' will convey how the authentication should be done. The authentication can be *mediated* or *direct*. For mediated authentication modes, HIP or HIU is epected to send over relevant code (OTP/token) or demographic info via subsequent API call to /auth/confirm. for direct authentication case, CM will notify requester through/users/auth/notify API.     1. **auth.mode** conveys whats the mode of authentication is, and what is expected from HIP/HIU in the subsequent /auth/confirm API call. Possible values        1. MOBILE_OTP - auth via OTP to registered mobile. Mediated.        2. AADHAAR_OTP - auth initiated with Aadhaar with OTP. Mediated.        3. DEMOGRAPHICS - auth initiated with demographic verification       4. DIRECT - for authentication directly with the patient. e.g. Mobile App, SMS. In this case, the HIP/HIU is not expected to call subsequent /auth/confirm call. CM will do direct authentication with the User (e.g. Mobile App, SMS etc) and will notify requester   2. **meta.expiry** conveys the expiry time of the token and the authentication session   3. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.   The error section in the body, represents the potential errors that may have occurred. Possible reasons:   1. Patient id is invalid 

### Example


```python
import abdm_gateway
from abdm_gateway.models.patient_auth_init_response import PatientAuthInitResponse
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
    api_instance = abdm_gateway.CmFacingApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    patient_auth_init_response = abdm_gateway.PatientAuthInitResponse() # PatientAuthInitResponse | 

    try:
        # Response to user authentication initialization from HIP
        api_instance.v05_users_auth_on_init_post(authorization, x_hip_id, x_hiu_id, patient_auth_init_response)
    except Exception as e:
        print("Exception when calling CmFacingApi->v05_users_auth_on_init_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hip_id** | **str**| Identifier of the health information provider to which the request was intended. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **patient_auth_init_response** | [**PatientAuthInitResponse**](PatientAuthInitResponse.md)|  | 

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
**400** | **Causes:**   * required information not provided   * neither authInit nor error specified  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

