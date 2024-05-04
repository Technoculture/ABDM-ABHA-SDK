# HIUSubscriptionNotificationEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**published** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**subscription_id** | **str** |  | 
**category** | [**SubscriptionCategory**](SubscriptionCategory.md) |  | 
**content** | [**HIUSubscriptionEventContent**](HIUSubscriptionEventContent.md) |  | 

## Example

```python
from abdm_gateway.models.hiu_subscription_notification_event import HIUSubscriptionNotificationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HIUSubscriptionNotificationEvent from a JSON string
hiu_subscription_notification_event_instance = HIUSubscriptionNotificationEvent.from_json(json)
# print the JSON string representation of the object
print(HIUSubscriptionNotificationEvent.to_json())

# convert the object into a dict
hiu_subscription_notification_event_dict = hiu_subscription_notification_event_instance.to_dict()
# create an instance of HIUSubscriptionNotificationEvent from a dict
hiu_subscription_notification_event_from_dict = HIUSubscriptionNotificationEvent.from_dict(hiu_subscription_notification_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


