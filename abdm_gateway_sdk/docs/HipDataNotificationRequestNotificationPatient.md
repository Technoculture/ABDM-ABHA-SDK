# HipDataNotificationRequestNotificationPatient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A patient identifier, abdm id or abdm number | 

## Example

```python
from abdm_gateway.models.hip_data_notification_request_notification_patient import HipDataNotificationRequestNotificationPatient

# TODO update the JSON string below
json = "{}"
# create an instance of HipDataNotificationRequestNotificationPatient from a JSON string
hip_data_notification_request_notification_patient_instance = HipDataNotificationRequestNotificationPatient.from_json(json)
# print the JSON string representation of the object
print(HipDataNotificationRequestNotificationPatient.to_json())

# convert the object into a dict
hip_data_notification_request_notification_patient_dict = hip_data_notification_request_notification_patient_instance.to_dict()
# create an instance of HipDataNotificationRequestNotificationPatient from a dict
hip_data_notification_request_notification_patient_from_dict = HipDataNotificationRequestNotificationPatient.from_dict(hip_data_notification_request_notification_patient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


