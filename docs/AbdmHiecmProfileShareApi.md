# abha.AbdmHiecmProfileShareApi

All URIs are relative to *https://healthidsbx.abdm.gov.in/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abdm_profile_share_1**](AbdmHiecmProfileShareApi.md#abdm_profile_share_1) | **POST** /v3/patient/profile/share | This API will be invoked from the integrator application for sharing the patient/user profile with the HMIS/LIMS.
[**profile_share_2**](AbdmHiecmProfileShareApi.md#profile_share_2) | **POST** /v3/patient/profile/on-share | This API will be invoked by the HIP for sharing the response of HIECM&#39;s /api/v3/hiecm/profile/share API


# **abdm_profile_share_1**
> AbdmProfileShare1200Response abdm_profile_share_1(abdm_profile_share1_request)

This API will be invoked from the integrator application for sharing the patient/user profile with the HMIS/LIMS.

This is a API will be invoked from the <b>integrator application</b> to share the user/patient profile with HMIS/LIMS. <ol type='1'> <li> <b>Header</b>  <ol type='a'> <br/> <li>Authorization will be provided by the gateway session API after the successful verification of client ID and Secret [ Example: eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJ2YXNhbnRoYWt1bWFyLmtlc2F2 ]</li> <li>REQUEST_ID unique UUID[ Example: 18235d89-cb13-479d-ad71-7a57d5f669a8 ]</li> <li>TIMESTAMP  actual time of the requested was initiated[ Example: 2022-10-06T10:10:00.587 ]</li> <li>X_AUTH_TOKEN JWT Authentication token which was issued by ABDM after successful validation of username and password[ Example: eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJ2YXNhbnRoYWt1bWFyLmtlc2F2 ]</li> <li>X_CM_ID  consent manager ID[ Example: ABDM_SBX ]</li> </ol> </li> <br/> <li> <b>Request Body</b> <ol type='a'><br/> <li>intent This is a key value pair  which contains the purpose [ Example: { hip_id: ABDM_HIP, context: 123, purpose: profile_share } ]</li> <li>metaData This is a key value pair which contains the location longitude and latitude[ Example: { lat: 20.5937 long: 78.9629} ]</li> </ol> </ol>

### Example


```python
import abha
from abha.models.abdm_profile_share1200_response import AbdmProfileShare1200Response
from abha.models.abdm_profile_share1_request import AbdmProfileShare1Request
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
    api_instance = abha.AbdmHiecmProfileShareApi(api_client)
    abdm_profile_share1_request = abha.AbdmProfileShare1Request() # AbdmProfileShare1Request | 

    try:
        # This API will be invoked from the integrator application for sharing the patient/user profile with the HMIS/LIMS.
        api_response = api_instance.abdm_profile_share_1(abdm_profile_share1_request)
        print("The response of AbdmHiecmProfileShareApi->abdm_profile_share_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AbdmHiecmProfileShareApi->abdm_profile_share_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **abdm_profile_share1_request** | [**AbdmProfileShare1Request**](AbdmProfileShare1Request.md)|  | 

### Return type

[**AbdmProfileShare1200Response**](AbdmProfileShare1200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_share_2**
> profile_share_2(profile_share2_request)

This API will be invoked by the HIP for sharing the response of HIECM's /api/v3/hiecm/profile/share API

This is a API will be invoked by the <b>HIP</b> to share the response of HIECM's /api/v3/hiecm/profile/share API. <ol type='1'> <li> <b>Header</b>  <ol type='a'> <br/> <li>AUTHORIZATION will be provided by the gateway session API after the successful verification of client ID and Secret [ Example: eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJ2YXNhbnRoYWt1bWFyLmtlc2F2 ]</li> <li>REQUEST_ID unique UUID[ Example: 18235d89-cb13-479d-ad71-7a57d5f669a8 ]</li> <li>TIMESTAMP  actual time of the requested was initiated[ Example: 2022-10-06T10:10:00.587 ]</li> <li>X_CM_ID  consent manager ID[ Example: ABDM_SBX ]</li> </ol> </li> <br/> <li> <b>Request Body</b> <ol type='a'><br/> <li>acknowledgement is mandatory object in case of successful response</li> <li>error is optional object in case of successful response</li> <li>response is mandatory object in both the cases</li> </ol> </ol>

### Example


```python
import abha
from abha.models.profile_share2_request import ProfileShare2Request
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
    api_instance = abha.AbdmHiecmProfileShareApi(api_client)
    profile_share2_request = abha.ProfileShare2Request() # ProfileShare2Request | 

    try:
        # This API will be invoked by the HIP for sharing the response of HIECM's /api/v3/hiecm/profile/share API
        api_instance.profile_share_2(profile_share2_request)
    except Exception as e:
        print("Exception when calling AbdmHiecmProfileShareApi->profile_share_2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_share2_request** | [**ProfileShare2Request**](ProfileShare2Request.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**408** | Request Timeout |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

