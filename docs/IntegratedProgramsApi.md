# abha.IntegratedProgramsApi

All URIs are relative to *http://healthidsbx.abdm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_health_id_by_demo_auth_using_post**](IntegratedProgramsApi.md#create_health_id_by_demo_auth_using_post) | **POST** /v1/hid/benefit/createHealthId/demo/auth | Create ABHA Number using Aadhaar Demo Auth.
[**create_health_id_by_mobile_using_post**](IntegratedProgramsApi.md#create_health_id_by_mobile_using_post) | **POST** /v1/hid/benefit/mobile/createHealthId | Create ABHA number using mobile Authentication.
[**create_phr_adress_with_health_id_number_using_post1**](IntegratedProgramsApi.md#create_phr_adress_with_health_id_number_using_post1) | **POST** /v1/hid/benefit/update/phr-address | Create ABHA Address With ABHA Number
[**delink_hid_benefit_using_post**](IntegratedProgramsApi.md#delink_hid_benefit_using_post) | **POST** /v1/hid/benefit/delink | Delinks benefit programme from ABHA Number
[**delink_user_hid_benefit_using_post**](IntegratedProgramsApi.md#delink_user_hid_benefit_using_post) | **POST** /v1/hid/benefit/deLinkHid | Delinks benefit programme from ABHA Number
[**find_by_aadhar_using_post**](IntegratedProgramsApi.md#find_by_aadhar_using_post) | **POST** /v1/hid/benefit/search/aadhaar | Search ABHA number using Aadhaar or Aadhaar token
[**find_by_health_id_using_post**](IntegratedProgramsApi.md#find_by_health_id_using_post) | **POST** /v1/hid/benefit/search/healthIdNumber | Search benefit using ABHA number
[**generate_aadhar_otp_using_post2**](IntegratedProgramsApi.md#generate_aadhar_otp_using_post2) | **POST** /v1/hid/benefit/aadhaar/generateOtp | Generate Aadhaar OTP on Registered mobile number
[**generate_mobile_otp_using_post**](IntegratedProgramsApi.md#generate_mobile_otp_using_post) | **POST** /v1/hid/benefit/mobile/generateOtp | Generate mobile OTP on Registered mobile number
[**link_hid_benefit_using_post**](IntegratedProgramsApi.md#link_hid_benefit_using_post) | **POST** /v1/hid/benefit/link | Links benefit programme with ABHA Number
[**link_user_hid_benefit_using_post**](IntegratedProgramsApi.md#link_user_hid_benefit_using_post) | **POST** /v1/hid/benefit/linkHid | Link Benefit ID with ABHA Number after authentication.
[**notify_benefit_using_post**](IntegratedProgramsApi.md#notify_benefit_using_post) | **POST** /v1/hid/benefit/notify/benefit | Create ABHA number using notify Benefit.
[**update_account_information_using_post1**](IntegratedProgramsApi.md#update_account_information_using_post1) | **POST** /v1/hid/benefit/update/profile | Update account information
[**update_mobile_information_using_post**](IntegratedProgramsApi.md#update_mobile_information_using_post) | **POST** /v1/hid/benefit/update/mobile | Update mobile number for account.
[**update_status_using_post**](IntegratedProgramsApi.md#update_status_using_post) | **POST** /v1/hid/benefit/update/status | Update ABHA status
[**verify_aadhar_otp_using_post**](IntegratedProgramsApi.md#verify_aadhar_otp_using_post) | **POST** /v1/hid/benefit/aadhaar/verifyAadharOtp | Create ABHA Number using Aadhaar Number OTP
[**verify_bio_using_post**](IntegratedProgramsApi.md#verify_bio_using_post) | **POST** /v1/hid/benefit/aadhaar/verifyBio | Create ABHA Number using Biometric Authentication


# **create_health_id_by_demo_auth_using_post**
> HidBenefitRequestPayload create_health_id_by_demo_auth_using_post(create_hid_demo_auth_request, accept_language=accept_language)

Create ABHA Number using Aadhaar Demo Auth.

<b>Explanation</b> - API accepts <b>Aadhaar Demo Auth.</b> and creates ABHA Number using it.    <b>Request Body</b> - Required    <b>Responce</b> - API accepts <b>Aadhaar Demo Auth.</b> and Creates ABHA Number using it. Returns Error for <b>Invalid/Incorrect Aadhaar Demo Auth.</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.create_hid_demo_auth_request import CreateHIdDemoAuthRequest
from abha.models.hid_benefit_request_payload import HidBenefitRequestPayload
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
    api_instance = abha.IntegratedProgramsApi(api_client)
    create_hid_demo_auth_request = abha.CreateHIdDemoAuthRequest() # CreateHIdDemoAuthRequest | createHIdDemoAuthRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Create ABHA Number using Aadhaar Demo Auth.
        api_response = api_instance.create_health_id_by_demo_auth_using_post(create_hid_demo_auth_request, accept_language=accept_language)
        print("The response of IntegratedProgramsApi->create_health_id_by_demo_auth_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedProgramsApi->create_health_id_by_demo_auth_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_hid_demo_auth_request** | [**CreateHIdDemoAuthRequest**](CreateHIdDemoAuthRequest.md)| createHIdDemoAuthRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HidBenefitRequestPayload**](HidBenefitRequestPayload.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Show Benefit Details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Create ABHA number using Aadhaar Demo Auth. or Invalid/Incorrect Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_health_id_by_mobile_using_post**
> HidBenefitRequestPayload create_health_id_by_mobile_using_post(create_hid_mobile_request, accept_language=accept_language)

Create ABHA number using mobile Authentication.

<b>Explanation</b> - Api Accepts <b>mobile Authentication.</b> and Creates HealthID Using it.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>mobile Authentication.</b> and Creates HealthID Using it. Returns Error for <b>Invalid/Incorrect mobile Authentication.</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.create_hid_mobile_request import CreateHidMobileRequest
from abha.models.hid_benefit_request_payload import HidBenefitRequestPayload
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
    api_instance = abha.IntegratedProgramsApi(api_client)
    create_hid_mobile_request = abha.CreateHidMobileRequest() # CreateHidMobileRequest | createHidMobileRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Create ABHA number using mobile Authentication.
        api_response = api_instance.create_health_id_by_mobile_using_post(create_hid_mobile_request, accept_language=accept_language)
        print("The response of IntegratedProgramsApi->create_health_id_by_mobile_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedProgramsApi->create_health_id_by_mobile_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_hid_mobile_request** | [**CreateHidMobileRequest**](CreateHidMobileRequest.md)| createHidMobileRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HidBenefitRequestPayload**](HidBenefitRequestPayload.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Show Benefit Details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Create ABHA number using mobile Authentication. or Invalid/Incorrect Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_phr_adress_with_health_id_number_using_post1**
> str create_phr_adress_with_health_id_number_using_post1(create_phr_adrs_with_health_id_num_req_pay_load, accept_language=accept_language)

Create ABHA Address With ABHA Number

<b>Explanation</b> - API Accepts <b>ABHA Number and Creates ABHA Address</b>.    <b>Request Body</b> - Required    <b>Responce</b> - API accepts <b>ABHA Number and creates ABHA Address</b>. Returns Error for <b>Invalid/Incorrect Info.</b>

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.create_phr_adrs_with_health_id_num_req_pay_load import CreatePhrAdrsWithHealthIdNumReqPayLoad
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
    api_instance = abha.IntegratedProgramsApi(api_client)
    create_phr_adrs_with_health_id_num_req_pay_load = abha.CreatePhrAdrsWithHealthIdNumReqPayLoad() # CreatePhrAdrsWithHealthIdNumReqPayLoad | createPhrAdrsWithHealthIdNumReqPayLoad
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Create ABHA Address With ABHA Number
        api_response = api_instance.create_phr_adress_with_health_id_number_using_post1(create_phr_adrs_with_health_id_num_req_pay_load, accept_language=accept_language)
        print("The response of IntegratedProgramsApi->create_phr_adress_with_health_id_number_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedProgramsApi->create_phr_adress_with_health_id_number_using_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_phr_adrs_with_health_id_num_req_pay_load** | [**CreatePhrAdrsWithHealthIdNumReqPayLoad**](CreatePhrAdrsWithHealthIdNumReqPayLoad.md)| createPhrAdrsWithHealthIdNumReqPayLoad | 
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
**200** | Successfully Created PHR. |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Created PHR. or Invalid/Incorrect Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delink_hid_benefit_using_post**
> HidBenefitLinkedResponsePayload delink_hid_benefit_using_post(hid_benefit_linked_request_payload, accept_language=accept_language)

Delinks benefit programme from ABHA Number

<b>Explanation</b> - API accepts <b>uidToken for Benefit details</b> and De-Links it from ABHA Number    <b>Request Body</b> - Required    <b>Response</b> - API accepts <b>uidToken for Benefit details</b> and De-Links it from ABHA Number. Returns Error for <b>Invalid/Incorrect uidToken</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.hid_benefit_delink_request_payload import HidBenefitDelinkRequestPayload
from abha.models.hid_benefit_linked_response_payload import HidBenefitLinkedResponsePayload
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
    api_instance = abha.IntegratedProgramsApi(api_client)
    hid_benefit_linked_request_payload = abha.HidBenefitDelinkRequestPayload() # HidBenefitDelinkRequestPayload | hidBenefitLinkedRequestPayload
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Delinks benefit programme from ABHA Number
        api_response = api_instance.delink_hid_benefit_using_post(hid_benefit_linked_request_payload, accept_language=accept_language)
        print("The response of IntegratedProgramsApi->delink_hid_benefit_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedProgramsApi->delink_hid_benefit_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hid_benefit_linked_request_payload** | [**HidBenefitDelinkRequestPayload**](HidBenefitDelinkRequestPayload.md)| hidBenefitLinkedRequestPayload | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HidBenefitLinkedResponsePayload**](HidBenefitLinkedResponsePayload.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Show status De-Linked in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not De-link with HID or Invalid/Incorrect Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delink_user_hid_benefit_using_post**
> HidBenefitLinkedResponsePayload delink_user_hid_benefit_using_post(hid_delink_other_programme_request_payload, accept_language=accept_language)

Delinks benefit programme from ABHA Number

<b>Explanation</b> - API accepts <b>ABHA Number and BenefitId</b> and De-Links BenefitId.    <b>Request Body</b> - Required    <b>Response</b> - API Accepts <b>ABHA Number and BenefitId</b> and De-Links BenefitId. Returns Error for <b>Invalid/Incorrect Info.</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.hid_benefit_linked_response_payload import HidBenefitLinkedResponsePayload
from abha.models.hid_delink_other_programme_request_payload import HidDelinkOtherProgrammeRequestPayload
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
    api_instance = abha.IntegratedProgramsApi(api_client)
    hid_delink_other_programme_request_payload = abha.HidDelinkOtherProgrammeRequestPayload() # HidDelinkOtherProgrammeRequestPayload | hidDelinkOtherProgrammeRequestPayload
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Delinks benefit programme from ABHA Number
        api_response = api_instance.delink_user_hid_benefit_using_post(hid_delink_other_programme_request_payload, accept_language=accept_language)
        print("The response of IntegratedProgramsApi->delink_user_hid_benefit_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedProgramsApi->delink_user_hid_benefit_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hid_delink_other_programme_request_payload** | [**HidDelinkOtherProgrammeRequestPayload**](HidDelinkOtherProgrammeRequestPayload.md)| hidDelinkOtherProgrammeRequestPayload | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HidBenefitLinkedResponsePayload**](HidBenefitLinkedResponsePayload.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Show Benefit,Hid Details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not De-Link Hid with programme. or Invalid/Incorrect Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_aadhar_using_post**
> List[str] find_by_aadhar_using_post(aadhar_number_request_payload, accept_language=accept_language)

Search ABHA number using Aadhaar or Aadhaar token

<b>Explanation</b> - Api Accepts <b>Aadhaar or Aadhaar token.</b> and finds ABHA number details using it.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Aadhaar or Aadhaar token.</b> and finds ABHA number details using it. Returns Error for <b>Invalid/Incorrect Aadhaar or Aadhaar token.</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.aadhar_number_request_payload import AadharNumberRequestPayload
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
    api_instance = abha.IntegratedProgramsApi(api_client)
    aadhar_number_request_payload = abha.AadharNumberRequestPayload() # AadharNumberRequestPayload | aadharNumberRequestPayload
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Search ABHA number using Aadhaar or Aadhaar token
        api_response = api_instance.find_by_aadhar_using_post(aadhar_number_request_payload, accept_language=accept_language)
        print("The response of IntegratedProgramsApi->find_by_aadhar_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedProgramsApi->find_by_aadhar_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aadhar_number_request_payload** | [**AadharNumberRequestPayload**](AadharNumberRequestPayload.md)| aadharNumberRequestPayload | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**List[str]**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Show ABHA number Details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not find ABHA number with Aadhar or Invalid/Incorrect Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_health_id_using_post**
> HidBenefitSearchResponsePayload find_by_health_id_using_post(search_request, accept_language=accept_language)

Search benefit using ABHA number

<b>Explanation</b> - API Accepts <b>ABHA Number</b> and finds Benefit details using it.    <b>Request Body</b> - Required    <b>Response</b> - API Accepts <b>ABHA Number</b> and finds Benefit details using it. Returns Error for <b>Invalid/Incorrect healthId</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.hid_benefit_name_search_request import HidBenefitNameSearchRequest
from abha.models.hid_benefit_search_response_payload import HidBenefitSearchResponsePayload
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
    api_instance = abha.IntegratedProgramsApi(api_client)
    search_request = abha.HidBenefitNameSearchRequest() # HidBenefitNameSearchRequest | searchRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Search benefit using ABHA number
        api_response = api_instance.find_by_health_id_using_post(search_request, accept_language=accept_language)
        print("The response of IntegratedProgramsApi->find_by_health_id_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedProgramsApi->find_by_health_id_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**HidBenefitNameSearchRequest**](HidBenefitNameSearchRequest.md)| searchRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HidBenefitSearchResponsePayload**](HidBenefitSearchResponsePayload.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Show Benefit Details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not find Benefit with HID or Invalid/Incorrect Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_aadhar_otp_using_post2**
> CovinTxnResponse generate_aadhar_otp_using_post2(generate_otp_request, accept_language=accept_language)

Generate Aadhaar OTP on Registered mobile number

<b>Explanation</b> - API Accepts <b>Aadhaar</b> and Creates OTP on Registered Mobile Number.    <b>Request Body</b> - Required    <b>Response</b> - API Accepts <b>Aadhaar</b> and Creates OTP on Registered Mobile Number. Returns Error for <b>Invalid/Incorrect Aadhaar</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.aadhar_otp_generate_request_pay_load import AadharOtpGenerateRequestPayLoad
from abha.models.covin_txn_response import CovinTxnResponse
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
    api_instance = abha.IntegratedProgramsApi(api_client)
    generate_otp_request = abha.AadharOtpGenerateRequestPayLoad() # AadharOtpGenerateRequestPayLoad | generateOtpRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate Aadhaar OTP on Registered mobile number
        api_response = api_instance.generate_aadhar_otp_using_post2(generate_otp_request, accept_language=accept_language)
        print("The response of IntegratedProgramsApi->generate_aadhar_otp_using_post2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedProgramsApi->generate_aadhar_otp_using_post2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_otp_request** | [**AadharOtpGenerateRequestPayLoad**](AadharOtpGenerateRequestPayLoad.md)| generateOtpRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**CovinTxnResponse**](CovinTxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Show Transaction ID Details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not generate OTP or Invalid/Incorrect Aadhaar Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_mobile_otp_using_post**
> TxnResponse generate_mobile_otp_using_post(generate_otp_request, accept_language=accept_language)

Generate mobile OTP on Registered mobile number

<b>Explanation</b> - Api Accepts <b>Mobile Number</b> and Creates OTP for it.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Mobile Number</b> and Creates OTP for it. Returns Error for <b>Invalid/Incorrect Mobile Number</b>.

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
    api_instance = abha.IntegratedProgramsApi(api_client)
    generate_otp_request = abha.GenerateMobileOTPRequest() # GenerateMobileOTPRequest | generateOtpRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Generate mobile OTP on Registered mobile number
        api_response = api_instance.generate_mobile_otp_using_post(generate_otp_request, accept_language=accept_language)
        print("The response of IntegratedProgramsApi->generate_mobile_otp_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedProgramsApi->generate_mobile_otp_using_post: %s\n" % e)
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
**200** | Show Transaction ID in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not create OTP or Invalid/Incorrect Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_hid_benefit_using_post**
> HidBenefitLinkedResponsePayload link_hid_benefit_using_post(hid_benefit_linked_request_payload, accept_language=accept_language)

Links benefit programme with ABHA Number

<b>Explanation</b> - API accepts <b>Benefit details</b> and Links it with ABHA Number    <b>Request Body</b> - Required    <b>Response</b> - API accepts <b>Benefit details</b> and Links it with ABHA Number. Returns Error for <b>Invalid Benefit details</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.hid_benefit_linked_request_payload import HidBenefitLinkedRequestPayload
from abha.models.hid_benefit_linked_response_payload import HidBenefitLinkedResponsePayload
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
    api_instance = abha.IntegratedProgramsApi(api_client)
    hid_benefit_linked_request_payload = abha.HidBenefitLinkedRequestPayload() # HidBenefitLinkedRequestPayload | hidBenefitLinkedRequestPayload
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Links benefit programme with ABHA Number
        api_response = api_instance.link_hid_benefit_using_post(hid_benefit_linked_request_payload, accept_language=accept_language)
        print("The response of IntegratedProgramsApi->link_hid_benefit_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedProgramsApi->link_hid_benefit_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hid_benefit_linked_request_payload** | [**HidBenefitLinkedRequestPayload**](HidBenefitLinkedRequestPayload.md)| hidBenefitLinkedRequestPayload | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HidBenefitLinkedResponsePayload**](HidBenefitLinkedResponsePayload.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Show status Linked in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not link with HID or Invalid/Incorrect Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_user_hid_benefit_using_post**
> HidBenefitLinkedResponsePayload link_user_hid_benefit_using_post(hid_linked_other_program_request_payload, accept_language=accept_language)

Link Benefit ID with ABHA Number after authentication.

<b>Explanation</b> - API Accepts <b>Benefit Account Info.</b> and Links it with ABHA Number after Authentication.    <b>Request Body</b> - Required    <b>Response</b> - API Accepts <b>Benefit Account Info.</b> and Links it with ABHA Number after Authentication. Returns Error for <b>Invalid/Incorrect Benefit Account Info.</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.hid_benefit_linked_response_payload import HidBenefitLinkedResponsePayload
from abha.models.hid_linked_other_program_request_payload import HidLinkedOtherProgramRequestPayload
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
    api_instance = abha.IntegratedProgramsApi(api_client)
    hid_linked_other_program_request_payload = abha.HidLinkedOtherProgramRequestPayload() # HidLinkedOtherProgramRequestPayload | hidLinkedOtherProgramRequestPayload
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Link Benefit ID with ABHA Number after authentication.
        api_response = api_instance.link_user_hid_benefit_using_post(hid_linked_other_program_request_payload, accept_language=accept_language)
        print("The response of IntegratedProgramsApi->link_user_hid_benefit_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedProgramsApi->link_user_hid_benefit_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hid_linked_other_program_request_payload** | [**HidLinkedOtherProgramRequestPayload**](HidLinkedOtherProgramRequestPayload.md)| hidLinkedOtherProgramRequestPayload | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HidBenefitLinkedResponsePayload**](HidBenefitLinkedResponsePayload.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Show Benefit Details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Link Benefit ID with ABHA number. or Invalid/Incorrect Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_benefit_using_post**
> HidBenefitRequestPayload notify_benefit_using_post(create_hid_notify_benefit_request, accept_language=accept_language)

Create ABHA number using notify Benefit.

<b>Explanation</b> - Create abha number, link benefit id and notify the user via sms.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.create_hid_notify_benefit_request import CreateHidNotifyBenefitRequest
from abha.models.hid_benefit_request_payload import HidBenefitRequestPayload
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
    api_instance = abha.IntegratedProgramsApi(api_client)
    create_hid_notify_benefit_request = abha.CreateHidNotifyBenefitRequest() # CreateHidNotifyBenefitRequest | createHidNotifyBenefitRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Create ABHA number using notify Benefit.
        api_response = api_instance.notify_benefit_using_post(create_hid_notify_benefit_request, accept_language=accept_language)
        print("The response of IntegratedProgramsApi->notify_benefit_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedProgramsApi->notify_benefit_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_hid_notify_benefit_request** | [**CreateHidNotifyBenefitRequest**](CreateHidNotifyBenefitRequest.md)| createHidNotifyBenefitRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HidBenefitRequestPayload**](HidBenefitRequestPayload.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Show Benefit Details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Create ABHA number using notify Benefit. or Invalid/Incorrect Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_information_using_post1**
> UserDTO update_account_information_using_post1(request, accept_language=accept_language)

Update account information

<b>Explanation</b> - API Accepts <b>Account Details</b> and Updates it.    <b>Request Body</b> - Required    <b>Response</b> - API Accepts <b>Account Details</b> and Updates it. Returns Error for <b>Invalid/Incorrect Account Details</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.hid_update_account_request import HidUpdateAccountRequest
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
    api_instance = abha.IntegratedProgramsApi(api_client)
    request = abha.HidUpdateAccountRequest() # HidUpdateAccountRequest | request
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Update account information
        api_response = api_instance.update_account_information_using_post1(request, accept_language=accept_language)
        print("The response of IntegratedProgramsApi->update_account_information_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedProgramsApi->update_account_information_using_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**HidUpdateAccountRequest**](HidUpdateAccountRequest.md)| request | 
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
**200** | Show User Details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Update Account Info. or Invalid/Incorrect Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mobile_information_using_post**
> UserDTO update_mobile_information_using_post(request, accept_language=accept_language)

Update mobile number for account.

<b>Explanation</b> - API Accepts <b>Mobile Number</b> and Updates it for Particular Account.    <b>Request Body</b> - Required    <b>Responce</b> - API Accepts <b>Mobile Number</b> and Updates it for Particular Account. Returns Error for <b>Invalid/Incorrect Mobile Number</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.hid_update_mobilet_request import HidUpdateMobiletRequest
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
    api_instance = abha.IntegratedProgramsApi(api_client)
    request = abha.HidUpdateMobiletRequest() # HidUpdateMobiletRequest | request
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Update mobile number for account.
        api_response = api_instance.update_mobile_information_using_post(request, accept_language=accept_language)
        print("The response of IntegratedProgramsApi->update_mobile_information_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedProgramsApi->update_mobile_information_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**HidUpdateMobiletRequest**](HidUpdateMobiletRequest.md)| request | 
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
**200** | Show User Details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Update mobile number for account. or Invalid/Incorrect Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_status_using_post**
> bool update_status_using_post(generate_otp_request, accept_language=accept_language)

Update ABHA status

<b>Explanation</b> - API accepts <b>ABHA Number</b> and Updates Status.    <b>Request Body</b> - Required    <b>Response</b> - API Accepts <b>ABHA Number</b> and Updates Status. Returns Error for <b>Invalid/Incorrect ABHA number Number</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.hid_status_request_payload import HidStatusRequestPayload
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
    api_instance = abha.IntegratedProgramsApi(api_client)
    generate_otp_request = abha.HidStatusRequestPayload() # HidStatusRequestPayload | generateOtpRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Update ABHA status
        api_response = api_instance.update_status_using_post(generate_otp_request, accept_language=accept_language)
        print("The response of IntegratedProgramsApi->update_status_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedProgramsApi->update_status_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_otp_request** | [**HidStatusRequestPayload**](HidStatusRequestPayload.md)| generateOtpRequest | 
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
**200** | Show Boolean true in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Update ABHA number status. or Invalid/Incorrect Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_aadhar_otp_using_post**
> HidBenefitRequestPayload verify_aadhar_otp_using_post(create_health_id_opt_request, accept_language=accept_language)

Create ABHA Number using Aadhaar Number OTP

<b>Explanation</b> - API accepts <b>Aadhaar Number OTP. Details</b> and creates ABHA Number using it.    <b>Request Body</b> - Required    <b>Response</b> - API Accepts <b>Aadhaar Number OTP and other details</b> and creates ABHA Number using it. Returns Error for <b>Invalid/Incorrect Aadhaar Number OTP</b>

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.create_health_id_opt_request import CreateHealthIdOptRequest
from abha.models.hid_benefit_request_payload import HidBenefitRequestPayload
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
    api_instance = abha.IntegratedProgramsApi(api_client)
    create_health_id_opt_request = abha.CreateHealthIdOptRequest() # CreateHealthIdOptRequest | createHealthIdOptRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Create ABHA Number using Aadhaar Number OTP
        api_response = api_instance.verify_aadhar_otp_using_post(create_health_id_opt_request, accept_language=accept_language)
        print("The response of IntegratedProgramsApi->verify_aadhar_otp_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedProgramsApi->verify_aadhar_otp_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_health_id_opt_request** | [**CreateHealthIdOptRequest**](CreateHealthIdOptRequest.md)| createHealthIdOptRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HidBenefitRequestPayload**](HidBenefitRequestPayload.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Show Benefit Details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Create ABHA number using Aadhaar Number Otp. or Invalid/Incorrect Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_bio_using_post**
> HidBenefitRequestPayload verify_bio_using_post(create_hid_biometric_request, accept_language=accept_language)

Create ABHA Number using Biometric Authentication

<b>Explanation</b> - API Accepts <b>Biometric Authentication Details</b> and creates ABHA Number using it.    <b>Request Body</b> - Required    <b>Responce</b> - API accepts <b>Biometric Authentication Details</b> and creates ABHA Number using it. Returns Error for <b>Invalid/Incorrect Biometric Authentication Details</b>.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (X-HIP-ID):

```python
import abha
from abha.models.create_hid_biometric_request import CreateHidBiometricRequest
from abha.models.hid_benefit_request_payload import HidBenefitRequestPayload
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
    api_instance = abha.IntegratedProgramsApi(api_client)
    create_hid_biometric_request = abha.CreateHidBiometricRequest() # CreateHidBiometricRequest | createHidBiometricRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Create ABHA Number using Biometric Authentication
        api_response = api_instance.verify_bio_using_post(create_hid_biometric_request, accept_language=accept_language)
        print("The response of IntegratedProgramsApi->verify_bio_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedProgramsApi->verify_bio_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_hid_biometric_request** | [**CreateHidBiometricRequest**](CreateHidBiometricRequest.md)| createHidBiometricRequest | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HidBenefitRequestPayload**](HidBenefitRequestPayload.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Show Benefit Details in case of success |  -  |
**201** | Created |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not Create ABHA number using Biometric Authentication. or Invalid/Incorrect Details |  -  |
**500** | Downstream system(s) is down. Unhandled exceptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

