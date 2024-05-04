# abdm_gateway.LinkApi

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_links_context_notify_post**](LinkApi.md#v05_links_context_notify_post) | **POST** /v0.5/links/context/notify | This API is meant to be called by HIPs when there is new health data generated for a patient, against a care context that is already linked to patient&#39;s ABDM account.
[**v05_links_context_on_notify_post**](LinkApi.md#v05_links_context_on_notify_post) | **POST** /v0.5/links/context/on-notify | Acknowledgement sent by Consent Manager to HIP for data notification.
[**v05_links_link_add_contexts_post**](LinkApi.md#v05_links_link_add_contexts_post) | **POST** /v0.5/links/link/add-contexts | API for HIP initiated care-context linking for patient
[**v05_links_link_confirm_post**](LinkApi.md#v05_links_link_confirm_post) | **POST** /v0.5/links/link/confirm | Token submission by Consent Manager for link confirmation
[**v05_links_link_init_post**](LinkApi.md#v05_links_link_init_post) | **POST** /v0.5/links/link/init | Link patient&#39;s care contexts
[**v05_links_link_on_add_contexts_post**](LinkApi.md#v05_links_link_on_add_contexts_post) | **POST** /v0.5/links/link/on-add-contexts | callback API for HIP initiated patient linking /link/add-context
[**v05_links_link_on_confirm_post**](LinkApi.md#v05_links_link_on_confirm_post) | **POST** /v0.5/links/link/on-confirm | Token authenticated by HIP, indicating completion of linkage of care-contexts
[**v05_links_link_on_init_post**](LinkApi.md#v05_links_link_on_init_post) | **POST** /v0.5/links/link/on-init | Response to patient&#39;s care context link request


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
    api_instance = abdm_gateway.LinkApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    hip_data_notification_request = abdm_gateway.HipDataNotificationRequest() # HipDataNotificationRequest | 

    try:
        # This API is meant to be called by HIPs when there is new health data generated for a patient, against a care context that is already linked to patient's ABDM account.
        api_instance.v05_links_context_notify_post(authorization, x_cm_id, hip_data_notification_request)
    except Exception as e:
        print("Exception when calling LinkApi->v05_links_context_notify_post: %s\n" % e)
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
    api_instance = abdm_gateway.LinkApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    hip_data_notification_acknowledgement = abdm_gateway.HipDataNotificationAcknowledgement() # HipDataNotificationAcknowledgement | 

    try:
        # Acknowledgement sent by Consent Manager to HIP for data notification.
        api_instance.v05_links_context_on_notify_post(authorization, x_hip_id, hip_data_notification_acknowledgement)
    except Exception as e:
        print("Exception when calling LinkApi->v05_links_context_on_notify_post: %s\n" % e)
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
    api_instance = abdm_gateway.LinkApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_care_context_link_request = abdm_gateway.PatientCareContextLinkRequest() # PatientCareContextLinkRequest | 

    try:
        # API for HIP initiated care-context linking for patient
        api_instance.v05_links_link_add_contexts_post(authorization, x_cm_id, patient_care_context_link_request)
    except Exception as e:
        print("Exception when calling LinkApi->v05_links_link_add_contexts_post: %s\n" % e)
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
    api_instance = abdm_gateway.LinkApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    link_confirmation_request = abdm_gateway.LinkConfirmationRequest() # LinkConfirmationRequest | 

    try:
        # Token submission by Consent Manager for link confirmation
        api_instance.v05_links_link_confirm_post(authorization, x_hip_id, link_confirmation_request)
    except Exception as e:
        print("Exception when calling LinkApi->v05_links_link_confirm_post: %s\n" % e)
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
    api_instance = abdm_gateway.LinkApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    patient_link_reference_request = abdm_gateway.PatientLinkReferenceRequest() # PatientLinkReferenceRequest | 

    try:
        # Link patient's care contexts
        api_instance.v05_links_link_init_post(authorization, x_hip_id, patient_link_reference_request)
    except Exception as e:
        print("Exception when calling LinkApi->v05_links_link_init_post: %s\n" % e)
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
    api_instance = abdm_gateway.LinkApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    patient_care_context_link_response = abdm_gateway.PatientCareContextLinkResponse() # PatientCareContextLinkResponse | 

    try:
        # callback API for HIP initiated patient linking /link/add-context
        api_instance.v05_links_link_on_add_contexts_post(authorization, x_hip_id, patient_care_context_link_response)
    except Exception as e:
        print("Exception when calling LinkApi->v05_links_link_on_add_contexts_post: %s\n" % e)
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
    api_instance = abdm_gateway.LinkApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_link_result = abdm_gateway.PatientLinkResult() # PatientLinkResult | 

    try:
        # Token authenticated by HIP, indicating completion of linkage of care-contexts
        api_instance.v05_links_link_on_confirm_post(authorization, x_cm_id, patient_link_result)
    except Exception as e:
        print("Exception when calling LinkApi->v05_links_link_on_confirm_post: %s\n" % e)
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
    api_instance = abdm_gateway.LinkApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_link_reference_result = abdm_gateway.PatientLinkReferenceResult() # PatientLinkReferenceResult | 

    try:
        # Response to patient's care context link request
        api_instance.v05_links_link_on_init_post(authorization, x_cm_id, patient_link_reference_result)
    except Exception as e:
        print("Exception when calling LinkApi->v05_links_link_on_init_post: %s\n" % e)
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

