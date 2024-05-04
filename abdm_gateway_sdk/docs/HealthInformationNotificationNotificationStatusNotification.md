# HealthInformationNotificationNotificationStatusNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_status** | **str** |  | 
**hip_id** | **str** |  | 
**status_responses** | [**List[HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner]**](HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.md) |  | [optional] 

## Example

```python
from abdm_gateway.models.health_information_notification_notification_status_notification import HealthInformationNotificationNotificationStatusNotification

# TODO update the JSON string below
json = "{}"
# create an instance of HealthInformationNotificationNotificationStatusNotification from a JSON string
health_information_notification_notification_status_notification_instance = HealthInformationNotificationNotificationStatusNotification.from_json(json)
# print the JSON string representation of the object
print(HealthInformationNotificationNotificationStatusNotification.to_json())

# convert the object into a dict
health_information_notification_notification_status_notification_dict = health_information_notification_notification_status_notification_instance.to_dict()
# create an instance of HealthInformationNotificationNotificationStatusNotification from a dict
health_information_notification_notification_status_notification_from_dict = HealthInformationNotificationNotificationStatusNotification.from_dict(health_information_notification_notification_status_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


