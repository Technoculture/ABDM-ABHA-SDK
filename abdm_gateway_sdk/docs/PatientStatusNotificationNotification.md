# PatientStatusNotificationNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**patient** | [**PatientStatusNotificationNotificationPatient**](PatientStatusNotificationNotificationPatient.md) |  | 

## Example

```python
from abdm_gateway.models.patient_status_notification_notification import PatientStatusNotificationNotification

# TODO update the JSON string below
json = "{}"
# create an instance of PatientStatusNotificationNotification from a JSON string
patient_status_notification_notification_instance = PatientStatusNotificationNotification.from_json(json)
# print the JSON string representation of the object
print(PatientStatusNotificationNotification.to_json())

# convert the object into a dict
patient_status_notification_notification_dict = patient_status_notification_notification_instance.to_dict()
# create an instance of PatientStatusNotificationNotification from a dict
patient_status_notification_notification_from_dict = PatientStatusNotificationNotification.from_dict(patient_status_notification_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


