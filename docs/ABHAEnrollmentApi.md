# abha.ABHAEnrollmentApi

All URIs are relative to *https://abhasbx.abdm.gov.in/abha/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_enrollment_auth_by_aadhaar_post**](ABHAEnrollmentApi.md#api_v3_enrollment_auth_by_aadhaar_post) | **POST** /api/v3/enrollment/auth/byAadhaar | AUTH - OF AADHAAR OTP FOR PARENT VERIFICATION
[**api_v3_enrollment_auth_by_abdm_post**](ABHAEnrollmentApi.md#api_v3_enrollment_auth_by_abdm_post) | **POST** /api/v3/enrollment/auth/byAbdm | VERIFY - EMAIL, MOBILE UPDATE
[**api_v3_enrollment_enrol_by_aadhaar_post**](ABHAEnrollmentApi.md#api_v3_enrollment_enrol_by_aadhaar_post) | **POST** /api/v3/enrollment/enrol/byAadhaar | ENROL - BY AADHAAR VERIFICATION
[**api_v3_enrollment_enrol_by_document_post**](ABHAEnrollmentApi.md#api_v3_enrollment_enrol_by_document_post) | **POST** /api/v3/enrollment/enrol/byDocument | ENROL - BY DOCUMENT
[**api_v3_enrollment_enrol_suggestion_get**](ABHAEnrollmentApi.md#api_v3_enrollment_enrol_suggestion_get) | **GET** /api/v3/enrollment/enrol/suggestion | SUGESSTION
[**api_v3_enrollment_request_otp_post**](ABHAEnrollmentApi.md#api_v3_enrollment_request_otp_post) | **POST** /api/v3/enrollment/request/otp | REQUEST - OTP FOR ENROLLMENT, UPDATE MOBILE and UPDATE EMAIL


# **api_v3_enrollment_auth_by_aadhaar_post**
> object api_v3_enrollment_auth_by_aadhaar_post(request_id, timestamp, body=body)

AUTH - OF AADHAAR OTP FOR PARENT VERIFICATION

### Example


```python
import abha
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://abhasbx.abdm.gov.in/abha/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "https://abhasbx.abdm.gov.in/abha/api/v3"
)


# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.ABHAEnrollmentApi(api_client)
    request_id = 'request_id_example' # str | 
    timestamp = 'timestamp_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # AUTH - OF AADHAAR OTP FOR PARENT VERIFICATION
        api_response = api_instance.api_v3_enrollment_auth_by_aadhaar_post(request_id, timestamp, body=body)
        print("The response of ABHAEnrollmentApi->api_v3_enrollment_auth_by_aadhaar_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ABHAEnrollmentApi->api_v3_enrollment_auth_by_aadhaar_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  | 
 **timestamp** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_enrollment_auth_by_abdm_post**
> object api_v3_enrollment_auth_by_abdm_post(request_id, timestamp, body=body)

VERIFY - EMAIL, MOBILE UPDATE

### Example


```python
import abha
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://abhasbx.abdm.gov.in/abha/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "https://abhasbx.abdm.gov.in/abha/api/v3"
)


# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.ABHAEnrollmentApi(api_client)
    request_id = 'request_id_example' # str | 
    timestamp = 'timestamp_example' # str | 
    body = {"scope":["abha-enrol","email-verify"],"authData":{"authMethods":["otp"],"otp":{"timeStamp":"{{current_timestamp}}","txnId":"b7ffebe2-8be8-433a-b447-62eecc45e397","otpValue":"<RSA Encrypted OTP Value>"}}} # object |  (optional)

    try:
        # VERIFY - EMAIL, MOBILE UPDATE
        api_response = api_instance.api_v3_enrollment_auth_by_abdm_post(request_id, timestamp, body=body)
        print("The response of ABHAEnrollmentApi->api_v3_enrollment_auth_by_abdm_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ABHAEnrollmentApi->api_v3_enrollment_auth_by_abdm_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  | 
 **timestamp** | **str**|  | 
 **body** | **object**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_enrollment_enrol_by_aadhaar_post**
> object api_v3_enrollment_enrol_by_aadhaar_post(request_id, timestamp, body=body)

ENROL - BY AADHAAR VERIFICATION

### Example


```python
import abha
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://abhasbx.abdm.gov.in/abha/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "https://abhasbx.abdm.gov.in/abha/api/v3"
)


# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.ABHAEnrollmentApi(api_client)
    request_id = 'request_id_example' # str | 
    timestamp = 'timestamp_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # ENROL - BY AADHAAR VERIFICATION
        api_response = api_instance.api_v3_enrollment_enrol_by_aadhaar_post(request_id, timestamp, body=body)
        print("The response of ABHAEnrollmentApi->api_v3_enrollment_enrol_by_aadhaar_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ABHAEnrollmentApi->api_v3_enrollment_enrol_by_aadhaar_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  | 
 **timestamp** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_enrollment_enrol_by_document_post**
> api_v3_enrollment_enrol_by_document_post(request_id, timestamp, body=body)

ENROL - BY DOCUMENT

### Example


```python
import abha
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://abhasbx.abdm.gov.in/abha/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "https://abhasbx.abdm.gov.in/abha/api/v3"
)


# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.ABHAEnrollmentApi(api_client)
    request_id = 'request_id_example' # str | 
    timestamp = 'timestamp_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # ENROL - BY DOCUMENT
        api_instance.api_v3_enrollment_enrol_by_document_post(request_id, timestamp, body=body)
    except Exception as e:
        print("Exception when calling ABHAEnrollmentApi->api_v3_enrollment_enrol_by_document_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  | 
 **timestamp** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_enrollment_enrol_suggestion_get**
> api_v3_enrollment_enrol_suggestion_get(request_id, timestamp, transaction_id=transaction_id)

SUGESSTION

### Example


```python
import abha
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://abhasbx.abdm.gov.in/abha/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "https://abhasbx.abdm.gov.in/abha/api/v3"
)


# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.ABHAEnrollmentApi(api_client)
    request_id = 'request_id_example' # str | 
    timestamp = 'timestamp_example' # str | 
    transaction_id = 'f7357347-440a-4c2d-b862-71cc787c763e' # str |  (optional)

    try:
        # SUGESSTION
        api_instance.api_v3_enrollment_enrol_suggestion_get(request_id, timestamp, transaction_id=transaction_id)
    except Exception as e:
        print("Exception when calling ABHAEnrollmentApi->api_v3_enrollment_enrol_suggestion_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  | 
 **timestamp** | **str**|  | 
 **transaction_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_enrollment_request_otp_post**
> object api_v3_enrollment_request_otp_post(request_id, timestamp, body=body)

REQUEST - OTP FOR ENROLLMENT, UPDATE MOBILE and UPDATE EMAIL

### Example


```python
import abha
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://abhasbx.abdm.gov.in/abha/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "https://abhasbx.abdm.gov.in/abha/api/v3"
)


# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.ABHAEnrollmentApi(api_client)
    request_id = 'request_id_example' # str | 
    timestamp = 'timestamp_example' # str | 
    body = {"txnId":"b7ffebe2-8be8-433a-b447-62eecc45e397","scope":["abha-enrol"],"loginHint":"aadhaar","loginId":"<RSA Encripted aadhaar number>","otpSystem":"aadhaar"} # object |  (optional)

    try:
        # REQUEST - OTP FOR ENROLLMENT, UPDATE MOBILE and UPDATE EMAIL
        api_response = api_instance.api_v3_enrollment_request_otp_post(request_id, timestamp, body=body)
        print("The response of ABHAEnrollmentApi->api_v3_enrollment_request_otp_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ABHAEnrollmentApi->api_v3_enrollment_request_otp_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  | 
 **timestamp** | **str**|  | 
 **body** | **object**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

