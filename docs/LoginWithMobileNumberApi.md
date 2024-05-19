# abha.LoginWithMobileNumberApi

All URIs are relative to *http://healthidsbx.abdm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_mobile_otp_using_post7**](LoginWithMobileNumberApi.md#generate_mobile_otp_using_post7) | **POST** /v2/registration/mobile/login/generateOtp | Generate Mobile OTP to start registration transaction
[**get_hid_info_using_post**](LoginWithMobileNumberApi.md#get_hid_info_using_post) | **POST** /v2/registration/mobile/login/userAuthorizedToken | Create ABHA Number with verified mobile token
[**resent_otp_using_post2**](LoginWithMobileNumberApi.md#resent_otp_using_post2) | **POST** /v2/registration/mobile/login/resendOtp | Resend Mobile OTP in an existing transaction in case previous OTP is not received.
[**verify_mobile_otp_using_post2**](LoginWithMobileNumberApi.md#verify_mobile_otp_using_post2) | **POST** /v2/registration/mobile/login/verifyOtp | Verify Mobile OTP sent as part of registration transaction.


# **generate_mobile_otp_using_post7**
> TxnResponse generate_mobile_otp_using_post7(generate_otp_request, accept_language=accept_language)

Generate Mobile OTP to start registration transaction

<b>Explanation</b> - API accepts <b>Mobile Number</b> and then Generates <b>OTP</b> for it.    <b>Request Body</b> - Required    <b>Response</b> - API accepts <b>Mobile Number</b> and then Generates <b>OTP</b> for it. if number not found then throws error.

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
    api_instance = abha.LoginWithMobileNumberApi(api_client)
    generate_otp_request = abha.GenerateMobileOTPRequest() # GenerateMobileOTPRequest | generateOtpRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate Mobile OTP to start registration transaction
        api_response = api_instance.generate_mobile_otp_using_post7(generate_otp_request, accept_language=accept_language)
        print("The response of LoginWithMobileNumberApi->generate_mobile_otp_using_post7:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginWithMobileNumberApi->generate_mobile_otp_using_post7: %s\n" % e)
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

# **get_hid_info_using_post**
> CreateAccountJwtResponse get_hid_info_using_post(t_token, mobile_login_web_request, accept_language=accept_language)

Create ABHA Number with verified mobile token

<b>Explanation</b> - API Checks <b>Details</b> and creates ABHA Number    <b>Request Body</b> - Required    <b>Response</b> - API Checks <b>Details</b> and creates ABHA Number

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.create_account_jwt_response import CreateAccountJwtResponse
from abha.models.mobile_login_web_request import MobileLoginWebRequest
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
    api_instance = abha.LoginWithMobileNumberApi(api_client)
    t_token = 'Bearer T-Token' # str | Transaction Token
    mobile_login_web_request = abha.MobileLoginWebRequest() # MobileLoginWebRequest | mobileLoginWebRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Create ABHA Number with verified mobile token
        api_response = api_instance.get_hid_info_using_post(t_token, mobile_login_web_request, accept_language=accept_language)
        print("The response of LoginWithMobileNumberApi->get_hid_info_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginWithMobileNumberApi->get_hid_info_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t_token** | **str**| Transaction Token | 
 **mobile_login_web_request** | [**MobileLoginWebRequest**](MobileLoginWebRequest.md)| mobileLoginWebRequest | 
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
**422** | Invalid Token or No Account Found with given Details. |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resent_otp_using_post2**
> bool resent_otp_using_post2(resend_request, accept_language=accept_language)

Resend Mobile OTP in an existing transaction in case previous OTP is not received.

<b>Explanation</b> - Api Resends <b>OTP</b> on <b>mobile number</b> to create ABHA number.    <b>Request Body</b> - Required    <b>Response</b> - Api Resends <b>OTP</b> on <b>mobile number</b> to create ABHA number. in case previous OTP is not received.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.resend_otp_request import ResendOTPRequest
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
    api_instance = abha.LoginWithMobileNumberApi(api_client)
    resend_request = abha.ResendOTPRequest() # ResendOTPRequest | resendRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Resend Mobile OTP in an existing transaction in case previous OTP is not received.
        api_response = api_instance.resent_otp_using_post2(resend_request, accept_language=accept_language)
        print("The response of LoginWithMobileNumberApi->resent_otp_using_post2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginWithMobileNumberApi->resent_otp_using_post2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resend_request** | [**ResendOTPRequest**](ResendOTPRequest.md)| resendRequest | 
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

# **verify_mobile_otp_using_post2**
> MobileVerificationToken2 verify_mobile_otp_using_post2(verify_mobile_web_request, accept_language=accept_language)

Verify Mobile OTP sent as part of registration transaction.

<b>Explanation</b> - API accepts <b>OTP</b> and then Checks <b>OTP</b> is Verified or Not    <b>Request Body</b> - Required    <b>Response</b> - API Accepts <b>OTP</b> and then Checks <b>OTP</b> is Verified or Not. if it is not verified then it shows Error.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.mobile_verification_token2 import MobileVerificationToken2
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
    api_instance = abha.LoginWithMobileNumberApi(api_client)
    verify_mobile_web_request = abha.VerifyMobileWebRequest() # VerifyMobileWebRequest | verifyMobileWebRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Verify Mobile OTP sent as part of registration transaction.
        api_response = api_instance.verify_mobile_otp_using_post2(verify_mobile_web_request, accept_language=accept_language)
        print("The response of LoginWithMobileNumberApi->verify_mobile_otp_using_post2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginWithMobileNumberApi->verify_mobile_otp_using_post2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_mobile_web_request** | [**VerifyMobileWebRequest**](VerifyMobileWebRequest.md)| verifyMobileWebRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**MobileVerificationToken2**](MobileVerificationToken2.md)

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
**422** | Non-Existing/Expired OTP or No Account Found with given Transaction. |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

