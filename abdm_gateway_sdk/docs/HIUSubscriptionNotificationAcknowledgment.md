# HIUSubscriptionNotificationAcknowledgment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**acknowledgement** | [**HIUSubscriptionNotificationAcknowledgmentAcknowledgement**](HIUSubscriptionNotificationAcknowledgmentAcknowledgement.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**resp** | [**RequestReference**](RequestReference.md) |  | 

## Example

```python
from abdm_gateway.models.hiu_subscription_notification_acknowledgment import HIUSubscriptionNotificationAcknowledgment

# TODO update the JSON string below
json = "{}"
# create an instance of HIUSubscriptionNotificationAcknowledgment from a JSON string
hiu_subscription_notification_acknowledgment_instance = HIUSubscriptionNotificationAcknowledgment.from_json(json)
# print the JSON string representation of the object
print(HIUSubscriptionNotificationAcknowledgment.to_json())

# convert the object into a dict
hiu_subscription_notification_acknowledgment_dict = hiu_subscription_notification_acknowledgment_instance.to_dict()
# create an instance of HIUSubscriptionNotificationAcknowledgment from a dict
hiu_subscription_notification_acknowledgment_from_dict = HIUSubscriptionNotificationAcknowledgment.from_dict(hiu_subscription_notification_acknowledgment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


