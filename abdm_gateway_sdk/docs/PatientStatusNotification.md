# PatientStatusNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**notification** | [**PatientStatusNotificationNotification**](PatientStatusNotificationNotification.md) |  | 

## Example

```python
from abdm_gateway.models.patient_status_notification import PatientStatusNotification

# TODO update the JSON string below
json = "{}"
# create an instance of PatientStatusNotification from a JSON string
patient_status_notification_instance = PatientStatusNotification.from_json(json)
# print the JSON string representation of the object
print(PatientStatusNotification.to_json())

# convert the object into a dict
patient_status_notification_dict = patient_status_notification_instance.to_dict()
# create an instance of PatientStatusNotification from a dict
patient_status_notification_from_dict = PatientStatusNotification.from_dict(patient_status_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


