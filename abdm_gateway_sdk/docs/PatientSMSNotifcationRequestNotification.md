# PatientSMSNotifcationRequestNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_no** | **str** | Phone number of the receiver with country code | 
**receiver_name** | **str** | Name of the reciever/patient. Receiver&#39;s name will not be sent if not provided. | [optional] 
**care_context_info** | **str** | Information about care context or visit for which the SMS is being sent. | 
**deeplink_url** | **str** | A link pointing to digital health records of the patient. ABHA Mobile Application&#39;s deeplink will be sent in SMS if this field is not provided. | [optional] 
**hip** | [**PatientSMSNotifcationRequestNotificationHip**](PatientSMSNotifcationRequestNotificationHip.md) |  | 

## Example

```python
from abdm_gateway.models.patient_sms_notifcation_request_notification import PatientSMSNotifcationRequestNotification

# TODO update the JSON string below
json = "{}"
# create an instance of PatientSMSNotifcationRequestNotification from a JSON string
patient_sms_notifcation_request_notification_instance = PatientSMSNotifcationRequestNotification.from_json(json)
# print the JSON string representation of the object
print(PatientSMSNotifcationRequestNotification.to_json())

# convert the object into a dict
patient_sms_notifcation_request_notification_dict = patient_sms_notifcation_request_notification_instance.to_dict()
# create an instance of PatientSMSNotifcationRequestNotification from a dict
patient_sms_notifcation_request_notification_from_dict = PatientSMSNotifcationRequestNotification.from_dict(patient_sms_notifcation_request_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


