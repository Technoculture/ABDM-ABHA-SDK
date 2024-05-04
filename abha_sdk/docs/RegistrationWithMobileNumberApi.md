# abha.RegistrationWithMobileNumberApi

All URIs are relative to *http://healthidsbx.abdm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_mobile_otp_using_post2**](RegistrationWithMobileNumberApi.md#generate_mobile_otp_using_post2) | **POST** /v1/registration/mobile/generateOtp | Generate Mobile OTP to start registration transaction
[**resent_otp_using_post**](RegistrationWithMobileNumberApi.md#resent_otp_using_post) | **POST** /v1/registration/mobile/resendOtp | Resend Mobile OTP in an existing transaction in case previous OTP is not received.
[**verify_mobile_otp_using_post**](RegistrationWithMobileNumberApi.md#verify_mobile_otp_using_post) | **POST** /v1/registration/mobile/verifyOtp | Verify Mobile OTP sent as part of registration transaction.
[**verify_user_via_mobile_using_post**](RegistrationWithMobileNumberApi.md#verify_user_via_mobile_using_post) | **POST** /v1/registration/mobile/createHealthId | Create ABHA number with verified mobile token


# **generate_mobile_otp_using_post2**
> TxnResponse generate_mobile_otp_using_post2(generate_otp_request, accept_language=accept_language)

Generate Mobile OTP to start registration transaction

<b>Explanation</b> - Api Accepts <b>Mobile Number</b> and then Generates <b>OTP</b> for it.    <b>Request Body</b> - Required    <b>Response</b> - Api Accepts <b>Mobile Number</b> and then Generates <b>OTP</b> for it. if number not found then throws error.

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
    api_instance = abha.RegistrationWithMobileNumberApi(api_client)
    generate_otp_request = abha.GenerateMobileOTPRequest() # GenerateMobileOTPRequest | generateOtpRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate Mobile OTP to start registration transaction
        api_response = api_instance.generate_mobile_otp_using_post2(generate_otp_request, accept_language=accept_language)
        print("The response of RegistrationWithMobileNumberApi->generate_mobile_otp_using_post2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationWithMobileNumberApi->generate_mobile_otp_using_post2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | Return transaction id in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Generate OTP or Mobile number may be Already Used. |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resent_otp_using_post**
> bool resent_otp_using_post(resend_request, accept_language=accept_language)

Resend Mobile OTP in an existing transaction in case previous OTP is not received.

<b>Explanation</b> - Api Resends <b>OTP</b> on <b>mobile number</b> to create ABHA number.    <b>Request Body</b> - Required    <b>Response</b> - Api Resends <b>OTP</b> on <b>mobile number</b> to create ABHA number. in case previous OTP is not received.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.mobile_resend_otp_request import MobileResendOTPRequest
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
    api_instance = abha.RegistrationWithMobileNumberApi(api_client)
    resend_request = abha.MobileResendOTPRequest() # MobileResendOTPRequest | resendRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Resend Mobile OTP in an existing transaction in case previous OTP is not received.
        api_response = api_instance.resent_otp_using_post(resend_request, accept_language=accept_language)
        print("The response of RegistrationWithMobileNumberApi->resent_otp_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationWithMobileNumberApi->resent_otp_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resend_request** | [**MobileResendOTPRequest**](MobileResendOTPRequest.md)| resendRequest | 
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
**422** | Could not Resend OTP or No Account Found with given Transaction. |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_mobile_otp_using_post**
> MobileVerificationToken verify_mobile_otp_using_post(verify_otp_request, accept_language=accept_language)

Verify Mobile OTP sent as part of registration transaction.

<b>Explanation</b> - Api Accepts <b>OTP</b> and then Checks <b>OTP</b> is Verified or Not    <b>Request Body</b> - Required    <b>Response</b> - Api Accepts <b>OTP</b> and then Checks <b>OTP</b> is Verified or Not. if it is not verified then it shows Error.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.mobile_verification_token import MobileVerificationToken
from abha.models.verify_mobile_request import VerifyMobileRequest
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
    api_instance = abha.RegistrationWithMobileNumberApi(api_client)
    verify_otp_request = abha.VerifyMobileRequest() # VerifyMobileRequest | verifyOtpRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Verify Mobile OTP sent as part of registration transaction.
        api_response = api_instance.verify_mobile_otp_using_post(verify_otp_request, accept_language=accept_language)
        print("The response of RegistrationWithMobileNumberApi->verify_mobile_otp_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationWithMobileNumberApi->verify_mobile_otp_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_otp_request** | [**VerifyMobileRequest**](VerifyMobileRequest.md)| verifyOtpRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**MobileVerificationToken**](MobileVerificationToken.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return Token in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Create Token or No Account Found with given Transaction. |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_user_via_mobile_using_post**
> CreateAccountJwtResponse verify_user_via_mobile_using_post(create_account_request, accept_language=accept_language)

Create ABHA number with verified mobile token

<b>Explanation</b> - Api Checks <b>Details</b> and creates ABHA number.    <b>Request Body</b> - Required    <b>Response</b> - Api Checks <b>Details</b> and creates ABHA number.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.create_account_by_verified_mobile_request import CreateAccountByVerifiedMobileRequest
from abha.models.create_account_jwt_response import CreateAccountJwtResponse
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
    api_instance = abha.RegistrationWithMobileNumberApi(api_client)
    create_account_request = abha.CreateAccountByVerifiedMobileRequest() # CreateAccountByVerifiedMobileRequest | createAccountRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Create ABHA number with verified mobile token
        api_response = api_instance.verify_user_via_mobile_using_post(create_account_request, accept_language=accept_language)
        print("The response of RegistrationWithMobileNumberApi->verify_user_via_mobile_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationWithMobileNumberApi->verify_user_via_mobile_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_account_request** | [**CreateAccountByVerifiedMobileRequest**](CreateAccountByVerifiedMobileRequest.md)| createAccountRequest | 
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
**200** | Return Account Details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Find Account or Non-Existing/Expired Tocken |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

