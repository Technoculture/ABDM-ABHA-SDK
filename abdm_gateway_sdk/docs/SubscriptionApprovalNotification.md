# SubscriptionApprovalNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**notification** | [**SubscriptionApprovalNotificationNotification**](SubscriptionApprovalNotificationNotification.md) |  | 

## Example

```python
from abdm_gateway.models.subscription_approval_notification import SubscriptionApprovalNotification

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionApprovalNotification from a JSON string
subscription_approval_notification_instance = SubscriptionApprovalNotification.from_json(json)
# print the JSON string representation of the object
print(SubscriptionApprovalNotification.to_json())

# convert the object into a dict
subscription_approval_notification_dict = subscription_approval_notification_instance.to_dict()
# create an instance of SubscriptionApprovalNotification from a dict
subscription_approval_notification_from_dict = SubscriptionApprovalNotification.from_dict(subscription_approval_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


