# HIUSubscriptionNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**event** | [**HIUSubscriptionNotificationEvent**](HIUSubscriptionNotificationEvent.md) |  | 

## Example

```python
from abdm_gateway.models.hiu_subscription_notification import HIUSubscriptionNotification

# TODO update the JSON string below
json = "{}"
# create an instance of HIUSubscriptionNotification from a JSON string
hiu_subscription_notification_instance = HIUSubscriptionNotification.from_json(json)
# print the JSON string representation of the object
print(HIUSubscriptionNotification.to_json())

# convert the object into a dict
hiu_subscription_notification_dict = hiu_subscription_notification_instance.to_dict()
# create an instance of HIUSubscriptionNotification from a dict
hiu_subscription_notification_from_dict = HIUSubscriptionNotification.from_dict(hiu_subscription_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


