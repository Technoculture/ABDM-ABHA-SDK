# HealthInformationNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request. | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**notification** | [**HealthInformationNotificationNotification**](HealthInformationNotificationNotification.md) |  | 

## Example

```python
from abdm_gateway.models.health_information_notification import HealthInformationNotification

# TODO update the JSON string below
json = "{}"
# create an instance of HealthInformationNotification from a JSON string
health_information_notification_instance = HealthInformationNotification.from_json(json)
# print the JSON string representation of the object
print(HealthInformationNotification.to_json())

# convert the object into a dict
health_information_notification_dict = health_information_notification_instance.to_dict()
# create an instance of HealthInformationNotification from a dict
health_information_notification_from_dict = HealthInformationNotification.from_dict(health_information_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


