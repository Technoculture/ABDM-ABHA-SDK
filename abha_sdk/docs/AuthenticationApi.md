# abha.AuthenticationApi

All URIs are relative to *http://healthidsbx.abdm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_with_mobile_token_using_post**](AuthenticationApi.md#auth_with_mobile_token_using_post) | **POST** /v1/auth/authWithMobileToken | Authenticate using verified Mobile Number and user data
[**authenticate_user_using_post**](AuthenticationApi.md#authenticate_user_using_post) | **POST** /v1/auth/authWithMobile | Authenticate request to generate Mobile OTP using ABHA number
[**authenticate_with_password_using_post**](AuthenticationApi.md#authenticate_with_password_using_post) | **POST** /v1/auth/authPassword | Authenticate using ABHA Number and password
[**cert_using_get**](AuthenticationApi.md#cert_using_get) | **GET** /v1/auth/cert | Authentication token public certificate. This certificate is also used to encrypt the data.
[**confirm_with_aadhaar_bio_using_post**](AuthenticationApi.md#confirm_with_aadhaar_bio_using_post) | **POST** /v1/auth/confirmWithAadhaarBio | Authentication with Aadhaar Biometric based auth transaction.
[**confirm_with_aadhaar_otp_using_post**](AuthenticationApi.md#confirm_with_aadhaar_otp_using_post) | **POST** /v1/auth/confirmWithAadhaarOtp | Authentication with Aadhaar OTP based auth transaction.
[**confirm_with_demographics_using_post**](AuthenticationApi.md#confirm_with_demographics_using_post) | **POST** /v1/auth/confirmWithDemographics | Authenticate using demographic data of user.
[**confirm_with_mobile_using_post**](AuthenticationApi.md#confirm_with_mobile_using_post) | **POST** /v1/auth/confirmWithMobileOTP | Authentication with Mobile OTP based auth transaction.
[**generate_access_token_using_post**](AuthenticationApi.md#generate_access_token_using_post) | **POST** /v1/auth/generate/access-token | create Access Token From Refresh Token
[**initiate_auth_using_post**](AuthenticationApi.md#initiate_auth_using_post) | **POST** /v1/auth/init | Initiate authentication process for a given ABHA Number
[**initiate_reactivate_auth_using_post**](AuthenticationApi.md#initiate_reactivate_auth_using_post) | **POST** /v2/auth/reactivate/init | Initiate authentication for reactivation of ABHA Number
[**reactivate_using_post**](AuthenticationApi.md#reactivate_using_post) | **POST** /v2/auth/reactivate | confirm reactivation txn with aadhar or mobile otp
[**resend_auth_mobile_otp_using_post**](AuthenticationApi.md#resend_auth_mobile_otp_using_post) | **POST** /v1/auth/resendAuthOTP | Resend Aadhaar/Mobile OTP for Authentication Transaction


# **auth_with_mobile_token_using_post**
> JwtResponse auth_with_mobile_token_using_post(auth_request, accept_language=accept_language)

Authenticate using verified Mobile Number and user data

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.auth_with_mobile_txn_and_user_data import AuthWithMobileTxnAndUserData
from abha.models.jwt_response import JwtResponse
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
    api_instance = abha.AuthenticationApi(api_client)
    auth_request = abha.AuthWithMobileTxnAndUserData() # AuthWithMobileTxnAndUserData | authRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Authenticate using verified Mobile Number and user data
        api_response = api_instance.auth_with_mobile_token_using_post(auth_request, accept_language=accept_language)
        print("The response of AuthenticationApi->auth_with_mobile_token_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_with_mobile_token_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_request** | [**AuthWithMobileTxnAndUserData**](AuthWithMobileTxnAndUserData.md)| authRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**JwtResponse**](JwtResponse.md)

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

# **authenticate_user_using_post**
> TxnResponse authenticate_user_using_post(auth_request, accept_language=accept_language)

Authenticate request to generate Mobile OTP using ABHA number

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.auth_mobile_otp_request import AuthMobileOTPRequest
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
    api_instance = abha.AuthenticationApi(api_client)
    auth_request = abha.AuthMobileOTPRequest() # AuthMobileOTPRequest | authRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Authenticate request to generate Mobile OTP using ABHA number
        api_response = api_instance.authenticate_user_using_post(auth_request, accept_language=accept_language)
        print("The response of AuthenticationApi->authenticate_user_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authenticate_user_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_request** | [**AuthMobileOTPRequest**](AuthMobileOTPRequest.md)| authRequest | 
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

# **authenticate_with_password_using_post**
> JwtResponse authenticate_with_password_using_post(authentication_request, accept_language=accept_language)

Authenticate using ABHA Number and password

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.jwt_request import JwtRequest
from abha.models.jwt_response import JwtResponse
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
    api_instance = abha.AuthenticationApi(api_client)
    authentication_request = abha.JwtRequest() # JwtRequest | authenticationRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Authenticate using ABHA Number and password
        api_response = api_instance.authenticate_with_password_using_post(authentication_request, accept_language=accept_language)
        print("The response of AuthenticationApi->authenticate_with_password_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authenticate_with_password_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentication_request** | [**JwtRequest**](JwtRequest.md)| authenticationRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**JwtResponse**](JwtResponse.md)

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

# **cert_using_get**
> str cert_using_get(accept_language=accept_language)

Authentication token public certificate. This certificate is also used to encrypt the data.

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
    api_instance = abha.AuthenticationApi(api_client)
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Authentication token public certificate. This certificate is also used to encrypt the data.
        api_response = api_instance.cert_using_get(accept_language=accept_language)
        print("The response of AuthenticationApi->cert_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->cert_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_with_aadhaar_bio_using_post**
> JwtResponse confirm_with_aadhaar_bio_using_post(authentication_request, accept_language=accept_language)

Authentication with Aadhaar Biometric based auth transaction.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.auth_account_aadhaar_bio_request import AuthAccountAadhaarBioRequest
from abha.models.jwt_response import JwtResponse
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
    api_instance = abha.AuthenticationApi(api_client)
    authentication_request = abha.AuthAccountAadhaarBioRequest() # AuthAccountAadhaarBioRequest | authenticationRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Authentication with Aadhaar Biometric based auth transaction.
        api_response = api_instance.confirm_with_aadhaar_bio_using_post(authentication_request, accept_language=accept_language)
        print("The response of AuthenticationApi->confirm_with_aadhaar_bio_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->confirm_with_aadhaar_bio_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentication_request** | [**AuthAccountAadhaarBioRequest**](AuthAccountAadhaarBioRequest.md)| authenticationRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**JwtResponse**](JwtResponse.md)

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

# **confirm_with_aadhaar_otp_using_post**
> JwtResponse confirm_with_aadhaar_otp_using_post(auth_account_aadhaar_otp_request, accept_language=accept_language)

Authentication with Aadhaar OTP based auth transaction.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.auth_account_aadhaar_otp_request import AuthAccountAadhaarOTPRequest
from abha.models.jwt_response import JwtResponse
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
    api_instance = abha.AuthenticationApi(api_client)
    auth_account_aadhaar_otp_request = abha.AuthAccountAadhaarOTPRequest() # AuthAccountAadhaarOTPRequest | authAccountAadhaarOTPRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Authentication with Aadhaar OTP based auth transaction.
        api_response = api_instance.confirm_with_aadhaar_otp_using_post(auth_account_aadhaar_otp_request, accept_language=accept_language)
        print("The response of AuthenticationApi->confirm_with_aadhaar_otp_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->confirm_with_aadhaar_otp_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_account_aadhaar_otp_request** | [**AuthAccountAadhaarOTPRequest**](AuthAccountAadhaarOTPRequest.md)| authAccountAadhaarOTPRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**JwtResponse**](JwtResponse.md)

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

# **confirm_with_demographics_using_post**
> str confirm_with_demographics_using_post(authentication_request, accept_language=accept_language)

Authenticate using demographic data of user.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.auth_account_with_demographics_request import AuthAccountWithDemographicsRequest
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
    api_instance = abha.AuthenticationApi(api_client)
    authentication_request = abha.AuthAccountWithDemographicsRequest() # AuthAccountWithDemographicsRequest | authenticationRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Authenticate using demographic data of user.
        api_response = api_instance.confirm_with_demographics_using_post(authentication_request, accept_language=accept_language)
        print("The response of AuthenticationApi->confirm_with_demographics_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->confirm_with_demographics_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentication_request** | [**AuthAccountWithDemographicsRequest**](AuthAccountWithDemographicsRequest.md)| authenticationRequest | 
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

# **confirm_with_mobile_using_post**
> JwtResponse confirm_with_mobile_using_post(auth_account_mobile_otp_request, accept_language=accept_language)

Authentication with Mobile OTP based auth transaction.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.auth_account_mobile_otp_request import AuthAccountMobileOTPRequest
from abha.models.jwt_response import JwtResponse
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
    api_instance = abha.AuthenticationApi(api_client)
    auth_account_mobile_otp_request = abha.AuthAccountMobileOTPRequest() # AuthAccountMobileOTPRequest | authAccountMobileOTPRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Authentication with Mobile OTP based auth transaction.
        api_response = api_instance.confirm_with_mobile_using_post(auth_account_mobile_otp_request, accept_language=accept_language)
        print("The response of AuthenticationApi->confirm_with_mobile_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->confirm_with_mobile_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_account_mobile_otp_request** | [**AuthAccountMobileOTPRequest**](AuthAccountMobileOTPRequest.md)| authAccountMobileOTPRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**JwtResponse**](JwtResponse.md)

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

# **generate_access_token_using_post**
> AccessTokenResponse generate_access_token_using_post(refresh_token_request, accept_language=accept_language)

create Access Token From Refresh Token

<b>Explanation</b> - API Accepts <b>Refresh Token and creates  Access Token</b>.    <b>Request Body</b> - Required    <b>Responce</b> - API accepts <b>Refresh Token and creates Access Token</b>. Returns Error for <b>Invalid/Incorrect Info.</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.access_token_response import AccessTokenResponse
from abha.models.refresh_token_request import RefreshTokenRequest
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
    api_instance = abha.AuthenticationApi(api_client)
    refresh_token_request = abha.RefreshTokenRequest() # RefreshTokenRequest | refreshTokenRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # create Access Token From Refresh Token
        api_response = api_instance.generate_access_token_using_post(refresh_token_request, accept_language=accept_language)
        print("The response of AuthenticationApi->generate_access_token_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->generate_access_token_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_request** | [**RefreshTokenRequest**](RefreshTokenRequest.md)| refreshTokenRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful. create Access Token. |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not create Access Token. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_auth_using_post**
> TxnResponse initiate_auth_using_post(auth_request, accept_language=accept_language)

Initiate authentication process for a given ABHA Number

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.auth_init_request import AuthInitRequest
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
    api_instance = abha.AuthenticationApi(api_client)
    auth_request = abha.AuthInitRequest() # AuthInitRequest | authRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Initiate authentication process for a given ABHA Number
        api_response = api_instance.initiate_auth_using_post(auth_request, accept_language=accept_language)
        print("The response of AuthenticationApi->initiate_auth_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->initiate_auth_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_request** | [**AuthInitRequest**](AuthInitRequest.md)| authRequest | 
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

# **initiate_reactivate_auth_using_post**
> TxnResponse initiate_reactivate_auth_using_post(auth_request, accept_language=accept_language)

Initiate authentication for reactivation of ABHA Number

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.auth_init_request import AuthInitRequest
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
    api_instance = abha.AuthenticationApi(api_client)
    auth_request = abha.AuthInitRequest() # AuthInitRequest | authRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Initiate authentication for reactivation of ABHA Number
        api_response = api_instance.initiate_reactivate_auth_using_post(auth_request, accept_language=accept_language)
        print("The response of AuthenticationApi->initiate_reactivate_auth_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->initiate_reactivate_auth_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_request** | [**AuthInitRequest**](AuthInitRequest.md)| authRequest | 
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
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactivate_using_post**
> JwtResponse reactivate_using_post(reactivate_by_otp_web_request, accept_language=accept_language)

confirm reactivation txn with aadhar or mobile otp

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.change_status_by_otp_account_request import ChangeStatusByOtpAccountRequest
from abha.models.jwt_response import JwtResponse
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
    api_instance = abha.AuthenticationApi(api_client)
    reactivate_by_otp_web_request = abha.ChangeStatusByOtpAccountRequest() # ChangeStatusByOtpAccountRequest | reactivateByOTPWebRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # confirm reactivation txn with aadhar or mobile otp
        api_response = api_instance.reactivate_using_post(reactivate_by_otp_web_request, accept_language=accept_language)
        print("The response of AuthenticationApi->reactivate_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->reactivate_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reactivate_by_otp_web_request** | [**ChangeStatusByOtpAccountRequest**](ChangeStatusByOtpAccountRequest.md)| reactivateByOTPWebRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**JwtResponse**](JwtResponse.md)

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
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_auth_mobile_otp_using_post**
> bool resend_auth_mobile_otp_using_post(resend_otp_request, accept_language=accept_language)

Resend Aadhaar/Mobile OTP for Authentication Transaction

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
    api_instance = abha.AuthenticationApi(api_client)
    resend_otp_request = abha.ResendOTPRequest() # ResendOTPRequest | resendOtpRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Resend Aadhaar/Mobile OTP for Authentication Transaction
        api_response = api_instance.resend_auth_mobile_otp_using_post(resend_otp_request, accept_language=accept_language)
        print("The response of AuthenticationApi->resend_auth_mobile_otp_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->resend_auth_mobile_otp_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resend_otp_request** | [**ResendOTPRequest**](ResendOTPRequest.md)| resendOtpRequest | 
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

