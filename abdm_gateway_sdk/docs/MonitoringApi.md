# abdm_gateway.MonitoringApi

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_heartbeat_get**](MonitoringApi.md#v05_heartbeat_get) | **GET** /v0.5/heartbeat | Informs about server status


# **v05_heartbeat_get**
> HeartbeatResponse v05_heartbeat_get()

Informs about server status

### Example


```python
import abdm_gateway
from abdm_gateway.models.heartbeat_response import HeartbeatResponse
from abdm_gateway.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dev.abdm.gov.in/gateway
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm_gateway.Configuration(
    host = "https://dev.abdm.gov.in/gateway"
)


# Enter a context with an instance of the API client
with abdm_gateway.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm_gateway.MonitoringApi(api_client)

    try:
        # Informs about server status
        api_response = api_instance.v05_heartbeat_get()
        print("The response of MonitoringApi->v05_heartbeat_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitoringApi->v05_heartbeat_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HeartbeatResponse**](HeartbeatResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

