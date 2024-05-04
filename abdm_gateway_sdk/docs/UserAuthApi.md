# abdm_gateway.UserAuthApi

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_users_auth_confirm_post**](UserAuthApi.md#v05_users_auth_confirm_post) | **POST** /v0.5/users/auth/confirm | Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation
[**v05_users_auth_fetch_modes_post**](UserAuthApi.md#v05_users_auth_fetch_modes_post) | **POST** /v0.5/users/auth/fetch-modes | Get a patient&#39;s authentication modes relevant to specified purpose
[**v05_users_auth_init_post**](UserAuthApi.md#v05_users_auth_init_post) | **POST** /v0.5/users/auth/init | Initialize authentication from HIP
[**v05_users_auth_notify_post**](UserAuthApi.md#v05_users_auth_notify_post) | **POST** /v0.5/users/auth/notify | notification API in case of DIRECT mode of authentication by the CM
[**v05_users_auth_on_confirm_post**](UserAuthApi.md#v05_users_auth_on_confirm_post) | **POST** /v0.5/users/auth/on-confirm | callback API for /auth/confirm (in case of MEDIATED auth) to confirm user authentication or not
[**v05_users_auth_on_fetch_modes_post**](UserAuthApi.md#v05_users_auth_on_fetch_modes_post) | **POST** /v0.5/users/auth/on-fetch-modes | Identification result for a consent-manager user-id
[**v05_users_auth_on_init_post**](UserAuthApi.md#v05_users_auth_on_init_post) | **POST** /v0.5/users/auth/on-init | Response to user authentication initialization from HIP
[**v05_users_auth_on_notify_post**](UserAuthApi.md#v05_users_auth_on_notify_post) | **POST** /v0.5/users/auth/on-notify | callback API by HIU/HIPs as acknowledgement of auth notification


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
    api_instance = abdm_gateway.UserAuthApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_auth_confirm_request = abdm_gateway.PatientAuthConfirmRequest() # PatientAuthConfirmRequest | 

    try:
        # Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation
        api_instance.v05_users_auth_confirm_post(authorization, x_cm_id, patient_auth_confirm_request)
    except Exception as e:
        print("Exception when calling UserAuthApi->v05_users_auth_confirm_post: %s\n" % e)
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
    api_instance = abdm_gateway.UserAuthApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_auth_mode_query_request = abdm_gateway.PatientAuthModeQueryRequest() # PatientAuthModeQueryRequest | 

    try:
        # Get a patient's authentication modes relevant to specified purpose
        api_instance.v05_users_auth_fetch_modes_post(authorization, x_cm_id, patient_auth_mode_query_request)
    except Exception as e:
        print("Exception when calling UserAuthApi->v05_users_auth_fetch_modes_post: %s\n" % e)
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
    api_instance = abdm_gateway.UserAuthApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_auth_init_request = abdm_gateway.PatientAuthInitRequest() # PatientAuthInitRequest | 

    try:
        # Initialize authentication from HIP
        api_instance.v05_users_auth_init_post(authorization, x_cm_id, patient_auth_init_request)
    except Exception as e:
        print("Exception when calling UserAuthApi->v05_users_auth_init_post: %s\n" % e)
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
    api_instance = abdm_gateway.UserAuthApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    patient_auth_notification = abdm_gateway.PatientAuthNotification() # PatientAuthNotification | 

    try:
        # notification API in case of DIRECT mode of authentication by the CM
        api_instance.v05_users_auth_notify_post(authorization, x_hip_id, x_hiu_id, patient_auth_notification)
    except Exception as e:
        print("Exception when calling UserAuthApi->v05_users_auth_notify_post: %s\n" % e)
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
    api_instance = abdm_gateway.UserAuthApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    patient_auth_confirm_response = abdm_gateway.PatientAuthConfirmResponse() # PatientAuthConfirmResponse | 

    try:
        # callback API for /auth/confirm (in case of MEDIATED auth) to confirm user authentication or not
        api_instance.v05_users_auth_on_confirm_post(authorization, x_hip_id, x_hiu_id, patient_auth_confirm_response)
    except Exception as e:
        print("Exception when calling UserAuthApi->v05_users_auth_on_confirm_post: %s\n" % e)
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
    api_instance = abdm_gateway.UserAuthApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    patient_auth_mode_query_response = abdm_gateway.PatientAuthModeQueryResponse() # PatientAuthModeQueryResponse | 

    try:
        # Identification result for a consent-manager user-id
        api_instance.v05_users_auth_on_fetch_modes_post(authorization, x_hip_id, x_hiu_id, patient_auth_mode_query_response)
    except Exception as e:
        print("Exception when calling UserAuthApi->v05_users_auth_on_fetch_modes_post: %s\n" % e)
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
    api_instance = abdm_gateway.UserAuthApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hip_id = 'x_hip_id_example' # str | Identifier of the health information provider to which the request was intended.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    patient_auth_init_response = abdm_gateway.PatientAuthInitResponse() # PatientAuthInitResponse | 

    try:
        # Response to user authentication initialization from HIP
        api_instance.v05_users_auth_on_init_post(authorization, x_hip_id, x_hiu_id, patient_auth_init_response)
    except Exception as e:
        print("Exception when calling UserAuthApi->v05_users_auth_on_init_post: %s\n" % e)
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
    api_instance = abdm_gateway.UserAuthApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    patient_auth_notification_acknowledgement = abdm_gateway.PatientAuthNotificationAcknowledgement() # PatientAuthNotificationAcknowledgement | 

    try:
        # callback API by HIU/HIPs as acknowledgement of auth notification
        api_instance.v05_users_auth_on_notify_post(authorization, x_cm_id, patient_auth_notification_acknowledgement)
    except Exception as e:
        print("Exception when calling UserAuthApi->v05_users_auth_on_notify_post: %s\n" % e)
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

