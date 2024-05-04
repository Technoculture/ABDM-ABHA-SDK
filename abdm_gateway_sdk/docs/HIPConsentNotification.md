# HIPConsentNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**notification** | [**HIPConsentNotificationNotification**](HIPConsentNotificationNotification.md) |  | 

## Example

```python
from abdm_gateway.models.hip_consent_notification import HIPConsentNotification

# TODO update the JSON string below
json = "{}"
# create an instance of HIPConsentNotification from a JSON string
hip_consent_notification_instance = HIPConsentNotification.from_json(json)
# print the JSON string representation of the object
print(HIPConsentNotification.to_json())

# convert the object into a dict
hip_consent_notification_dict = hip_consent_notification_instance.to_dict()
# create an instance of HIPConsentNotification from a dict
hip_consent_notification_from_dict = HIPConsentNotification.from_dict(hip_consent_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


