# abdm_gateway.ConsentFlowApi

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_consent_requests_init_post**](ConsentFlowApi.md#v05_consent_requests_init_post) | **POST** /v0.5/consent-requests/init | Create consent request
[**v05_consent_requests_on_init_post**](ConsentFlowApi.md#v05_consent_requests_on_init_post) | **POST** /v0.5/consent-requests/on-init | Response to consent request
[**v05_consent_requests_on_status_post**](ConsentFlowApi.md#v05_consent_requests_on_status_post) | **POST** /v0.5/consent-requests/on-status | Result of consent request status
[**v05_consent_requests_status_post**](ConsentFlowApi.md#v05_consent_requests_status_post) | **POST** /v0.5/consent-requests/status | Get consent request status
[**v05_consents_fetch_post**](ConsentFlowApi.md#v05_consents_fetch_post) | **POST** /v0.5/consents/fetch | Get consent artefact
[**v05_consents_hip_notify_post**](ConsentFlowApi.md#v05_consents_hip_notify_post) | **POST** /v0.5/consents/hip/notify | Consent notification
[**v05_consents_hip_on_notify_post**](ConsentFlowApi.md#v05_consents_hip_on_notify_post) | **POST** /v0.5/consents/hip/on-notify | Consent notification
[**v05_consents_hiu_notify_post**](ConsentFlowApi.md#v05_consents_hiu_notify_post) | **POST** /v0.5/consents/hiu/notify | Consent notification
[**v05_consents_hiu_on_notify_post**](ConsentFlowApi.md#v05_consents_hiu_on_notify_post) | **POST** /v0.5/consents/hiu/on-notify | Consent notification
[**v05_consents_on_fetch_post**](ConsentFlowApi.md#v05_consents_on_fetch_post) | **POST** /v0.5/consents/on-fetch | Result of fetch request for a consent artefact


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
    api_instance = abdm_gateway.ConsentFlowApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    consent_request = abdm_gateway.ConsentRequest() # ConsentRequest | 

    try:
        # Create consent request
        api_instance.v05_consent_requests_init_post(authorization, x_cm_id, consent_request)
    except Exception as e:
        print("Exception when calling ConsentFlowApi->v05_consent_requests_init_post: %s\n" % e)
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
    api_instance = abdm_gateway.ConsentFlowApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    consent_request_init_response = abdm_gateway.ConsentRequestInitResponse() # ConsentRequestInitResponse | 

    try:
        # Response to consent request
        api_instance.v05_consent_requests_on_init_post(authorization, x_hiu_id, consent_request_init_response)
    except Exception as e:
        print("Exception when calling ConsentFlowApi->v05_consent_requests_on_init_post: %s\n" % e)
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
    api_instance = abdm_gateway.ConsentFlowApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    hiu_consent_request_status = abdm_gateway.HIUConsentRequestStatus() # HIUConsentRequestStatus | 

    try:
        # Result of consent request status
        api_instance.v05_consent_requests_on_status_post(authorization, x_hiu_id, hiu_consent_request_status)
    except Exception as e:
        print("Exception when calling ConsentFlowApi->v05_consent_requests_on_status_post: %s\n" % e)
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
    api_instance = abdm_gateway.ConsentFlowApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    consent_request_status_request = abdm_gateway.ConsentRequestStatusRequest() # ConsentRequestStatusRequest | 

    try:
        # Get consent request status
        api_instance.v05_consent_requests_status_post(authorization, x_cm_id, consent_request_status_request)
    except Exception as e:
        print("Exception when calling ConsentFlowApi->v05_consent_requests_status_post: %s\n" % e)
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
    api_instance = abdm_gateway.ConsentFlowApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    consent_fetch_request = abdm_gateway.ConsentFetchRequest() # ConsentFetchRequest | 

    try:
        # Get consent artefact
        api_instance.v05_consents_fetch_post(authorization, x_cm_id, consent_fetch_request)
    except Exception as e:
        print("Exception when calling ConsentFlowApi->v05_consents_fetch_post: %s\n" % e)
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
    api_instance = abdm_gateway.ConsentFlowApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    hip_consent_notification = abdm_gateway.HIPConsentNotification() # HIPConsentNotification | 

    try:
        # Consent notification
        api_instance.v05_consents_hip_notify_post(authorization, x_hip_id, hip_consent_notification)
    except Exception as e:
        print("Exception when calling ConsentFlowApi->v05_consents_hip_notify_post: %s\n" % e)
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
    api_instance = abdm_gateway.ConsentFlowApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    hip_consent_notification_response = abdm_gateway.HIPConsentNotificationResponse() # HIPConsentNotificationResponse | 

    try:
        # Consent notification
        api_instance.v05_consents_hip_on_notify_post(authorization, x_cm_id, hip_consent_notification_response)
    except Exception as e:
        print("Exception when calling ConsentFlowApi->v05_consents_hip_on_notify_post: %s\n" % e)
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
    api_instance = abdm_gateway.ConsentFlowApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    hiu_consent_notification_event = abdm_gateway.HIUConsentNotificationEvent() # HIUConsentNotificationEvent | 

    try:
        # Consent notification
        api_instance.v05_consents_hiu_notify_post(authorization, x_hiu_id, hiu_consent_notification_event)
    except Exception as e:
        print("Exception when calling ConsentFlowApi->v05_consents_hiu_notify_post: %s\n" % e)
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
    api_instance = abdm_gateway.ConsentFlowApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    hiu_consent_notification_response = abdm_gateway.HIUConsentNotificationResponse() # HIUConsentNotificationResponse | 

    try:
        # Consent notification
        api_instance.v05_consents_hiu_on_notify_post(authorization, x_cm_id, hiu_consent_notification_response)
    except Exception as e:
        print("Exception when calling ConsentFlowApi->v05_consents_hiu_on_notify_post: %s\n" % e)
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
    api_instance = abdm_gateway.ConsentFlowApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    consent_artefact_response = abdm_gateway.ConsentArtefactResponse() # ConsentArtefactResponse | 

    try:
        # Result of fetch request for a consent artefact
        api_instance.v05_consents_on_fetch_post(authorization, x_hiu_id, consent_artefact_response)
    except Exception as e:
        print("Exception when calling ConsentFlowApi->v05_consents_on_fetch_post: %s\n" % e)
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

