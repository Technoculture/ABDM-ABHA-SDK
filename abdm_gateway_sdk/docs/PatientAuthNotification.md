# PatientAuthNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**auth** | [**PatientAuthNotificationAuth**](PatientAuthNotificationAuth.md) |  | [optional] 

## Example

```python
from abdm_gateway.models.patient_auth_notification import PatientAuthNotification

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthNotification from a JSON string
patient_auth_notification_instance = PatientAuthNotification.from_json(json)
# print the JSON string representation of the object
print(PatientAuthNotification.to_json())

# convert the object into a dict
patient_auth_notification_dict = patient_auth_notification_instance.to_dict()
# create an instance of PatientAuthNotification from a dict
patient_auth_notification_from_dict = PatientAuthNotification.from_dict(patient_auth_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


