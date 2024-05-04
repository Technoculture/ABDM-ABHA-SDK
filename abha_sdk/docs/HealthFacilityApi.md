# abha.HealthFacilityApi

All URIs are relative to *http://healthidsbx.abdm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ack_face_auth_client_using_get**](HealthFacilityApi.md#ack_face_auth_client_using_get) | **GET** /v1/health/facility/faceAuth/ackSession | Accept or reject FaceAuth Client session
[**add_role_using_post**](HealthFacilityApi.md#add_role_using_post) | **POST** /v1/health/facility/add/role | Add a role for the facilty
[**authenticate_health_facility_using_post**](HealthFacilityApi.md#authenticate_health_facility_using_post) | **POST** /v1/health/facility/authenticate | Generate token for heath facility id.
[**change_password_using_post**](HealthFacilityApi.md#change_password_using_post) | **POST** /v1/health/facility/change/password | Change password for heath facility id.
[**confirm_with_mobile_using_post1**](HealthFacilityApi.md#confirm_with_mobile_using_post1) | **POST** /v1/health/facility/confirmWithMobileOTP | Verify otp to fetch the enrollment Id details
[**create_aadhaar_account_using_post1**](HealthFacilityApi.md#create_aadhaar_account_using_post1) | **POST** /v1/health/facility/createHealthIdWithPreVerified | Generate ABHA number card SVG
[**create_health_id_by_facility_using_post**](HealthFacilityApi.md#create_health_id_by_facility_using_post) | **POST** /v1/health/facility/create-hid | Create ABHA number by Facility manager
[**create_with_face_auth_using_post**](HealthFacilityApi.md#create_with_face_auth_using_post) | **POST** /v1/health/facility/faceAuth/capture | Capture Face Auth for KYC.
[**delete_by_enrollment_number_using_delete**](HealthFacilityApi.md#delete_by_enrollment_number_using_delete) | **DELETE** /v1/health/facility/enrollmentNumber/{enrollmentNumber} | Delete the provisional ID
[**fetch_by_document_number_using_get**](HealthFacilityApi.md#fetch_by_document_number_using_get) | **GET** /v1/health/facility | Fetch by Document Number
[**fetch_by_enrollment_id_using_get**](HealthFacilityApi.md#fetch_by_enrollment_id_using_get) | **GET** /v1/health/facility/generate/otp/enrollmentNumber/{enrollmentNumber} | Send the otp on linked mobile number
[**fetch_document_using_post**](HealthFacilityApi.md#fetch_document_using_post) | **POST** /v1/health/facility/find | Fetch The document from Document provider
[**generate_facility_otp_using_post**](HealthFacilityApi.md#generate_facility_otp_using_post) | **POST** /v1/health/facility/generate/aadharOtp | Generate health hacility OTP on registrered mobile number
[**generate_mobile_otp_using_post1**](HealthFacilityApi.md#generate_mobile_otp_using_post1) | **POST** /v1/health/facility/generate/mobileOtp | Generate health hacility create using mobile number
[**generate_password_using_post**](HealthFacilityApi.md#generate_password_using_post) | **POST** /v1/health/facility/generate/password | Generates password for heath facility id.
[**generate_pdf_card_using_get**](HealthFacilityApi.md#generate_pdf_card_using_get) | **GET** /v1/health/facility/getPdfCard | Generate ABHA number card in PDF format
[**generate_png_card_using_get1**](HealthFacilityApi.md#generate_png_card_using_get1) | **GET** /v1/health/facility/getPngCard | generatePngCard
[**get_qr_code_using_get1**](HealthFacilityApi.md#get_qr_code_using_get1) | **GET** /v1/health/facility/qrCode | Get Quick Response code in PNG format for this account.
[**health_facility_share_profile_using_post**](HealthFacilityApi.md#health_facility_share_profile_using_post) | **POST** /v1/health/facility/profile/share | Health hacility share profile
[**init_face_auth_session_using_get**](HealthFacilityApi.md#init_face_auth_session_using_get) | **GET** /v1/health/facility/faceAuth/initSession | Start new FaceAuth session
[**remove_role_using_post**](HealthFacilityApi.md#remove_role_using_post) | **POST** /v1/health/facility/remove/role | Remove the role for the facilty
[**reset_password_using_post**](HealthFacilityApi.md#reset_password_using_post) | **POST** /v1/health/facility/reset/password | Reset password for heath facility id.
[**update_health_id_by_self_using_put**](HealthFacilityApi.md#update_health_id_by_self_using_put) | **PUT** /v1/health/facility/hid/self | Update self created ABHA number.
[**update_health_id_status_using_get**](HealthFacilityApi.md#update_health_id_status_using_get) | **GET** /v1/health/facility/hid/self/verified | Verify the provisional ABHA number
[**verify_document_using_post**](HealthFacilityApi.md#verify_document_using_post) | **POST** /v1/health/facility/verify | Verify documents.
[**wait_for_face_auth_client_using_get**](HealthFacilityApi.md#wait_for_face_auth_client_using_get) | **GET** /v1/health/facility/faceAuth/waitSession | Wait for FaceAuth client to connect


# **ack_face_auth_client_using_get**
> TxnResponse ack_face_auth_client_using_get(f_token, ack, suid, accept_language=accept_language)

Accept or reject FaceAuth Client session

Accept or reject FaceAuth Client session.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.txn_response import TxnResponse
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer F-Token' # str | Auth Token
    ack = 'ack_example' # str | ack
    suid = 'suid_example' # str | suid
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Accept or reject FaceAuth Client session
        api_response = api_instance.ack_face_auth_client_using_get(f_token, ack, suid, accept_language=accept_language)
        print("The response of HealthFacilityApi->ack_face_auth_client_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->ack_face_auth_client_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **ack** | **str**| ack | 
 **suid** | **str**| suid | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role_using_post**
> bool add_role_using_post(f_token, facility_role_request, accept_language=accept_language)

Add a role for the facilty

Add a role for the facilty

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.health_facility_role_request import HealthFacilityRoleRequest
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer XToken' # str | Auth Token
    facility_role_request = abha.HealthFacilityRoleRequest() # HealthFacilityRoleRequest | facilityRoleRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Add a role for the facilty
        api_response = api_instance.add_role_using_post(f_token, facility_role_request, accept_language=accept_language)
        print("The response of HealthFacilityApi->add_role_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->add_role_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **facility_role_request** | [**HealthFacilityRoleRequest**](HealthFacilityRoleRequest.md)| facilityRoleRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**bool**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticate_health_facility_using_post**
> str authenticate_health_facility_using_post(health_facility_authentication_request, accept_language=accept_language)

Generate token for heath facility id.

Generate token for heath facility id.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.health_facility_authentication_request import HealthFacilityAuthenticationRequest
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    health_facility_authentication_request = abha.HealthFacilityAuthenticationRequest() # HealthFacilityAuthenticationRequest | healthFacilityAuthenticationRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate token for heath facility id.
        api_response = api_instance.authenticate_health_facility_using_post(health_facility_authentication_request, accept_language=accept_language)
        print("The response of HealthFacilityApi->authenticate_health_facility_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->authenticate_health_facility_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **health_facility_authentication_request** | [**HealthFacilityAuthenticationRequest**](HealthFacilityAuthenticationRequest.md)| healthFacilityAuthenticationRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password_using_post**
> str change_password_using_post(health_facility_password_request, accept_language=accept_language)

Change password for heath facility id.

Change password for heath facility id.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.health_facility_changed_password_request import HealthFacilityChangedPasswordRequest
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    health_facility_password_request = abha.HealthFacilityChangedPasswordRequest() # HealthFacilityChangedPasswordRequest | healthFacilityPasswordRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Change password for heath facility id.
        api_response = api_instance.change_password_using_post(health_facility_password_request, accept_language=accept_language)
        print("The response of HealthFacilityApi->change_password_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->change_password_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **health_facility_password_request** | [**HealthFacilityChangedPasswordRequest**](HealthFacilityChangedPasswordRequest.md)| healthFacilityPasswordRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_with_mobile_using_post1**
> IdentityDocumentsBySelfResponse confirm_with_mobile_using_post1(f_token, auth_account_mobile_otp_web_request, accept_language=accept_language)

Verify otp to fetch the enrollment Id details

Verify otp to fetch the enrollment Id details

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.auth_account_mobile_otp_web_request import AuthAccountMobileOtpWebRequest
from abha.models.identity_documents_by_self_response import IdentityDocumentsBySelfResponse
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer F-Token' # str | Auth Token
    auth_account_mobile_otp_web_request = abha.AuthAccountMobileOtpWebRequest() # AuthAccountMobileOtpWebRequest | authAccountMobileOtpWebRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Verify otp to fetch the enrollment Id details
        api_response = api_instance.confirm_with_mobile_using_post1(f_token, auth_account_mobile_otp_web_request, accept_language=accept_language)
        print("The response of HealthFacilityApi->confirm_with_mobile_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->confirm_with_mobile_using_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **auth_account_mobile_otp_web_request** | [**AuthAccountMobileOtpWebRequest**](AuthAccountMobileOtpWebRequest.md)| authAccountMobileOtpWebRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**IdentityDocumentsBySelfResponse**](IdentityDocumentsBySelfResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_aadhaar_account_using_post1**
> CreateAccountJwtResponse create_aadhaar_account_using_post1(account_request, accept_language=accept_language)

Generate ABHA number card SVG

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.create_account_jwt_response import CreateAccountJwtResponse
from abha.models.create_account_with_pre_verified_aadhaar import CreateAccountWithPreVerifiedAadhaar
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    account_request = abha.CreateAccountWithPreVerifiedAadhaar() # CreateAccountWithPreVerifiedAadhaar | accountRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate ABHA number card SVG
        api_response = api_instance.create_aadhaar_account_using_post1(account_request, accept_language=accept_language)
        print("The response of HealthFacilityApi->create_aadhaar_account_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->create_aadhaar_account_using_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_request** | [**CreateAccountWithPreVerifiedAadhaar**](CreateAccountWithPreVerifiedAadhaar.md)| accountRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**CreateAccountJwtResponse**](CreateAccountJwtResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_health_id_by_facility_using_post**
> IdentityDocumentsByFMResponse create_health_id_by_facility_using_post(f_token, t_token, request, accept_language=accept_language)

Create ABHA number by Facility manager

Create ABHA number by Facility manager

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.identity_documents_by_fm_request import IdentityDocumentsByFMRequest
from abha.models.identity_documents_by_fm_response import IdentityDocumentsByFMResponse
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer F-Token' # str | Auth Token
    t_token = 'Bearer T-Token' # str | Transaction Token
    request = abha.IdentityDocumentsByFMRequest() # IdentityDocumentsByFMRequest | request
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Create ABHA number by Facility manager
        api_response = api_instance.create_health_id_by_facility_using_post(f_token, t_token, request, accept_language=accept_language)
        print("The response of HealthFacilityApi->create_health_id_by_facility_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->create_health_id_by_facility_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **t_token** | **str**| Transaction Token | 
 **request** | [**IdentityDocumentsByFMRequest**](IdentityDocumentsByFMRequest.md)| request | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**IdentityDocumentsByFMResponse**](IdentityDocumentsByFMResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_with_face_auth_using_post**
> TxnResponse create_with_face_auth_using_post(f_token, suid, generate_otp_request, accept_language=accept_language)

Capture Face Auth for KYC.

Generate health facility OTP on registrered mobile number

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.aadhar_otp_generate_request_pay_load import AadharOtpGenerateRequestPayLoad
from abha.models.txn_response import TxnResponse
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer XToken' # str | Auth Token
    suid = 'suid_example' # str | suid
    generate_otp_request = abha.AadharOtpGenerateRequestPayLoad() # AadharOtpGenerateRequestPayLoad | generateOtpRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Capture Face Auth for KYC.
        api_response = api_instance.create_with_face_auth_using_post(f_token, suid, generate_otp_request, accept_language=accept_language)
        print("The response of HealthFacilityApi->create_with_face_auth_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->create_with_face_auth_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **suid** | **str**| suid | 
 **generate_otp_request** | [**AadharOtpGenerateRequestPayLoad**](AadharOtpGenerateRequestPayLoad.md)| generateOtpRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_by_enrollment_number_using_delete**
> bool delete_by_enrollment_number_using_delete(f_token, enrollment_number, accept_language=accept_language)

Delete the provisional ID

Delete the provisional ID

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer XToken' # str | Auth Token
    enrollment_number = 'enrollment_number_example' # str | enrollmentNumber
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Delete the provisional ID
        api_response = api_instance.delete_by_enrollment_number_using_delete(f_token, enrollment_number, accept_language=accept_language)
        print("The response of HealthFacilityApi->delete_by_enrollment_number_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->delete_by_enrollment_number_using_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **enrollment_number** | **str**| enrollmentNumber | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**bool**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_by_document_number_using_get**
> IdentityDocumentsByFMResponse fetch_by_document_number_using_get(f_token, document_number, document_type, accept_language=accept_language)

Fetch by Document Number

Fetch by Document Number

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.identity_documents_by_fm_response import IdentityDocumentsByFMResponse
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer F-Token' # str | Auth Token
    document_number = 'document_number_example' # str | documentNumber
    document_type = 'document_type_example' # str | documentType
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Fetch by Document Number
        api_response = api_instance.fetch_by_document_number_using_get(f_token, document_number, document_type, accept_language=accept_language)
        print("The response of HealthFacilityApi->fetch_by_document_number_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->fetch_by_document_number_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **document_number** | **str**| documentNumber | 
 **document_type** | **str**| documentType | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**IdentityDocumentsByFMResponse**](IdentityDocumentsByFMResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_by_enrollment_id_using_get**
> HidTxnResponse fetch_by_enrollment_id_using_get(f_token, enrollment_number, accept_language=accept_language)

Send the otp on linked mobile number

Send the otp on linked mobile number

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.hid_txn_response import HidTxnResponse
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer F-Token' # str | Auth Token
    enrollment_number = 'enrollment_number_example' # str | enrollmentNumber
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Send the otp on linked mobile number
        api_response = api_instance.fetch_by_enrollment_id_using_get(f_token, enrollment_number, accept_language=accept_language)
        print("The response of HealthFacilityApi->fetch_by_enrollment_id_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->fetch_by_enrollment_id_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **enrollment_number** | **str**| enrollmentNumber | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HidTxnResponse**](HidTxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_document_using_post**
> FetchDocumentResponse fetch_document_using_post(f_token, request, accept_language=accept_language)

Fetch The document from Document provider

Fetch The document from Document provider

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.fetch_document_request import FetchDocumentRequest
from abha.models.fetch_document_response import FetchDocumentResponse
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer F-Token' # str | Auth Token
    request = abha.FetchDocumentRequest() # FetchDocumentRequest | request
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Fetch The document from Document provider
        api_response = api_instance.fetch_document_using_post(f_token, request, accept_language=accept_language)
        print("The response of HealthFacilityApi->fetch_document_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->fetch_document_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **request** | [**FetchDocumentRequest**](FetchDocumentRequest.md)| request | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**FetchDocumentResponse**](FetchDocumentResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_facility_otp_using_post**
> TxnResponse generate_facility_otp_using_post(f_token, generate_otp_request, accept_language=accept_language)

Generate health hacility OTP on registrered mobile number

Generate health facility OTP on registrered mobile number

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.aadhar_otp_generate_request_pay_load import AadharOtpGenerateRequestPayLoad
from abha.models.txn_response import TxnResponse
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer XToken' # str | Auth Token
    generate_otp_request = abha.AadharOtpGenerateRequestPayLoad() # AadharOtpGenerateRequestPayLoad | generateOtpRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate health hacility OTP on registrered mobile number
        api_response = api_instance.generate_facility_otp_using_post(f_token, generate_otp_request, accept_language=accept_language)
        print("The response of HealthFacilityApi->generate_facility_otp_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->generate_facility_otp_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **generate_otp_request** | [**AadharOtpGenerateRequestPayLoad**](AadharOtpGenerateRequestPayLoad.md)| generateOtpRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_mobile_otp_using_post1**
> TxnResponse generate_mobile_otp_using_post1(f_token, generate_otp_request, accept_language=accept_language)

Generate health hacility create using mobile number

Generate health facility create using mobile number

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.generate_mobile_otp_request import GenerateMobileOTPRequest
from abha.models.txn_response import TxnResponse
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer F-Token' # str | Auth Token
    generate_otp_request = abha.GenerateMobileOTPRequest() # GenerateMobileOTPRequest | generateOtpRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate health hacility create using mobile number
        api_response = api_instance.generate_mobile_otp_using_post1(f_token, generate_otp_request, accept_language=accept_language)
        print("The response of HealthFacilityApi->generate_mobile_otp_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->generate_mobile_otp_using_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **generate_otp_request** | [**GenerateMobileOTPRequest**](GenerateMobileOTPRequest.md)| generateOtpRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_password_using_post**
> str generate_password_using_post(health_facility_password_request, accept_language=accept_language)

Generates password for heath facility id.

Generates password for heath facility id.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.health_facility_password_request import HealthFacilityPasswordRequest
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    health_facility_password_request = abha.HealthFacilityPasswordRequest() # HealthFacilityPasswordRequest | healthFacilityPasswordRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generates password for heath facility id.
        api_response = api_instance.generate_password_using_post(health_facility_password_request, accept_language=accept_language)
        print("The response of HealthFacilityApi->generate_password_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->generate_password_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **health_facility_password_request** | [**HealthFacilityPasswordRequest**](HealthFacilityPasswordRequest.md)| healthFacilityPasswordRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_pdf_card_using_get**
> UserDTO generate_pdf_card_using_get(f_token, x_token, accept_language=accept_language)

Generate ABHA number card in PDF format

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.user_dto import UserDTO
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer F-Token' # str | Auth Token
    x_token = 'Bearer X-Token' # str | Auth Token
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate ABHA number card in PDF format
        api_response = api_instance.generate_pdf_card_using_get(f_token, x_token, accept_language=accept_language)
        print("The response of HealthFacilityApi->generate_pdf_card_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->generate_pdf_card_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **x_token** | **str**| Auth Token | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**UserDTO**](UserDTO.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_png_card_using_get1**
> ByteArrayResource generate_png_card_using_get1(f_token, x_token, accept_language=accept_language, token=token)

generatePngCard

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.byte_array_resource import ByteArrayResource
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'BearerF-Token' # str | Auth Token
    x_token = 'Bearer X-Token' # str | Auth Token
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')
    token = 'token_example' # str |  (optional)

    try:
        # generatePngCard
        api_response = api_instance.generate_png_card_using_get1(f_token, x_token, accept_language=accept_language, token=token)
        print("The response of HealthFacilityApi->generate_png_card_using_get1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->generate_png_card_using_get1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **x_token** | **str**| Auth Token | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **token** | **str**|  | [optional] 

### Return type

[**ByteArrayResource**](ByteArrayResource.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_qr_code_using_get1**
> bytearray get_qr_code_using_get1(f_token, x_token, accept_language=accept_language)

Get Quick Response code in PNG format for this account.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer F-Token' # str | Auth Token
    x_token = 'Bearer X-Token' # str | Auth Token
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Get Quick Response code in PNG format for this account.
        api_response = api_instance.get_qr_code_using_get1(f_token, x_token, accept_language=accept_language)
        print("The response of HealthFacilityApi->get_qr_code_using_get1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->get_qr_code_using_get1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **x_token** | **str**| Auth Token | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**bytearray**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_facility_share_profile_using_post**
> HealthFacilityShareProfileResponse health_facility_share_profile_using_post(f_token, x_token, share_profile_request, accept_language=accept_language)

Health hacility share profile

Health hacility share profile

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.health_facility_share_profile_response import HealthFacilityShareProfileResponse
from abha.models.share_profile_request import ShareProfileRequest
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'BearerF-Token' # str | Auth Token
    x_token = 'BearerX-Token' # str | Auth Token
    share_profile_request = abha.ShareProfileRequest() # ShareProfileRequest | shareProfileRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Health hacility share profile
        api_response = api_instance.health_facility_share_profile_using_post(f_token, x_token, share_profile_request, accept_language=accept_language)
        print("The response of HealthFacilityApi->health_facility_share_profile_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->health_facility_share_profile_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **x_token** | **str**| Auth Token | 
 **share_profile_request** | [**ShareProfileRequest**](ShareProfileRequest.md)| shareProfileRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HealthFacilityShareProfileResponse**](HealthFacilityShareProfileResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_face_auth_session_using_get**
> TxnResponse init_face_auth_session_using_get(f_token, accept_language=accept_language)

Start new FaceAuth session

Generate Session QrCode

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.txn_response import TxnResponse
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer F-Token' # str | Auth Token
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Start new FaceAuth session
        api_response = api_instance.init_face_auth_session_using_get(f_token, accept_language=accept_language)
        print("The response of HealthFacilityApi->init_face_auth_session_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->init_face_auth_session_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_role_using_post**
> bool remove_role_using_post(f_token, facility_role_request, accept_language=accept_language)

Remove the role for the facilty

Remove the role for the facilty

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.health_facility_role_request import HealthFacilityRoleRequest
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer XToken' # str | Auth Token
    facility_role_request = abha.HealthFacilityRoleRequest() # HealthFacilityRoleRequest | facilityRoleRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Remove the role for the facilty
        api_response = api_instance.remove_role_using_post(f_token, facility_role_request, accept_language=accept_language)
        print("The response of HealthFacilityApi->remove_role_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->remove_role_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **facility_role_request** | [**HealthFacilityRoleRequest**](HealthFacilityRoleRequest.md)| facilityRoleRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**bool**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password_using_post**
> str reset_password_using_post(health_facility_password_request, accept_language=accept_language)

Reset password for heath facility id.

Reset password for heath facility id.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.health_facility_password_request import HealthFacilityPasswordRequest
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    health_facility_password_request = abha.HealthFacilityPasswordRequest() # HealthFacilityPasswordRequest | healthFacilityPasswordRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Reset password for heath facility id.
        api_response = api_instance.reset_password_using_post(health_facility_password_request, accept_language=accept_language)
        print("The response of HealthFacilityApi->reset_password_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->reset_password_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **health_facility_password_request** | [**HealthFacilityPasswordRequest**](HealthFacilityPasswordRequest.md)| healthFacilityPasswordRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_health_id_by_self_using_put**
> IdentityDocumentsBySelfResponse update_health_id_by_self_using_put(f_token, t_token, request, accept_language=accept_language)

Update self created ABHA number.

Update self created ABHA number.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.identity_documents_by_self_request import IdentityDocumentsBySelfRequest
from abha.models.identity_documents_by_self_response import IdentityDocumentsBySelfResponse
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer F-Token' # str | Auth Token
    t_token = 'Bearer T-Token' # str | Transaction Token
    request = abha.IdentityDocumentsBySelfRequest() # IdentityDocumentsBySelfRequest | request
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Update self created ABHA number.
        api_response = api_instance.update_health_id_by_self_using_put(f_token, t_token, request, accept_language=accept_language)
        print("The response of HealthFacilityApi->update_health_id_by_self_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->update_health_id_by_self_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **t_token** | **str**| Transaction Token | 
 **request** | [**IdentityDocumentsBySelfRequest**](IdentityDocumentsBySelfRequest.md)| request | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**IdentityDocumentsBySelfResponse**](IdentityDocumentsBySelfResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_health_id_status_using_get**
> update_health_id_status_using_get(f_token, x_token, accept_language=accept_language)

Verify the provisional ABHA number

Verify the provisional ABHA number

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer F-Token' # str | Auth Token
    x_token = 'Bearer X-Token' # str | Auth Token
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Verify the provisional ABHA number
        api_instance.update_health_id_status_using_get(f_token, x_token, accept_language=accept_language)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->update_health_id_status_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **x_token** | **str**| Auth Token | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_document_using_post**
> VerifyIdentityDocumentsResponse verify_document_using_post(f_token, request, accept_language=accept_language)

Verify documents.

Verify the documents.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.verify_identity_documents_request import VerifyIdentityDocumentsRequest
from abha.models.verify_identity_documents_response import VerifyIdentityDocumentsResponse
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer F-Token' # str | Auth Token
    request = abha.VerifyIdentityDocumentsRequest() # VerifyIdentityDocumentsRequest | request
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Verify documents.
        api_response = api_instance.verify_document_using_post(f_token, request, accept_language=accept_language)
        print("The response of HealthFacilityApi->verify_document_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->verify_document_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **request** | [**VerifyIdentityDocumentsRequest**](VerifyIdentityDocumentsRequest.md)| request | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**VerifyIdentityDocumentsResponse**](VerifyIdentityDocumentsResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wait_for_face_auth_client_using_get**
> TxnResponse wait_for_face_auth_client_using_get(f_token, suid, accept_language=accept_language)

Wait for FaceAuth client to connect

Wait for FaceAuth client to connect.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.txn_response import TxnResponse
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.HealthFacilityApi(api_client)
    f_token = 'Bearer F-Token' # str | Auth Token
    suid = 'suid_example' # str | suid
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Wait for FaceAuth client to connect
        api_response = api_instance.wait_for_face_auth_client_using_get(f_token, suid, accept_language=accept_language)
        print("The response of HealthFacilityApi->wait_for_face_auth_client_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthFacilityApi->wait_for_face_auth_client_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_token** | **str**| Auth Token | 
 **suid** | **str**| suid | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

