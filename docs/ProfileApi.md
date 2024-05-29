# abha.ProfileApi

All URIs are relative to *https://healthidsbx.abdm.gov.in/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v10_patients_profile_share_post**](ProfileApi.md#v10_patients_profile_share_post) | **POST** /v1.0/patients/profile/share | Share patient profile details


# **v10_patients_profile_share_post**
> v10_patients_profile_share_post(v10_patients_profile_share_post_request)

Share patient profile details

Request for sharing patient's profile details to HIP 

### Example


```python
import abha
from abha.models.v10_patients_profile_share_post_request import V10PatientsProfileSharePostRequest
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
    api_instance = abha.ProfileApi(api_client)
    v10_patients_profile_share_post_request = abha.V10PatientsProfileSharePostRequest() # V10PatientsProfileSharePostRequest | 

    try:
        # Share patient profile details
        api_instance.v10_patients_profile_share_post(v10_patients_profile_share_post_request)
    except Exception as e:
        print("Exception when calling ProfileApi->v10_patients_profile_share_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v10_patients_profile_share_post_request** | [**V10PatientsProfileSharePostRequest**](V10PatientsProfileSharePostRequest.md)|  | 

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
**202** | Request accepted |  -  |
**400** | **Causes:**   * Invalid Request  |  -  |
**401** | **Causes:**   * Unauthorized request  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

