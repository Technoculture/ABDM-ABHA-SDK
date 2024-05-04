# HealthInformationNotificationNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_id** | **str** |  | 
**transaction_id** | **str** |  | 
**done_at** | **datetime** |  | 
**notifier** | [**HealthInformationNotificationNotificationNotifier**](HealthInformationNotificationNotificationNotifier.md) |  | 
**status_notification** | [**HealthInformationNotificationNotificationStatusNotification**](HealthInformationNotificationNotificationStatusNotification.md) |  | 

## Example

```python
from abdm_gateway.models.health_information_notification_notification import HealthInformationNotificationNotification

# TODO update the JSON string below
json = "{}"
# create an instance of HealthInformationNotificationNotification from a JSON string
health_information_notification_notification_instance = HealthInformationNotificationNotification.from_json(json)
# print the JSON string representation of the object
print(HealthInformationNotificationNotification.to_json())

# convert the object into a dict
health_information_notification_notification_dict = health_information_notification_notification_instance.to_dict()
# create an instance of HealthInformationNotificationNotification from a dict
health_information_notification_notification_from_dict = HealthInformationNotificationNotification.from_dict(health_information_notification_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


