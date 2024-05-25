# abha.DefaultApi

All URIs are relative to *https://healthidsbx.abdm.gov.in/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_health_id_with_pre_verified**](DefaultApi.md#create_health_id_with_pre_verified) | **POST** /registration/aadhaar/createHealthIdWithPreVerified | Health ID creation
[**generate_card_using_get**](DefaultApi.md#generate_card_using_get) | **GET** /account/getCard | Generate ABHA card in PDF format
[**generate_mobile_otp**](DefaultApi.md#generate_mobile_otp) | **POST** /registration/aadhaar/generateMobileOTP | Generate Mobile OTP
[**generate_otp**](DefaultApi.md#generate_otp) | **POST** /registration/aadhaar/generateOtp | Generate OTP
[**generate_png_card_using_get**](DefaultApi.md#generate_png_card_using_get) | **GET** /account/getPngCard | Generate ABHA card PNG
[**generate_svg_card_using_get**](DefaultApi.md#generate_svg_card_using_get) | **GET** /account/getSvgCard | Generate ABHA card SVG
[**get_qr_code_using_get**](DefaultApi.md#get_qr_code_using_get) | **GET** /account/qrCode | Get Quick Response code in PNG format for this account.
[**verify_mobile_otp**](DefaultApi.md#verify_mobile_otp) | **POST** /registration/aadhaar/verifyMobileOTP | Verify Mobile OTP
[**verify_otp**](DefaultApi.md#verify_otp) | **POST** /registration/aadhaar/verifyOTP | Verify OTP


# **create_health_id_with_pre_verified**
> CreateHealthIdWithPreVerified200Response create_health_id_with_pre_verified(create_health_id_with_pre_verified_request)

Health ID creation

This endpoint Creates Health Id .

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import abha
from abha.models.create_health_id_with_pre_verified200_response import CreateHealthIdWithPreVerified200Response
from abha.models.create_health_id_with_pre_verified_request import CreateHealthIdWithPreVerifiedRequest
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://healthidsbx.abdm.gov.in/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "https://healthidsbx.abdm.gov.in/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = abha.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.DefaultApi(api_client)
    create_health_id_with_pre_verified_request = abha.CreateHealthIdWithPreVerifiedRequest() # CreateHealthIdWithPreVerifiedRequest | 

    try:
        # Health ID creation
        api_response = api_instance.create_health_id_with_pre_verified(create_health_id_with_pre_verified_request)
        print("The response of DefaultApi->create_health_id_with_pre_verified:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_health_id_with_pre_verified: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_health_id_with_pre_verified_request** | [**CreateHealthIdWithPreVerifiedRequest**](CreateHealthIdWithPreVerifiedRequest.md)|  | 

### Return type

[**CreateHealthIdWithPreVerified200Response**](CreateHealthIdWithPreVerified200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Health Id Created successfully |  -  |
**400** | Bad request (e.g., missing or invalid Aadhaar number) |  -  |
**401** | Unauthorized (invalid or missing bearer token) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_card_using_get**
> generate_card_using_get()

Generate ABHA card in PDF format

<b>Explanation</b> - Api Accepts <b>Auth Token</b> and then Returns Account Details for PDF format.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Auth Token</b> and then Returns Account Details for PDF format. Returns Error for <b>Unauthorized Auth Token</b>.

### Example


```python
import abha
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://healthidsbx.abdm.gov.in/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "https://healthidsbx.abdm.gov.in/api/v1"
)


# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.DefaultApi(api_client)

    try:
        # Generate ABHA card in PDF format
        api_instance.generate_card_using_get()
    except Exception as e:
        print("Exception when calling DefaultApi->generate_card_using_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

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

# **generate_mobile_otp**
> GenerateOtp200Response generate_mobile_otp(generate_mobile_otp_request)

Generate Mobile OTP

This endpoint Generates OTP for Abha verification.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import abha
from abha.models.generate_mobile_otp_request import GenerateMobileOtpRequest
from abha.models.generate_otp200_response import GenerateOtp200Response
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://healthidsbx.abdm.gov.in/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "https://healthidsbx.abdm.gov.in/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = abha.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.DefaultApi(api_client)
    generate_mobile_otp_request = abha.GenerateMobileOtpRequest() # GenerateMobileOtpRequest | 

    try:
        # Generate Mobile OTP
        api_response = api_instance.generate_mobile_otp(generate_mobile_otp_request)
        print("The response of DefaultApi->generate_mobile_otp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->generate_mobile_otp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_mobile_otp_request** | [**GenerateMobileOtpRequest**](GenerateMobileOtpRequest.md)|  | 

### Return type

[**GenerateOtp200Response**](GenerateOtp200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OTP Generated successfully |  -  |
**400** | Bad request (e.g., missing or invalid Aadhaar number) |  -  |
**401** | Unauthorized (invalid or missing bearer token) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_otp**
> GenerateOtp200Response generate_otp(generate_otp_request)

Generate OTP

This endpoint generates an OTP for Aadhaar number verification.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import abha
from abha.models.generate_otp200_response import GenerateOtp200Response
from abha.models.generate_otp_request import GenerateOtpRequest
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://healthidsbx.abdm.gov.in/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "https://healthidsbx.abdm.gov.in/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = abha.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.DefaultApi(api_client)
    generate_otp_request = abha.GenerateOtpRequest() # GenerateOtpRequest | 

    try:
        # Generate OTP
        api_response = api_instance.generate_otp(generate_otp_request)
        print("The response of DefaultApi->generate_otp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->generate_otp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_otp_request** | [**GenerateOtpRequest**](GenerateOtpRequest.md)|  | 

### Return type

[**GenerateOtp200Response**](GenerateOtp200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OTP generated successfully |  -  |
**400** | Bad request (e.g., missing or invalid Aadhaar number) |  -  |
**401** | Unauthorized (invalid or missing bearer token) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_png_card_using_get**
> generate_png_card_using_get()

Generate ABHA card PNG

<b>Explanation</b> - Api Accepts <b>Auth Token</b> and then Returns Account Details for PNG format.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Auth Token</b> and then Returns Account Details for PNG format. Returns Error for <b>Unauthorized Auth Token</b>.

### Example


```python
import abha
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://healthidsbx.abdm.gov.in/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "https://healthidsbx.abdm.gov.in/api/v1"
)


# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.DefaultApi(api_client)

    try:
        # Generate ABHA card PNG
        api_instance.generate_png_card_using_get()
    except Exception as e:
        print("Exception when calling DefaultApi->generate_png_card_using_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

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
> generate_svg_card_using_get()

Generate ABHA card SVG

<b>Explanation</b> - Api Accepts <b>Auth Token</b> and then Returns Account Details for SVG format.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Auth Token</b> and then Returns Account Details for SVG format. Returns Error for <b>Unauthorized Auth Token</b>.

### Example


```python
import abha
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://healthidsbx.abdm.gov.in/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "https://healthidsbx.abdm.gov.in/api/v1"
)


# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.DefaultApi(api_client)

    try:
        # Generate ABHA card SVG
        api_instance.generate_svg_card_using_get()
    except Exception as e:
        print("Exception when calling DefaultApi->generate_svg_card_using_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

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

# **get_qr_code_using_get**
> get_qr_code_using_get()

Get Quick Response code in PNG format for this account.

<b>Explanation</b> - Api Accepts <b>Auth Token</b> and then returns Account Info for QR Code.    <b>Request Body</b> - Required    <b>Responce</b> - Api Accepts <b>Auth Token</b> and then returns Account Info for QR Code. Returns Error for <b>Unauthorized Token</b>.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import abha
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://healthidsbx.abdm.gov.in/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "https://healthidsbx.abdm.gov.in/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = abha.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.DefaultApi(api_client)

    try:
        # Get Quick Response code in PNG format for this account.
        api_instance.get_qr_code_using_get()
    except Exception as e:
        print("Exception when calling DefaultApi->get_qr_code_using_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return QR Code in Byte Array Form in case of success |  -  |
**400** | Bad request, check request before retrying |  -  |
**401** | Unauthorized Access. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_mobile_otp**
> GenerateOtp200Response verify_mobile_otp(verify_otp_request)

Verify Mobile OTP

This endpoint Verfies OTP for Abha verification.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import abha
from abha.models.generate_otp200_response import GenerateOtp200Response
from abha.models.verify_otp_request import VerifyOtpRequest
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://healthidsbx.abdm.gov.in/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "https://healthidsbx.abdm.gov.in/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = abha.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.DefaultApi(api_client)
    verify_otp_request = abha.VerifyOtpRequest() # VerifyOtpRequest | 

    try:
        # Verify Mobile OTP
        api_response = api_instance.verify_mobile_otp(verify_otp_request)
        print("The response of DefaultApi->verify_mobile_otp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->verify_mobile_otp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_otp_request** | [**VerifyOtpRequest**](VerifyOtpRequest.md)|  | 

### Return type

[**GenerateOtp200Response**](GenerateOtp200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OTP Verified successfully |  -  |
**400** | Bad request (e.g., missing or invalid Aadhaar number) |  -  |
**401** | Unauthorized (invalid or missing bearer token) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_otp**
> GenerateOtp200Response verify_otp(verify_otp_request)

Verify OTP

This endpoint Verfies OTP for Aadhaar number verification.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import abha
from abha.models.generate_otp200_response import GenerateOtp200Response
from abha.models.verify_otp_request import VerifyOtpRequest
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://healthidsbx.abdm.gov.in/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "https://healthidsbx.abdm.gov.in/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = abha.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.DefaultApi(api_client)
    verify_otp_request = abha.VerifyOtpRequest() # VerifyOtpRequest | 

    try:
        # Verify OTP
        api_response = api_instance.verify_otp(verify_otp_request)
        print("The response of DefaultApi->verify_otp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->verify_otp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_otp_request** | [**VerifyOtpRequest**](VerifyOtpRequest.md)|  | 

### Return type

[**GenerateOtp200Response**](GenerateOtp200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OTP Validated successfully |  -  |
**400** | Bad request (e.g., missing or invalid Aadhaar number) |  -  |
**401** | Unauthorized (invalid or missing bearer token) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

