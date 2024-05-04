# HIUSubscriptionRequestNotificationAcknowledgement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**acknowledgement** | [**HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement**](HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**resp** | [**RequestReference**](RequestReference.md) |  | 

## Example

```python
from abdm_gateway.models.hiu_subscription_request_notification_acknowledgement import HIUSubscriptionRequestNotificationAcknowledgement

# TODO update the JSON string below
json = "{}"
# create an instance of HIUSubscriptionRequestNotificationAcknowledgement from a JSON string
hiu_subscription_request_notification_acknowledgement_instance = HIUSubscriptionRequestNotificationAcknowledgement.from_json(json)
# print the JSON string representation of the object
print(HIUSubscriptionRequestNotificationAcknowledgement.to_json())

# convert the object into a dict
hiu_subscription_request_notification_acknowledgement_dict = hiu_subscription_request_notification_acknowledgement_instance.to_dict()
# create an instance of HIUSubscriptionRequestNotificationAcknowledgement from a dict
hiu_subscription_request_notification_acknowledgement_from_dict = HIUSubscriptionRequestNotificationAcknowledgement.from_dict(hiu_subscription_request_notification_acknowledgement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


