# abdm_gateway.SubscriptionsApi

All URIs are relative to *https://dev.abdm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05_subscription_requests_cm_init_post**](SubscriptionsApi.md#v05_subscription_requests_cm_init_post) | **POST** /v0.5/subscription-requests/cm/init | Request for subscription
[**v05_subscription_requests_cm_on_init_post**](SubscriptionsApi.md#v05_subscription_requests_cm_on_init_post) | **POST** /v0.5/subscription-requests/cm/on-init | callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.
[**v05_subscription_requests_hiu_notify_post**](SubscriptionsApi.md#v05_subscription_requests_hiu_notify_post) | **POST** /v0.5/subscription-requests/hiu/notify | Notification for subscription grant/deny/revoke
[**v05_subscription_requests_hiu_on_notify_post**](SubscriptionsApi.md#v05_subscription_requests_hiu_on_notify_post) | **POST** /v0.5/subscription-requests/hiu/on-notify | Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.
[**v05_subscriptions_hiu_notify_post**](SubscriptionsApi.md#v05_subscriptions_hiu_notify_post) | **POST** /v0.5/subscriptions/hiu/notify | Notification to HIU on basis of a granted subscription
[**v05_subscriptions_hiu_on_notify_post**](SubscriptionsApi.md#v05_subscriptions_hiu_on_notify_post) | **POST** /v0.5/subscriptions/hiu/on-notify | Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.


# **v05_subscription_requests_cm_init_post**
> v05_subscription_requests_cm_init_post(authorization, x_cm_id, subscription_request)

Request for subscription

creates a request for subscription. The subscription categories can be for care-contexts linkages or availability of data against existing care-contexts. Note that the requester must have HIU role

### Example


```python
import abdm_gateway
from abdm_gateway.models.subscription_request import SubscriptionRequest
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
    api_instance = abdm_gateway.SubscriptionsApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    subscription_request = abdm_gateway.SubscriptionRequest() # SubscriptionRequest | 

    try:
        # Request for subscription
        api_instance.v05_subscription_requests_cm_init_post(authorization, x_cm_id, subscription_request)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->v05_subscription_requests_cm_init_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **subscription_request** | [**SubscriptionRequest**](SubscriptionRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted |  -  |
**400** | **Causes:**   * Invalid data sent    * Required attributes not mentioned  |  -  |
**401** | **Causes:**   * Expired/Invalid token.  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_subscription_requests_cm_on_init_post**
> v05_subscription_requests_cm_on_init_post(authorization, x_hiu_id, hiu_subscription_request_receipt)

callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.

This callback API acknowledges the request for subscription from a HIU, and sends back a \"id\" that will be used when the patient/user approves or denies the subscription. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hiu_subscription_request_receipt import HIUSubscriptionRequestReceipt
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
    api_instance = abdm_gateway.SubscriptionsApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    hiu_subscription_request_receipt = abdm_gateway.HIUSubscriptionRequestReceipt() # HIUSubscriptionRequestReceipt | 

    try:
        # callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.
        api_instance.v05_subscription_requests_cm_on_init_post(authorization, x_hiu_id, hiu_subscription_request_receipt)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->v05_subscription_requests_cm_on_init_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **hiu_subscription_request_receipt** | [**HIUSubscriptionRequestReceipt**](HIUSubscriptionRequestReceipt.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted. |  -  |
**401** | **Causes:**   * Invalid/Expired/Empty token.  |  -  |
**500** | **Causes:**   * Downstream services are down  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_subscription_requests_hiu_notify_post**
> v05_subscription_requests_hiu_notify_post(authorization, x_hiu_id, subscription_approval_notification)

Notification for subscription grant/deny/revoke

This API is used by CM to notify a HIU to grant or deny a request for subscription, and also to notify that in case an existing subscription is revoked or expired. For notifying that a particular subscription request was GRANTED or DENIED, the **subscriptionRequestId** is passed. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.subscription_approval_notification import SubscriptionApprovalNotification
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
    api_instance = abdm_gateway.SubscriptionsApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    subscription_approval_notification = abdm_gateway.SubscriptionApprovalNotification() # SubscriptionApprovalNotification | 

    try:
        # Notification for subscription grant/deny/revoke
        api_instance.v05_subscription_requests_hiu_notify_post(authorization, x_hiu_id, subscription_approval_notification)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->v05_subscription_requests_hiu_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **subscription_approval_notification** | [**SubscriptionApprovalNotification**](SubscriptionApprovalNotification.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted |  -  |
**400** | **Causes:**   * Invalid data sent    * Required attributes not mentioned  |  -  |
**401** | **Causes:**   * Expired/Invalid token.  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_subscription_requests_hiu_on_notify_post**
> v05_subscription_requests_hiu_on_notify_post(authorization, x_cm_id, hiu_subscription_request_notification_acknowledgement)

Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.

This API is called by HIU as acknowledgement to subscription request relevant notifications. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hiu_subscription_request_notification_acknowledgement import HIUSubscriptionRequestNotificationAcknowledgement
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
    api_instance = abdm_gateway.SubscriptionsApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    hiu_subscription_request_notification_acknowledgement = abdm_gateway.HIUSubscriptionRequestNotificationAcknowledgement() # HIUSubscriptionRequestNotificationAcknowledgement | 

    try:
        # Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.
        api_instance.v05_subscription_requests_hiu_on_notify_post(authorization, x_cm_id, hiu_subscription_request_notification_acknowledgement)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->v05_subscription_requests_hiu_on_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **hiu_subscription_request_notification_acknowledgement** | [**HIUSubscriptionRequestNotificationAcknowledgement**](HIUSubscriptionRequestNotificationAcknowledgement.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted. |  -  |
**401** | **Causes:**   * Invalid/Expired/Empty token.  |  -  |
**500** | **Causes:**   * Downstream services are down  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_subscriptions_hiu_notify_post**
> v05_subscriptions_hiu_notify_post(authorization, x_hiu_id, hiu_subscription_notification)

Notification to HIU on basis of a granted subscription

This API is used by CM to notify a HIU for notification relevant to subscription. Notifications are sent to subscribed HIUs whenever a new care-context is linked or new data is available on an existing linked care-context.  1. if event.category = LINK, then only care-contexts are passed when new care-contexts are linked for patient.  2. If event.category = DATA, then hiTypes are passed. Care-context is passed only if the subscribed HIU has any valid consent for that care-context 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hiu_subscription_notification import HIUSubscriptionNotification
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
    api_instance = abdm_gateway.SubscriptionsApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_hiu_id = 'x_hiu_id_example' # str | Identifier of the health information user to which the request was intended.
    hiu_subscription_notification = abdm_gateway.HIUSubscriptionNotification() # HIUSubscriptionNotification | 

    try:
        # Notification to HIU on basis of a granted subscription
        api_instance.v05_subscriptions_hiu_notify_post(authorization, x_hiu_id, hiu_subscription_notification)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->v05_subscriptions_hiu_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_hiu_id** | **str**| Identifier of the health information user to which the request was intended. | 
 **hiu_subscription_notification** | [**HIUSubscriptionNotification**](HIUSubscriptionNotification.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted |  -  |
**400** | **Causes:**   * Invalid data sent    * Required attributes not mentioned  |  -  |
**401** | **Causes:**   * Expired/Invalid token.  |  -  |
**500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v05_subscriptions_hiu_on_notify_post**
> v05_subscriptions_hiu_on_notify_post(authorization, x_cm_id, hiu_subscription_notification_acknowledgment)

Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.

This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

### Example


```python
import abdm_gateway
from abdm_gateway.models.hiu_subscription_notification_acknowledgment import HIUSubscriptionNotificationAcknowledgment
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
    api_instance = abdm_gateway.SubscriptionsApi(api_client)
    authorization = 'authorization_example' # str | Access token which was issued after successful login with gateway auth server.
    x_cm_id = 'x_cm_id_example' # str | Suffix of the consent manager to which the request was intended.
    hiu_subscription_notification_acknowledgment = abdm_gateway.HIUSubscriptionNotificationAcknowledgment() # HIUSubscriptionNotificationAcknowledgment | 

    try:
        # Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.
        api_instance.v05_subscriptions_hiu_on_notify_post(authorization, x_cm_id, hiu_subscription_notification_acknowledgment)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->v05_subscriptions_hiu_on_notify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Access token which was issued after successful login with gateway auth server. | 
 **x_cm_id** | **str**| Suffix of the consent manager to which the request was intended. | 
 **hiu_subscription_notification_acknowledgment** | [**HIUSubscriptionNotificationAcknowledgment**](HIUSubscriptionNotificationAcknowledgment.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted. |  -  |
**401** | **Causes:**   * Invalid/Expired/Empty token.  |  -  |
**500** | **Causes:**   * Downstream services are down  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

