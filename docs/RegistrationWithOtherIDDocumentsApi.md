# abha.RegistrationWithOtherIDDocumentsApi

All URIs are relative to *http://healthidsbx.abdm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_health_id_using_post**](RegistrationWithOtherIDDocumentsApi.md#create_health_id_using_post) | **POST** /v2/document | Create ABHA Number using ID documents like Driving Licence, PAN Card
[**generate_mobile_otp_using_post4**](RegistrationWithOtherIDDocumentsApi.md#generate_mobile_otp_using_post4) | **POST** /v2/document/generate/mobile/otp | Generate Mobile OTP
[**validate_document_using_post**](RegistrationWithOtherIDDocumentsApi.md#validate_document_using_post) | **POST** /v2/document/validate | Validate the document. Match the provided demographic details (Name, DOB, Gender) against the document. It also checks for already created ABHA Number or Enrolment number against the document
[**verify_mobile_otp_using_post1**](RegistrationWithOtherIDDocumentsApi.md#verify_mobile_otp_using_post1) | **POST** /v2/document/verify/mobile/otp | Verify Mobile OTP


# **create_health_id_using_post**
> IdentityDocumentsBySelfResponse create_health_id_using_post(t_token, request, accept_language=accept_language)

Create ABHA Number using ID documents like Driving Licence, PAN Card

<b>Explanation</b> - Api Accepts <b>Identity Document details</b> and Creates HealthID for it.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Identity Document details</b> and Creates HealthID for it. Returns Error for <b>Invalid Identity Document details</b>.

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
    api_instance = abha.RegistrationWithOtherIDDocumentsApi(api_client)
    t_token = 'Bearer T-Token' # str | Transaction Token
    request = abha.IdentityDocumentsBySelfRequest() # IdentityDocumentsBySelfRequest | request
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Create ABHA Number using ID documents like Driving Licence, PAN Card
        api_response = api_instance.create_health_id_using_post(t_token, request, accept_language=accept_language)
        print("The response of RegistrationWithOtherIDDocumentsApi->create_health_id_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationWithOtherIDDocumentsApi->create_health_id_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | Return Identity Document details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not create Identity Document or Invalid request details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_mobile_otp_using_post4**
> TxnResponse generate_mobile_otp_using_post4(generate_otp_request, accept_language=accept_language)

Generate Mobile OTP

<b>Explanation</b> - Api Accepts <b>Mobile Number</b> and creates OTP fo it.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Mobile Number</b> and creates OTP fo it. Returns Error for <b>Invalid Mobile number</b>.

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
    api_instance = abha.RegistrationWithOtherIDDocumentsApi(api_client)
    generate_otp_request = abha.GenerateMobileOTPRequest() # GenerateMobileOTPRequest | generateOtpRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate Mobile OTP
        api_response = api_instance.generate_mobile_otp_using_post4(generate_otp_request, accept_language=accept_language)
        print("The response of RegistrationWithOtherIDDocumentsApi->generate_mobile_otp_using_post4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationWithOtherIDDocumentsApi->generate_mobile_otp_using_post4: %s\n" % e)
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
**422** | Could not generate OTP or Invalid Mobile number |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_document_using_post**
> ValidateIdentityDocumentsResponse validate_document_using_post(request, accept_language=accept_language)

Validate the document. Match the provided demographic details (Name, DOB, Gender) against the document. It also checks for already created ABHA Number or Enrolment number against the document

<b>Explanation</b> - API accepts <b>Identity Document details</b> and validates the document. Match the provided demographic details (Name, DOB, Gender) against document. It also check for the already created ABHA Number or Enrolment number against the document.    <b>Request Body</b> - Required    <b>Response</b> - API accepts <b>Identity Document details</b> and validates the document. Match the provided demographic details(Name, DOB, Gender) against document. It also check for the already created ABHA Number or Enrolment number against the document. Returns Error for <b>Invalid Identity Document details</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.validate_identity_documents_response import ValidateIdentityDocumentsResponse
from abha.models.verify_identity_documents_request import VerifyIdentityDocumentsRequest
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
    api_instance = abha.RegistrationWithOtherIDDocumentsApi(api_client)
    request = abha.VerifyIdentityDocumentsRequest() # VerifyIdentityDocumentsRequest | request
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Validate the document. Match the provided demographic details (Name, DOB, Gender) against the document. It also checks for already created ABHA Number or Enrolment number against the document
        api_response = api_instance.validate_document_using_post(request, accept_language=accept_language)
        print("The response of RegistrationWithOtherIDDocumentsApi->validate_document_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationWithOtherIDDocumentsApi->validate_document_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**VerifyIdentityDocumentsRequest**](VerifyIdentityDocumentsRequest.md)| request | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**ValidateIdentityDocumentsResponse**](ValidateIdentityDocumentsResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return Identity Document details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not find Identity Document or Invalid/UnRegistered/UnAutherised request details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_mobile_otp_using_post1**
> MobileVerificationToken verify_mobile_otp_using_post1(verify_mobile_web_request, accept_language=accept_language)

Verify Mobile OTP

<b>Explanation</b> - Api Accepts <b>Mobile OTP</b> and validates it.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Mobile OTP</b> and validates it. Returns Error for <b>Invalid Mobile OTP</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.mobile_verification_token import MobileVerificationToken
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
    api_instance = abha.RegistrationWithOtherIDDocumentsApi(api_client)
    verify_mobile_web_request = abha.VerifyMobileWebRequest() # VerifyMobileWebRequest | verifyMobileWebRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Verify Mobile OTP
        api_response = api_instance.verify_mobile_otp_using_post1(verify_mobile_web_request, accept_language=accept_language)
        print("The response of RegistrationWithOtherIDDocumentsApi->verify_mobile_otp_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationWithOtherIDDocumentsApi->verify_mobile_otp_using_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_mobile_web_request** | [**VerifyMobileWebRequest**](VerifyMobileWebRequest.md)| verifyMobileWebRequest | 
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
**200** | Return Verified Token in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Invalid/Expired OTP |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

