# PatientSMSNotifcationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**notification** | [**PatientSMSNotifcationRequestNotification**](PatientSMSNotifcationRequestNotification.md) |  | 

## Example

```python
from abdm_gateway.models.patient_sms_notifcation_request import PatientSMSNotifcationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatientSMSNotifcationRequest from a JSON string
patient_sms_notifcation_request_instance = PatientSMSNotifcationRequest.from_json(json)
# print the JSON string representation of the object
print(PatientSMSNotifcationRequest.to_json())

# convert the object into a dict
patient_sms_notifcation_request_dict = patient_sms_notifcation_request_instance.to_dict()
# create an instance of PatientSMSNotifcationRequest from a dict
patient_sms_notifcation_request_from_dict = PatientSMSNotifcationRequest.from_dict(patient_sms_notifcation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


