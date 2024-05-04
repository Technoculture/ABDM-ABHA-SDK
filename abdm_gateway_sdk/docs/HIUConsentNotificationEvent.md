# HIUConsentNotificationEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**notification** | [**HIUConsentNotificationEventNotification**](HIUConsentNotificationEventNotification.md) |  | 

## Example

```python
from abdm_gateway.models.hiu_consent_notification_event import HIUConsentNotificationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HIUConsentNotificationEvent from a JSON string
hiu_consent_notification_event_instance = HIUConsentNotificationEvent.from_json(json)
# print the JSON string representation of the object
print(HIUConsentNotificationEvent.to_json())

# convert the object into a dict
hiu_consent_notification_event_dict = hiu_consent_notification_event_instance.to_dict()
# create an instance of HIUConsentNotificationEvent from a dict
hiu_consent_notification_event_from_dict = HIUConsentNotificationEvent.from_dict(hiu_consent_notification_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


