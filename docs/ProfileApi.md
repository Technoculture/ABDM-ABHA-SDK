# abha.ProfileApi

All URIs are relative to *http://healthidsbx.abdm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password_via_aadhar_using_post**](ProfileApi.md#change_password_via_aadhar_using_post) | **POST** /v1/account/change/passwd/byAadhaar | Change password via Aadhaar
[**change_password_via_mobile_using_post**](ProfileApi.md#change_password_via_mobile_using_post) | **POST** /v1/account/change/passwd/byMobile | Change password via mobile for heath id.
[**change_password_via_using_post**](ProfileApi.md#change_password_via_using_post) | **POST** /v1/account/change/password | Change password via password for heath id.
[**create_phr_adress_with_health_id_number_using_post**](ProfileApi.md#create_phr_adress_with_health_id_number_using_post) | **POST** /v1/account/update/phr-address | create ABHA Address With ABHA Number.
[**deactivate_account_using_post**](ProfileApi.md#deactivate_account_using_post) | **POST** /v2/account/profile/deactivate | Deactivate the account using mobile or aadhaar otp.
[**delete_account_using_post**](ProfileApi.md#delete_account_using_post) | **POST** /v2/account/profile/delete | Delete the account using mobile or aadhaar otp.
[**generate_aadhar_otp_using_get**](ProfileApi.md#generate_aadhar_otp_using_get) | **GET** /v1/account/change/passwd/generateAadhaarOTP | Generate Aadhaar OTP on Registered mobile number.
[**generate_card_using_get**](ProfileApi.md#generate_card_using_get) | **GET** /v1/account/getCard | Generate ABHA card in PDF format
[**generate_mobile_otp_using_get**](ProfileApi.md#generate_mobile_otp_using_get) | **GET** /v1/account/change/passwd/generateMobileOTP | Generate Mobile OTP to start registration.
[**generate_mobile_otp_using_post3**](ProfileApi.md#generate_mobile_otp_using_post3) | **POST** /v2/account/mobile/generateOTP | Generate Mobile OTP to start mobile txn.
[**generate_png_card_using_get**](ProfileApi.md#generate_png_card_using_get) | **GET** /v1/account/getPngCard | Generate ABHA card PNG
[**generate_svg_card_using_get**](ProfileApi.md#generate_svg_card_using_get) | **GET** /v1/account/getSvgCard | Generate ABHA card SVG
[**generatere_kyc_aadhar_otp_using_post**](ProfileApi.md#generatere_kyc_aadhar_otp_using_post) | **POST** /v1/account/aadhaar/generateOTP | Generate Aadhaar OTP on Registered for link account with aadhar number
[**generatere_kyc_aadhar_otp_using_post1**](ProfileApi.md#generatere_kyc_aadhar_otp_using_post1) | **POST** /v2/account/aadhaar/generateOTP | Generate Aadhaar OTP on mobile number linked with Aadhar
[**generatere_new_mobile_otp_using_post**](ProfileApi.md#generatere_new_mobile_otp_using_post) | **POST** /v2/account/change/mobile/new/generateOTP | Generate OTP on new mobile need to update existing account mobile number
[**get_account_information_using_get**](ProfileApi.md#get_account_information_using_get) | **GET** /v1/account/profile | Get account information.
[**get_benefits_using_get**](ProfileApi.md#get_benefits_using_get) | **GET** /v1/account/benefits | Get List of Benefits associated with HealthID.
[**get_qr_code_using_get**](ProfileApi.md#get_qr_code_using_get) | **GET** /v1/account/qrCode | Get Quick Response code in PNG format for this account.
[**logout_using_get**](ProfileApi.md#logout_using_get) | **GET** /v1/account/logout | Logout of account
[**phr_de_linked_using_post**](ProfileApi.md#phr_de_linked_using_post) | **POST** /v2/account/phr-delinked |  de-links the given ABHA Address from the ABHA number
[**phr_linked_using_post**](ProfileApi.md#phr_linked_using_post) | **POST** /v2/account/phr-linked |  links the given ABHA Address to the ABHA number
[**send_email_initiate_verification_e_mail_using_post**](ProfileApi.md#send_email_initiate_verification_e_mail_using_post) | **POST** /v2/account/email/verification/auth/initiate/send | Send the Email Verification Activation Link to verify the E-mail Address.
[**send_email_user_auth_verification_e_mail_using_post**](ProfileApi.md#send_email_user_auth_verification_e_mail_using_post) | **POST** /v2/account/email/verification/auth/verify | Verfiy the user initiate the Activation Link.
[**update_account_information_using_post**](ProfileApi.md#update_account_information_using_post) | **POST** /v1/account/profile | Update account information
[**validate_token_using_post**](ProfileApi.md#validate_token_using_post) | **POST** /v1/account/token | Validate auth token
[**verify_aadhar_otp_only_using_post1**](ProfileApi.md#verify_aadhar_otp_only_using_post1) | **POST** /v1/account/aadhaar/verifyOTP | Verify Aadhaar OTP to complete KYC/re-KYC verification.
[**verify_new_mobile_otp_using_post**](ProfileApi.md#verify_new_mobile_otp_using_post) | **POST** /v2/account/change/mobile/new/verifyOTP | Verify Mobile OTP to complete new mobile update verification.


# **change_password_via_aadhar_using_post**
> str change_password_via_aadhar_using_post(x_token, hid_otp_request_paylaod, accept_language=accept_language)

Change password via Aadhaar

<b>Explanation</b> - API accepts <b>Old And New Password and Aadhaar Transaction ID</b> and changes the Password via Aadhaar Transaction ID.    <b>Request Body</b> - Required    <b>Response</b> - API accepts <b>Old,New Pass. ,Aadhaar Transaction ID</b> and changes the Password via Aadhaar Transaction ID. Returns Error for <b>Unauthorized Aadhaar Transaction ID</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.hid_otp_request_paylaod import HidOtpRequestPaylaod
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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    hid_otp_request_paylaod = abha.HidOtpRequestPaylaod() # HidOtpRequestPaylaod | hidOtpRequestPaylaod
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Change password via Aadhaar
        api_response = api_instance.change_password_via_aadhar_using_post(x_token, hid_otp_request_paylaod, accept_language=accept_language)
        print("The response of ProfileApi->change_password_via_aadhar_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->change_password_via_aadhar_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **hid_otp_request_paylaod** | [**HidOtpRequestPaylaod**](HidOtpRequestPaylaod.md)| hidOtpRequestPaylaod | 
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
**200** | Return Status OK in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Change Password or Invalid Token |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password_via_mobile_using_post**
> str change_password_via_mobile_using_post(x_token, hid_otp_request_paylaod, accept_language=accept_language)

Change password via mobile for heath id.

<b>Explanation</b> - API accepts <b>Old And New Password and mobile number</b> and changes the Password via mobile number.    <b>Request Body</b> - Required    <b>Responce</b> - API accepts <b>Old And New Password and mobile number</b> and changes the Password via mobile number. Returns Error for <b>Unauthorized mobile </b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.hid_otp_request_paylaod import HidOtpRequestPaylaod
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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    hid_otp_request_paylaod = abha.HidOtpRequestPaylaod() # HidOtpRequestPaylaod | hidOtpRequestPaylaod
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Change password via mobile for heath id.
        api_response = api_instance.change_password_via_mobile_using_post(x_token, hid_otp_request_paylaod, accept_language=accept_language)
        print("The response of ProfileApi->change_password_via_mobile_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->change_password_via_mobile_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **hid_otp_request_paylaod** | [**HidOtpRequestPaylaod**](HidOtpRequestPaylaod.md)| hidOtpRequestPaylaod | 
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
**200** | Return Status OK in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Change Password or Invalid Token |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password_via_using_post**
> str change_password_via_using_post(x_token, health_facility_password_request, accept_language=accept_language)

Change password via password for heath id.

<b>Explanation</b> - Api Accepts <b>Old And New Password</b> and changes the Password via new password.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Old And New Password</b> and changes the Password via new password. Returns Error for <b>Unauthorized Password</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.hid_change_password_request_payload import HidChangePasswordRequestPayload
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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    health_facility_password_request = abha.HidChangePasswordRequestPayload() # HidChangePasswordRequestPayload | healthFacilityPasswordRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Change password via password for heath id.
        api_response = api_instance.change_password_via_using_post(x_token, health_facility_password_request, accept_language=accept_language)
        print("The response of ProfileApi->change_password_via_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->change_password_via_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **health_facility_password_request** | [**HidChangePasswordRequestPayload**](HidChangePasswordRequestPayload.md)| healthFacilityPasswordRequest | 
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
**200** | Return Status OK in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Change Password or Invalid Token |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_phr_adress_with_health_id_number_using_post**
> str create_phr_adress_with_health_id_number_using_post(x_token, accept_language=accept_language)

create ABHA Address With ABHA Number.

<b>Explanation</b> - API Accepts <b>ABHA Number and Creates ABHA Address</b>.    <b>Request Body</b> - Required    <b>Response</b> - API Accepts <b>ABHA Number and Creates ABHA Address</b>. Returns Error for <b>Invalid/Incorrect Info.</b>.

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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # create ABHA Address With ABHA Number.
        api_response = api_instance.create_phr_adress_with_health_id_number_using_post(x_token, accept_language=accept_language)
        print("The response of ProfileApi->create_phr_adress_with_health_id_number_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->create_phr_adress_with_health_id_number_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Created PHR. |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Created PHR. or Invalid/Incorrect Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_account_using_post**
> deactivate_account_using_post(x_token, deactivate_account_by_otp_web_request, accept_language=accept_language)

Deactivate the account using mobile or aadhaar otp.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.change_status_by_otp_account_request import ChangeStatusByOtpAccountRequest
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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer XToken' # str | Auth Token
    deactivate_account_by_otp_web_request = abha.ChangeStatusByOtpAccountRequest() # ChangeStatusByOtpAccountRequest | deactivateAccountByOtpWebRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Deactivate the account using mobile or aadhaar otp.
        api_instance.deactivate_account_using_post(x_token, deactivate_account_by_otp_web_request, accept_language=accept_language)
    except Exception as e:
        print("Exception when calling ProfileApi->deactivate_account_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **deactivate_account_by_otp_web_request** | [**ChangeStatusByOtpAccountRequest**](ChangeStatusByOtpAccountRequest.md)| deactivateAccountByOtpWebRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_using_post**
> delete_account_using_post(x_token, delete_account_by_otp_web_request, accept_language=accept_language)

Delete the account using mobile or aadhaar otp.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.change_status_by_otp_account_request import ChangeStatusByOtpAccountRequest
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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer XToken' # str | Auth Token
    delete_account_by_otp_web_request = abha.ChangeStatusByOtpAccountRequest() # ChangeStatusByOtpAccountRequest | deleteAccountByOtpWebRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Delete the account using mobile or aadhaar otp.
        api_instance.delete_account_using_post(x_token, delete_account_by_otp_web_request, accept_language=accept_language)
    except Exception as e:
        print("Exception when calling ProfileApi->delete_account_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **delete_account_by_otp_web_request** | [**ChangeStatusByOtpAccountRequest**](ChangeStatusByOtpAccountRequest.md)| deleteAccountByOtpWebRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_aadhar_otp_using_get**
> TxnResponse generate_aadhar_otp_using_get(x_token, accept_language=accept_language)

Generate Aadhaar OTP on Registered mobile number.

<b>Explanation</b> - API accepts <b>Auth Token</b> and creates Aadhaar OTP to start registration.    <b>Request Body</b> - Required    <b>Response</b> - API accepts <b>Auth Token</b> and creates Aadhaar OTP to start registration. Returns Error for <b>Unauthorized Token</b>.

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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate Aadhaar OTP on Registered mobile number.
        api_response = api_instance.generate_aadhar_otp_using_get(x_token, accept_language=accept_language)
        print("The response of ProfileApi->generate_aadhar_otp_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->generate_aadhar_otp_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
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
**200** | Return Transaction ID in case of success |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not generate OTP or Invalid Token |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_card_using_get**
> ByteArrayResource generate_card_using_get(x_token, accept_language=accept_language)

Generate ABHA card in PDF format

<b>Explanation</b> - Api Accepts <b>Auth Token</b> and then Returns Account Details for PDF format.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Auth Token</b> and then Returns Account Details for PDF format. Returns Error for <b>Unauthorized Auth Token</b>.

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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate ABHA card in PDF format
        api_response = api_instance.generate_card_using_get(x_token, accept_language=accept_language)
        print("The response of ProfileApi->generate_card_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->generate_card_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

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
**200** | Return details in case of success |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not generate Card or Invalid Token |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_mobile_otp_using_get**
> TxnResponse generate_mobile_otp_using_get(x_token, accept_language=accept_language)

Generate Mobile OTP to start registration.

<b>Explanation</b> - API accepts <b>Auth Token</b> and creates OTP to start registration.    <b>Request Body</b> - Required    <b>Responce</b> - API accepts <b>Auth Token</b> and creates OTP to start registration. Returns Error for <b>Unauthorized Token</b>.

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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate Mobile OTP to start registration.
        api_response = api_instance.generate_mobile_otp_using_get(x_token, accept_language=accept_language)
        print("The response of ProfileApi->generate_mobile_otp_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->generate_mobile_otp_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
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
**200** | Return Transaction ID in case of success |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not generate OTP or Invalid Token |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_mobile_otp_using_post3**
> TxnResponse generate_mobile_otp_using_post3(x_token, accept_language=accept_language)

Generate Mobile OTP to start mobile txn.

<b>Explanation</b> - Api Accepts <b>Auth Token</b> and Generates OTP on mobile number.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Auth Token</b> and Generates OTP on mobile number. Returns Error for <b>Unauthorized token </b>.

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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate Mobile OTP to start mobile txn.
        api_response = api_instance.generate_mobile_otp_using_post3(x_token, accept_language=accept_language)
        print("The response of ProfileApi->generate_mobile_otp_using_post3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->generate_mobile_otp_using_post3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
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
**200** | Return transaction id in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not create OTP Given Mobile |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_png_card_using_get**
> ByteArrayResource generate_png_card_using_get(x_token, accept_language=accept_language)

Generate ABHA card PNG

<b>Explanation</b> - Api Accepts <b>Auth Token</b> and then Returns Account Details for PNG format.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Auth Token</b> and then Returns Account Details for PNG format. Returns Error for <b>Unauthorized Auth Token</b>.

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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate ABHA card PNG
        api_response = api_instance.generate_png_card_using_get(x_token, accept_language=accept_language)
        print("The response of ProfileApi->generate_png_card_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->generate_png_card_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

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
**200** | Return details in case of success |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not generate Card or Invalid Token |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_svg_card_using_get**
> bytearray generate_svg_card_using_get(x_token, accept_language=accept_language)

Generate ABHA card SVG

<b>Explanation</b> - Api Accepts <b>Auth Token</b> and then Returns Account Details for SVG format.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Auth Token</b> and then Returns Account Details for SVG format. Returns Error for <b>Unauthorized Auth Token</b>.

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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate ABHA card SVG
        api_response = api_instance.generate_svg_card_using_get(x_token, accept_language=accept_language)
        print("The response of ProfileApi->generate_svg_card_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->generate_svg_card_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**bytearray**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return details in case of success |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not generate Card or Invalid Token |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generatere_kyc_aadhar_otp_using_post**
> TxnResponse generatere_kyc_aadhar_otp_using_post(x_token, aadhar_number_request_optional_payload, accept_language=accept_language)

Generate Aadhaar OTP on Registered for link account with aadhar number

<b>Explanation</b> - API accepts <b>Auth Token</b> and then Generates Aadhaar OTP for Registered Mobile number.    <b>Request Body</b> - Required    <b>Responce</b> - API accepts <b>Auth Token</b> and then Generates Aadhaar OTP for Registered Mobile number. Returns Error for <b>Unauthorized Token</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.aadhar_number_request_optional_payload import AadharNumberRequestOptionalPayload
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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    aadhar_number_request_optional_payload = abha.AadharNumberRequestOptionalPayload() # AadharNumberRequestOptionalPayload | aadharNumberRequestOptionalPayload
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate Aadhaar OTP on Registered for link account with aadhar number
        api_response = api_instance.generatere_kyc_aadhar_otp_using_post(x_token, aadhar_number_request_optional_payload, accept_language=accept_language)
        print("The response of ProfileApi->generatere_kyc_aadhar_otp_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->generatere_kyc_aadhar_otp_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **aadhar_number_request_optional_payload** | [**AadharNumberRequestOptionalPayload**](AadharNumberRequestOptionalPayload.md)| aadharNumberRequestOptionalPayload | 
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
**200** | Return Transaction ID in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not generate OTP or Invalid Token |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generatere_kyc_aadhar_otp_using_post1**
> TxnResponse generatere_kyc_aadhar_otp_using_post1(x_token, aadhar_number_web_optional_request_payload, accept_language=accept_language)

Generate Aadhaar OTP on mobile number linked with Aadhar

<b>Explanation</b> - API accepts <b>Auth Token</b> and Generates OTP on Linked mobile number.    <b>Request Body</b> - Required    <b>Response</b> - API accepts <b>Auth Token</b> and Generates OTP on Linked mobile number. Returns Error for <b>Unauthorized token </b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.aadhar_number_web_optional_request_payload import AadharNumberWebOptionalRequestPayload
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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    aadhar_number_web_optional_request_payload = abha.AadharNumberWebOptionalRequestPayload() # AadharNumberWebOptionalRequestPayload | aadharNumberWebOptionalRequestPayload
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate Aadhaar OTP on mobile number linked with Aadhar
        api_response = api_instance.generatere_kyc_aadhar_otp_using_post1(x_token, aadhar_number_web_optional_request_payload, accept_language=accept_language)
        print("The response of ProfileApi->generatere_kyc_aadhar_otp_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->generatere_kyc_aadhar_otp_using_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **aadhar_number_web_optional_request_payload** | [**AadharNumberWebOptionalRequestPayload**](AadharNumberWebOptionalRequestPayload.md)| aadharNumberWebOptionalRequestPayload | 
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
**200** | Return transaction id in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not find Registered Mobile number for given Aadhaar |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generatere_new_mobile_otp_using_post**
> TxnResponse generatere_new_mobile_otp_using_post(x_token, mobile_number_new_request_payload, accept_language=accept_language)

Generate OTP on new mobile need to update existing account mobile number

<b>Explanation</b> - Api Accepts <b>New Mobile Number and Auth Token</b> and creates OTP.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>New Mobile Number and Auth Token</b> and creates OTP. Returns Error for <b>Unauthorized Auth Token</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.mobile_number_new_request_payload import MobileNumberNewRequestPayload
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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    mobile_number_new_request_payload = abha.MobileNumberNewRequestPayload() # MobileNumberNewRequestPayload | mobileNumberNewRequestPayload
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate OTP on new mobile need to update existing account mobile number
        api_response = api_instance.generatere_new_mobile_otp_using_post(x_token, mobile_number_new_request_payload, accept_language=accept_language)
        print("The response of ProfileApi->generatere_new_mobile_otp_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->generatere_new_mobile_otp_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **mobile_number_new_request_payload** | [**MobileNumberNewRequestPayload**](MobileNumberNewRequestPayload.md)| mobileNumberNewRequestPayload | 
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
**200** | Return Trnsaction ID in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Invalid mobile number |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_information_using_get**
> UserDTO get_account_information_using_get(x_token, accept_language=accept_language)

Get account information.

<b>Explanation</b> - Api Accepts <b>Auth Token</b> and then Returns Account Details.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Auth Token</b> and then Returns Account Details. Returns Error for <b>Unauthorized Auth Token</b>.

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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer XToken' # str | Auth Token
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Get account information.
        api_response = api_instance.get_account_information_using_get(x_token, accept_language=accept_language)
        print("The response of ProfileApi->get_account_information_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_account_information_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | Return Account details in case of success |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Get account information or Invalid Token |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_benefits_using_get**
> BenefitDTO get_benefits_using_get(x_token, accept_language=accept_language)

Get List of Benefits associated with HealthID.

<b>Explanation</b> - API accepts <b>Auth Token</b> and returns List of Benefits associated with HealthID.    <b>Request Body</b> - Required    <b>Responce</b> - API accepts <b>Auth Token</b> and returns List of Benefits associated with HealthID. Returns Error for <b>Unauthorized token </b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.benefit_dto import BenefitDTO
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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer XToken' # str | Auth Token
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Get List of Benefits associated with HealthID.
        api_response = api_instance.get_benefits_using_get(x_token, accept_language=accept_language)
        print("The response of ProfileApi->get_benefits_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_benefits_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**BenefitDTO**](BenefitDTO.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return List of Benefit in case of success |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not get Benefit or Invalid Token |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_qr_code_using_get**
> bytearray get_qr_code_using_get(x_token, accept_language=accept_language)

Get Quick Response code in PNG format for this account.

<b>Explanation</b> - Api Accepts <b>Auth Token</b> and then returns Account Info for QR Code.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Auth Token</b> and then returns Account Info for QR Code. Returns Error for <b>Unauthorized Token</b>.

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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer XToken' # str | Auth Token
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Get Quick Response code in PNG format for this account.
        api_response = api_instance.get_qr_code_using_get(x_token, accept_language=accept_language)
        print("The response of ProfileApi->get_qr_code_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_qr_code_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | Return QR Code in Byte Array Form in case of success |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Expired or Invalid Token |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_using_get**
> logout_using_get(x_token, accept_language=accept_language)

Logout of account

<b>Explanation</b> - Api Accepts <b>Auth Token</b> and logout of the account.    <b>Request Body</b> - Required    <b>Response</b> - Api Accepts <b>Auth Token</b> and logout of the account. Returns Error for <b>Unauthorized token </b>.

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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer XToken' # str | Auth Token
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Logout of account
        api_instance.logout_using_get(x_token, accept_language=accept_language)
    except Exception as e:
        print("Exception when calling ProfileApi->logout_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return status ok in case of success |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Log out or Invalid Token |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phr_de_linked_using_post**
> bool phr_de_linked_using_post(x_token, phr_linked_or_de_linked_request_pay_load, accept_language=accept_language)

 de-links the given ABHA Address from the ABHA number

<b>Explanation</b> - API delinks a given ABHA Address from the ABHA number    <b>Request Body</b> - Required

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.phr_de_linked_request_pay_load import PhrDeLinkedRequestPayLoad
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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    phr_linked_or_de_linked_request_pay_load = abha.PhrDeLinkedRequestPayLoad() # PhrDeLinkedRequestPayLoad | phrLinkedOrDeLinkedRequestPayLoad
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        #  de-links the given ABHA Address from the ABHA number
        api_response = api_instance.phr_de_linked_using_post(x_token, phr_linked_or_de_linked_request_pay_load, accept_language=accept_language)
        print("The response of ProfileApi->phr_de_linked_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->phr_de_linked_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **phr_linked_or_de_linked_request_pay_load** | [**PhrDeLinkedRequestPayLoad**](PhrDeLinkedRequestPayLoad.md)| phrLinkedOrDeLinkedRequestPayLoad | 
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
**200** | Return status true in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | ABHA number is not available |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phr_linked_using_post**
> bool phr_linked_using_post(x_token, phr_linked_or_de_linked_request_pay_load, accept_language=accept_language)

 links the given ABHA Address to the ABHA number

<b>Explanation</b> - API links the given ABHA Address to the ABHA number and defines whether it is the preferred ABHA Address    <b>Request Body</b> - Required

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.phr_linked_or_de_linked_request_pay_load import PhrLinkedOrDeLinkedRequestPayLoad
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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    phr_linked_or_de_linked_request_pay_load = abha.PhrLinkedOrDeLinkedRequestPayLoad() # PhrLinkedOrDeLinkedRequestPayLoad | phrLinkedOrDeLinkedRequestPayLoad
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        #  links the given ABHA Address to the ABHA number
        api_response = api_instance.phr_linked_using_post(x_token, phr_linked_or_de_linked_request_pay_load, accept_language=accept_language)
        print("The response of ProfileApi->phr_linked_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->phr_linked_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **phr_linked_or_de_linked_request_pay_load** | [**PhrLinkedOrDeLinkedRequestPayLoad**](PhrLinkedOrDeLinkedRequestPayLoad.md)| phrLinkedOrDeLinkedRequestPayLoad | 
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
**200** | Return status true in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | ABHA number is not available |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_initiate_verification_e_mail_using_post**
> str send_email_initiate_verification_e_mail_using_post(x_token, accept_language=accept_language, request=request)

Send the Email Verification Activation Link to verify the E-mail Address.

<h2>Notes</h2>  <p>1: To verify the <b>Email Address</b> provided by the beneficiary during the <b style='color:black'>registration</b> process, Send the <b>Email Address</b> in the request.</p>  <p>2: Activation link will be expire in <strong style='color:red'>2 hours</strong>.</p><p>3: To regenerate the <b style='color:DodgerBlue'>Activation link</b> when the previous link is expired. Send the X-Token <sup style='color:red'>* required</sup> in the Header.</p>  <p>4: To <b style='color:red'>Update or Changes</b> the existing e-mail Address (Verified/Unverified email). Send the <b>New Email Address</b><sup style='color:red'>* required</sup> in the request.</p>  <p>5: To Generate the activation link user / OTP must be authorized

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.email_verification_otp_request import EmailVerificationOTPRequest
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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')
    request = abha.EmailVerificationOTPRequest() # EmailVerificationOTPRequest | request (optional)

    try:
        # Send the Email Verification Activation Link to verify the E-mail Address.
        api_response = api_instance.send_email_initiate_verification_e_mail_using_post(x_token, accept_language=accept_language, request=request)
        print("The response of ProfileApi->send_email_initiate_verification_e_mail_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->send_email_initiate_verification_e_mail_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **request** | [**EmailVerificationOTPRequest**](EmailVerificationOTPRequest.md)| request | [optional] 

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_user_auth_verification_e_mail_using_post**
> bool send_email_user_auth_verification_e_mail_using_post(x_token, request, accept_language=accept_language)

Verfiy the user initiate the Activation Link.

<h2>Notes</h2>  <p>1: To authenticate the user,Send the <b>Transaction Id</b><sup style='color:red'>* required</sup>  and <b>Authenticate Mode</b><sup style='color:red'>* required</sup>  in the request.</p>  <p>2: Valid modes of Authentication are <strong style='color:red'> MOBILE_OTP, AADHAAR_OTP, PASSWORD </strong>  <p>3: Send the X-Token<sup style='color:red'>* required</sup>.</p>  <p>4: <b>OTP/PASSWORD must be in encrypted form</b>, Plain Form OTP is not allowed</p>

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.verify_email_otp_request import VerifyEmailOTPRequest
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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    request = abha.VerifyEmailOTPRequest() # VerifyEmailOTPRequest | request
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Verfiy the user initiate the Activation Link.
        api_response = api_instance.send_email_user_auth_verification_e_mail_using_post(x_token, request, accept_language=accept_language)
        print("The response of ProfileApi->send_email_user_auth_verification_e_mail_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->send_email_user_auth_verification_e_mail_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **request** | [**VerifyEmailOTPRequest**](VerifyEmailOTPRequest.md)| request | 
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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_information_using_post**
> UserDTO update_account_information_using_post(x_token, request, accept_language=accept_language)

Update account information

<b>Explanation</b> - Api Accepts <b>Account Details</b> and then Updates Account Details Accordingly.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Account Details</b> and then Updates Account Details Accordingly. Returns Error for <b>Unauthorized Account Details</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.update_account_request import UpdateAccountRequest
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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    request = abha.UpdateAccountRequest() # UpdateAccountRequest | request
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Update account information
        api_response = api_instance.update_account_information_using_post(x_token, request, accept_language=accept_language)
        print("The response of ProfileApi->update_account_information_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->update_account_information_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **request** | [**UpdateAccountRequest**](UpdateAccountRequest.md)| request | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**UserDTO**](UserDTO.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return Account information in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Update account information or Invalid Token |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_token_using_post**
> bool validate_token_using_post(request, accept_language=accept_language)

Validate auth token

<b>Explanation</b> - Api Accepts <b>Auth Token</b> and then Checks is it Valid/Invalid/Expired.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Auth Token</b> and then Checks is it Valid/Invalid/Expired. Returns Error for <b>Unauthorized Token</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.validate_token_request import ValidateTokenRequest
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
    api_instance = abha.ProfileApi(api_client)
    request = abha.ValidateTokenRequest() # ValidateTokenRequest | request
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Validate auth token
        api_response = api_instance.validate_token_using_post(request, accept_language=accept_language)
        print("The response of ProfileApi->validate_token_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->validate_token_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ValidateTokenRequest**](ValidateTokenRequest.md)| request | 
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
**200** | Return Boolean value True in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Expired or Invalid Token |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_aadhar_otp_only_using_post1**
> bool verify_aadhar_otp_only_using_post1(x_token, verify_aadhaar_otp, accept_language=accept_language)

Verify Aadhaar OTP to complete KYC/re-KYC verification.

<b>Explanation</b> - API accepts <b>OTP</b> and Checks is it Valid/Invalid/Expired to complete KYC/re-KYC verification.    <b>Request Body</b> - Required    <b>Response</b> - API accepts <b>OTP</b> and checks is it Valid/Invalid/Expired to complete KYC/re-KYC verification. Returns Error for <b>Unauthorized OTP</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.verify_aadhaar_otp import VerifyAadhaarOtp
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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    verify_aadhaar_otp = abha.VerifyAadhaarOtp() # VerifyAadhaarOtp | verifyAadhaarOtp
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Verify Aadhaar OTP to complete KYC/re-KYC verification.
        api_response = api_instance.verify_aadhar_otp_only_using_post1(x_token, verify_aadhaar_otp, accept_language=accept_language)
        print("The response of ProfileApi->verify_aadhar_otp_only_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->verify_aadhar_otp_only_using_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **verify_aadhaar_otp** | [**VerifyAadhaarOtp**](VerifyAadhaarOtp.md)| verifyAadhaarOtp | 
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
**200** | Return Boolean value true in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Expired or Invalid OTP/Token |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_new_mobile_otp_using_post**
> TxnResponse verify_new_mobile_otp_using_post(x_token, verify_mobile_web_request, accept_language=accept_language)

Verify Mobile OTP to complete new mobile update verification.

<b>Explanation</b> - Api Accepts <b>New Mobile Number OTP</b> and Verifies it.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>New Mobile Number OTP</b> and Verifies it. Returns Error for <b>Unauthorized OTP</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.txn_response import TxnResponse
from abha.models.verify_mobile_web_request import VerifyMobileWebRequest
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
    api_instance = abha.ProfileApi(api_client)
    x_token = 'Bearer X-Token' # str | Auth Token
    verify_mobile_web_request = abha.VerifyMobileWebRequest() # VerifyMobileWebRequest | verifyAadhaarOtpWebPaylaod
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Verify Mobile OTP to complete new mobile update verification.
        api_response = api_instance.verify_new_mobile_otp_using_post(x_token, verify_mobile_web_request, accept_language=accept_language)
        print("The response of ProfileApi->verify_new_mobile_otp_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->verify_new_mobile_otp_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_token** | **str**| Auth Token | 
 **verify_mobile_web_request** | [**VerifyMobileWebRequest**](VerifyMobileWebRequest.md)| verifyAadhaarOtpWebPaylaod | 
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
**200** | Return Trnsaction ID in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Invalid mobile number |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

