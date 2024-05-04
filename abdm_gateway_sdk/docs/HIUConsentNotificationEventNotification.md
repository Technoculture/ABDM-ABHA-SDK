# HIUConsentNotificationEventNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_request_id** | **str** |  | 
**status** | [**ConsentStatus**](ConsentStatus.md) |  | 
**consent_artefacts** | [**List[ConsentArtefactReference]**](ConsentArtefactReference.md) | if the status is GRANTED or REVOKED, then the consentArtefact references (Ids) must be specified. | [optional] 

## Example

```python
from abdm_gateway.models.hiu_consent_notification_event_notification import HIUConsentNotificationEventNotification

# TODO update the JSON string below
json = "{}"
# create an instance of HIUConsentNotificationEventNotification from a JSON string
hiu_consent_notification_event_notification_instance = HIUConsentNotificationEventNotification.from_json(json)
# print the JSON string representation of the object
print(HIUConsentNotificationEventNotification.to_json())

# convert the object into a dict
hiu_consent_notification_event_notification_dict = hiu_consent_notification_event_notification_instance.to_dict()
# create an instance of HIUConsentNotificationEventNotification from a dict
hiu_consent_notification_event_notification_from_dict = HIUConsentNotificationEventNotification.from_dict(hiu_consent_notification_event_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


