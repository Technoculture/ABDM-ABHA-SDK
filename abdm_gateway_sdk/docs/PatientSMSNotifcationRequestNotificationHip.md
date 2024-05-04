# PatientSMSNotifcationRequestNotificationHip


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the HIP(Hospital). Hospital&#39;s name will be fetched from registry if not provided. | [optional] 
**id** | **str** | Registered id of the HIP. | 

## Example

```python
from abdm_gateway.models.patient_sms_notifcation_request_notification_hip import PatientSMSNotifcationRequestNotificationHip

# TODO update the JSON string below
json = "{}"
# create an instance of PatientSMSNotifcationRequestNotificationHip from a JSON string
patient_sms_notifcation_request_notification_hip_instance = PatientSMSNotifcationRequestNotificationHip.from_json(json)
# print the JSON string representation of the object
print(PatientSMSNotifcationRequestNotificationHip.to_json())

# convert the object into a dict
patient_sms_notifcation_request_notification_hip_dict = patient_sms_notifcation_request_notification_hip_instance.to_dict()
# create an instance of PatientSMSNotifcationRequestNotificationHip from a dict
patient_sms_notifcation_request_notification_hip_from_dict = PatientSMSNotifcationRequestNotificationHip.from_dict(patient_sms_notifcation_request_notification_hip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


