# abha.AbdmHipProfileShareApi

All URIs are relative to *https://healthidsbx.abdm.gov.in/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profile_share_3**](AbdmHipProfileShareApi.md#profile_share_3) | **POST** /[callback_url]/v3/hip/patient/profile/share | This API will be invoked by the HIP for sharing the response of HIECM&#39;s /api/v3/hiecm/profile/share API


# **profile_share_3**
> profile_share_3(profile_share3_request)

This API will be invoked by the HIP for sharing the response of HIECM's /api/v3/hiecm/profile/share API

This is a API will be invoked by the <b>HIP</b> to share the response of HIECM's /api/v3/hiecm/profile/share API. <ol type='1'> <li> <b>Header</b>  <ol type='a'> <br/> <li>REQUEST_ID unique UUID[ Example: 18235d89-cb13-479d-ad71-7a57d5f669a8 ]</li> <li>TIMESTAMP  actual time of the requested was initiated[ Example: 2022-10-06T10:10:00.587 ]</li> <li>X_HIP_ID  consent manager ID[ Example: ABDM_SBX ]</li> </ol> </li> <br/> <li> <b>Request Body</b> <ol type='a'><br/> <li>acknowledgement is mandatory object in case of successful response</li> <li>error is optional object in case of successful response</li> <li>response is mandatory object in both the cases</li> </ol> </ol>

### Example


```python
import abha
from abha.models.profile_share3_request import ProfileShare3Request
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
    api_instance = abha.AbdmHipProfileShareApi(api_client)
    profile_share3_request = abha.ProfileShare3Request() # ProfileShare3Request | 

    try:
        # This API will be invoked by the HIP for sharing the response of HIECM's /api/v3/hiecm/profile/share API
        api_instance.profile_share_3(profile_share3_request)
    except Exception as e:
        print("Exception when calling AbdmHipProfileShareApi->profile_share_3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_share3_request** | [**ProfileShare3Request**](ProfileShare3Request.md)|  | 

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

