# abha.RegistrationWithAadhaarApi

All URIs are relative to *http://healthidsbx.abdm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_aadhaar_account_using_post**](RegistrationWithAadhaarApi.md#create_aadhaar_account_using_post) | **POST** /v1/registration/aadhaar/createHealthIdWithPreVerified | Create ABHA Number using pre-verified Aadhaar &amp; Mobile.
[**generate_aadhar_otp_using_post**](RegistrationWithAadhaarApi.md#generate_aadhar_otp_using_post) | **POST** /v1/registration/aadhaar/generateOtp | Generate Aadhaar OTP on Registered mobile number
[**generate_mobile_otp_for_txn_using_post**](RegistrationWithAadhaarApi.md#generate_mobile_otp_for_txn_using_post) | **POST** /v1/registration/aadhaar/generateMobileOTP | Generate Mobile OTP for verification
[**resend_aadhar_otp_using_post**](RegistrationWithAadhaarApi.md#resend_aadhar_otp_using_post) | **POST** /v1/registration/aadhaar/resendAadhaarOtp | Resend Aadhaar OTP on Registered mobile number to create ABHA Number
[**verify_aadhar_bio_using_post**](RegistrationWithAadhaarApi.md#verify_aadhar_bio_using_post) | **POST** /v1/registration/aadhaar/verifyBio | Verify Aadhaar using biometrics.
[**verify_aadhar_otp_only_using_post**](RegistrationWithAadhaarApi.md#verify_aadhar_otp_only_using_post) | **POST** /v1/registration/aadhaar/verifyOTP | Verify Aadhaar OTP received on Registered mobile number
[**verify_mobile_otp_for_txn_using_post**](RegistrationWithAadhaarApi.md#verify_mobile_otp_for_txn_using_post) | **POST** /v1/registration/aadhaar/verifyMobileOTP | Verify Mobile OTP in an existing transaction.


# **create_aadhaar_account_using_post**
> CreateAccountJwtResponse create_aadhaar_account_using_post(account_request, accept_language=accept_language)

Create ABHA Number using pre-verified Aadhaar & Mobile.

<b>Explanation</b> - API creates <b>ABHA Number</b> using <b>Aadhaar & Mobile</b> Which are already <b>Registered.</b>    <b>Request Body</b> - Required    <b>Response</b> - API creates <b>ABHA Number</b> using <b>Aadhaar & Mobile</b> Which are already <b>Registered.</b> gives Error for Non-Registered

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
    api_instance = abha.RegistrationWithAadhaarApi(api_client)
    account_request = abha.CreateAccountWithPreVerifiedAadhaar() # CreateAccountWithPreVerifiedAadhaar | accountRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Create ABHA Number using pre-verified Aadhaar & Mobile.
        api_response = api_instance.create_aadhaar_account_using_post(account_request, accept_language=accept_language)
        print("The response of RegistrationWithAadhaarApi->create_aadhaar_account_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationWithAadhaarApi->create_aadhaar_account_using_post: %s\n" % e)
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
**200** | Return Account Details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not find Account for given Aadhaar/Mobile. |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_aadhar_otp_using_post**
> TxnResponse generate_aadhar_otp_using_post(generate_otp_request, accept_language=accept_language)

Generate Aadhaar OTP on Registered mobile number

<b>Explanation</b> - API accepts <b>Aadhar Card Number</b> and then Generates <b>OTP</b> for Registered Mobile Number    <b>Request Body</b> - Required    <b>Response</b> - API accepts <b>Aadhar Card Number</b> and then Generates <b>OTP</b> for Regestered Mobile Number. If number not found then throws error.

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
    api_instance = abha.RegistrationWithAadhaarApi(api_client)
    generate_otp_request = abha.AadharOtpGenerateRequestPayLoad() # AadharOtpGenerateRequestPayLoad | generateOtpRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate Aadhaar OTP on Registered mobile number
        api_response = api_instance.generate_aadhar_otp_using_post(generate_otp_request, accept_language=accept_language)
        print("The response of RegistrationWithAadhaarApi->generate_aadhar_otp_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationWithAadhaarApi->generate_aadhar_otp_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | Returns transaction id in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not find Registered Mobile number for given Aadhaar |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_mobile_otp_for_txn_using_post**
> TxnResponse generate_mobile_otp_for_txn_using_post(request, accept_language=accept_language)

Generate Mobile OTP for verification

<b>Explanation</b> - API accepts <b>Mobile Number</b> and then creates <b>OTP</b> for it    <b>Request Body</b> - Required    <b>Response</b> - API creates <b>Mobile OTP</b> depend upon mobile number

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.generate_mobile_otp_for_txn_request import GenerateMobileOTPForTxnRequest
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
    api_instance = abha.RegistrationWithAadhaarApi(api_client)
    request = abha.GenerateMobileOTPForTxnRequest() # GenerateMobileOTPForTxnRequest | request
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate Mobile OTP for verification
        api_response = api_instance.generate_mobile_otp_for_txn_using_post(request, accept_language=accept_language)
        print("The response of RegistrationWithAadhaarApi->generate_mobile_otp_for_txn_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationWithAadhaarApi->generate_mobile_otp_for_txn_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GenerateMobileOTPForTxnRequest**](GenerateMobileOTPForTxnRequest.md)| request | 
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
**422** | Mobile number may not Registered |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_aadhar_otp_using_post**
> TxnResponse resend_aadhar_otp_using_post(request, accept_language=accept_language)

Resend Aadhaar OTP on Registered mobile number to create ABHA Number

<b>Explanation</b> - API Resends <b>Aadhaar OTP</b> on <b>Registered mobile number</b> to create ABHA Number    <b>Request Body</b> - Required    <b>Response</b> - API Resends <b>Aadhaar OTP</b> on <b>Registered mobile number</b> to create ABHA Number. Gives Error for Non-Registered.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.aadhaar_resend_otp_request import AadhaarResendOTPRequest
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
    api_instance = abha.RegistrationWithAadhaarApi(api_client)
    request = abha.AadhaarResendOTPRequest() # AadhaarResendOTPRequest | request
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Resend Aadhaar OTP on Registered mobile number to create ABHA Number
        api_response = api_instance.resend_aadhar_otp_using_post(request, accept_language=accept_language)
        print("The response of RegistrationWithAadhaarApi->resend_aadhar_otp_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationWithAadhaarApi->resend_aadhar_otp_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AadhaarResendOTPRequest**](AadhaarResendOTPRequest.md)| request | 
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
**200** | Return Account Details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not find Account for given Transaction. |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_aadhar_bio_using_post**
> TxnResponse verify_aadhar_bio_using_post(verify_aadhar_otp_request, accept_language=accept_language)

Verify Aadhaar using biometrics.

<b>Explanation</b> - API checks <b>Aadhaar</b> Using <b>Registered Biometrics</b>.    <b>Request Body</b> - Required    <b>Response</b> - API checks <b>Aadhaar</b> Using <b>Registered Biometrics</b>. Gives Error for Non-Registered.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.txn_response import TxnResponse
from abha.models.verify_aadhaar_with_bio import VerifyAadhaarWithBio
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
    api_instance = abha.RegistrationWithAadhaarApi(api_client)
    verify_aadhar_otp_request = abha.VerifyAadhaarWithBio() # VerifyAadhaarWithBio | verifyAadharOtpRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Verify Aadhaar using biometrics.
        api_response = api_instance.verify_aadhar_bio_using_post(verify_aadhar_otp_request, accept_language=accept_language)
        print("The response of RegistrationWithAadhaarApi->verify_aadhar_bio_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationWithAadhaarApi->verify_aadhar_bio_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_aadhar_otp_request** | [**VerifyAadhaarWithBio**](VerifyAadhaarWithBio.md)| verifyAadharOtpRequest | 
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
**422** | Could not find Transaction ID for given biometrics. |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_aadhar_otp_only_using_post**
> TxnResponse verify_aadhar_otp_only_using_post(verify_aadhaar_otp, accept_language=accept_language)

Verify Aadhaar OTP received on Registered mobile number

<b>Explanation</b> - API accepts <b>OTP</b> and then checks <b>OTP</b> is Verified or Not    <b>Request Body</b> - Required    <b>Response</b> - API accepts <b>OTP</b> and then checks <b>OTP</b> is Verified or Not. If it is not verified then it shows Error.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.txn_response import TxnResponse
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
    api_instance = abha.RegistrationWithAadhaarApi(api_client)
    verify_aadhaar_otp = abha.VerifyAadhaarOtp() # VerifyAadhaarOtp | verifyAadhaarOtp
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Verify Aadhaar OTP received on Registered mobile number
        api_response = api_instance.verify_aadhar_otp_only_using_post(verify_aadhaar_otp, accept_language=accept_language)
        print("The response of RegistrationWithAadhaarApi->verify_aadhar_otp_only_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationWithAadhaarApi->verify_aadhar_otp_only_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_aadhaar_otp** | [**VerifyAadhaarOtp**](VerifyAadhaarOtp.md)| verifyAadhaarOtp | 
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
**422** | OTP Expired or No transaction found for given OTP. |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_mobile_otp_for_txn_using_post**
> TxnResponse verify_mobile_otp_for_txn_using_post(request, accept_language=accept_language)

Verify Mobile OTP in an existing transaction.

<b>Explanation</b> - API accepts <b>Mobile OTP</b> and then checks it is <b>Verified</b> or Not.    <b>Request Body</b> - Required    <b>Response</b> - API accepts <b>Mobile OTP</b> and then checks it is <b>Verified</b> or Not. If it's not Verified it gives Error.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.txn_response import TxnResponse
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
    api_instance = abha.RegistrationWithAadhaarApi(api_client)
    request = abha.VerifyMobileRequest() # VerifyMobileRequest | request
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Verify Mobile OTP in an existing transaction.
        api_response = api_instance.verify_mobile_otp_for_txn_using_post(request, accept_language=accept_language)
        print("The response of RegistrationWithAadhaarApi->verify_mobile_otp_for_txn_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationWithAadhaarApi->verify_mobile_otp_for_txn_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**VerifyMobileRequest**](VerifyMobileRequest.md)| request | 
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
**422** | OTP Expired or No transaction found for given OTP. |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

