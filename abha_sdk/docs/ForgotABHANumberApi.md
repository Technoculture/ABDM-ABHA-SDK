# abha.ForgotABHANumberApi

All URIs are relative to *http://healthidsbx.abdm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_aadhar_otp_using_post1**](ForgotABHANumberApi.md#generate_aadhar_otp_using_post1) | **POST** /v1/forgot/healthId/aadhaar/generateOtp | Generate Aadhaar OTP on Registered mobile number
[**generate_mobile_otp_using_post**](ForgotABHANumberApi.md#generate_mobile_otp_using_post) | **POST** /v1/forgot/healthId/mobile/generateOtp | Generate Mobile OTP as part of Forgot flow
[**retrieval_health_id_by_aadhar_using_post**](ForgotABHANumberApi.md#retrieval_health_id_by_aadhar_using_post) | **POST** /v1/forgot/healthId/aadhaar | Verify aadhar OTP sent as part of forget ABHA Number
[**retrieval_health_id_by_mobile_using_post**](ForgotABHANumberApi.md#retrieval_health_id_by_mobile_using_post) | **POST** /v1/forgot/healthId/mobile | Verify Mobile OTP sent as part of forget ABHA number


# **generate_aadhar_otp_using_post1**
> TxnResponse generate_aadhar_otp_using_post1(generate_otp_request, accept_language=accept_language)

Generate Aadhaar OTP on Registered mobile number

<b>Explanation</b> - API accepts <b>Aadhaar Number</b> and then generates OTP for linked number as part of Forgot flow.    <b>Request Body</b> - Required    <b>Response</b> - Api Accepts <b>Aadhaar Number</b> and then generates OTP for linked number as part of Forgot flow. Returns <b>Transaction ID</b>.

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
    api_instance = abha.ForgotABHANumberApi(api_client)
    generate_otp_request = abha.AadharOtpGenerateRequestPayLoad() # AadharOtpGenerateRequestPayLoad | generateOtpRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate Aadhaar OTP on Registered mobile number
        api_response = api_instance.generate_aadhar_otp_using_post1(generate_otp_request, accept_language=accept_language)
        print("The response of ForgotABHANumberApi->generate_aadhar_otp_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForgotABHANumberApi->generate_aadhar_otp_using_post1: %s\n" % e)
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
**200** | Return transaction id in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not find Registered Mobile number for given Aadhaar |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_mobile_otp_using_post**
> TxnResponse generate_mobile_otp_using_post(generate_otp_request, accept_language=accept_language)

Generate Mobile OTP as part of Forgot flow

<b>Explanation</b> - API accepts <b>Mobile Number</b> and then generates OTP for it.    <b>Request Body</b> - Required    <b>Responce</b> - API Accepts <b>Mobile Number</b> and then generates OTP for it. Returns <b>Transaction ID</b>.

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
    api_instance = abha.ForgotABHANumberApi(api_client)
    generate_otp_request = abha.GenerateMobileOTPRequest() # GenerateMobileOTPRequest | generateOtpRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate Mobile OTP as part of Forgot flow
        api_response = api_instance.generate_mobile_otp_using_post(generate_otp_request, accept_language=accept_language)
        print("The response of ForgotABHANumberApi->generate_mobile_otp_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForgotABHANumberApi->generate_mobile_otp_using_post: %s\n" % e)
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
**422** | Could not create OTP for given number or Mobile number invalid |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieval_health_id_by_aadhar_using_post**
> RetrieveHealthIdPayloadResponse retrieval_health_id_by_aadhar_using_post(auth_account_aadhaar_otp_request, accept_language=accept_language)

Verify aadhar OTP sent as part of forget ABHA Number

<b>Explanation</b> - API accepts <b>OTP</b> and then checks is it Valid as per given Aadhaar Transaction.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>OTP</b> then returns ABHA Number and ABHA Address accordingly.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.auth_account_aadhaar_otp_request import AuthAccountAadhaarOTPRequest
from abha.models.retrieve_health_id_payload_response import RetrieveHealthIdPayloadResponse
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
    api_instance = abha.ForgotABHANumberApi(api_client)
    auth_account_aadhaar_otp_request = abha.AuthAccountAadhaarOTPRequest() # AuthAccountAadhaarOTPRequest | authAccountAadhaarOTPRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Verify aadhar OTP sent as part of forget ABHA Number
        api_response = api_instance.retrieval_health_id_by_aadhar_using_post(auth_account_aadhaar_otp_request, accept_language=accept_language)
        print("The response of ForgotABHANumberApi->retrieval_health_id_by_aadhar_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForgotABHANumberApi->retrieval_health_id_by_aadhar_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_account_aadhaar_otp_request** | [**AuthAccountAadhaarOTPRequest**](AuthAccountAadhaarOTPRequest.md)| authAccountAadhaarOTPRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**RetrieveHealthIdPayloadResponse**](RetrieveHealthIdPayloadResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return ABHA number,number in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Expired or Invalid OTP |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieval_health_id_by_mobile_using_post**
> RetrieveHealthIdPayloadResponse retrieval_health_id_by_mobile_using_post(retrive_health_id_mobile_pay_load, accept_language=accept_language)

Verify Mobile OTP sent as part of forget ABHA number

<b>Explanation</b> - API accepts <b>OTP</b> and then checks is it Valid as per given Mobile Transaction.    <b>Request Body</b> - Required    <b>Response</b> - API accepts <b>OTP</b> then returns ABHA Number accordingly.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.retrieve_health_id_payload_response import RetrieveHealthIdPayloadResponse
from abha.models.retrive_health_id_mobile_pay_load import RetriveHealthIdMobilePayLoad
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
    api_instance = abha.ForgotABHANumberApi(api_client)
    retrive_health_id_mobile_pay_load = abha.RetriveHealthIdMobilePayLoad() # RetriveHealthIdMobilePayLoad | retriveHealthIdMobilePayLoad
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Verify Mobile OTP sent as part of forget ABHA number
        api_response = api_instance.retrieval_health_id_by_mobile_using_post(retrive_health_id_mobile_pay_load, accept_language=accept_language)
        print("The response of ForgotABHANumberApi->retrieval_health_id_by_mobile_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForgotABHANumberApi->retrieval_health_id_by_mobile_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retrive_health_id_mobile_pay_load** | [**RetriveHealthIdMobilePayLoad**](RetriveHealthIdMobilePayLoad.md)| retriveHealthIdMobilePayLoad | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**RetrieveHealthIdPayloadResponse**](RetrieveHealthIdPayloadResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return ABHA number,number in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Expired or Invalid OTP |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

