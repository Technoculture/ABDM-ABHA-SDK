# PatientAuthNotificationAcknowledgement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**acknowledgement** | [**PatientAuthNotificationAcknowledgementAcknowledgement**](PatientAuthNotificationAcknowledgementAcknowledgement.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**resp** | [**RequestReference**](RequestReference.md) |  | 

## Example

```python
from abdm_gateway.models.patient_auth_notification_acknowledgement import PatientAuthNotificationAcknowledgement

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthNotificationAcknowledgement from a JSON string
patient_auth_notification_acknowledgement_instance = PatientAuthNotificationAcknowledgement.from_json(json)
# print the JSON string representation of the object
print(PatientAuthNotificationAcknowledgement.to_json())

# convert the object into a dict
patient_auth_notification_acknowledgement_dict = patient_auth_notification_acknowledgement_instance.to_dict()
# create an instance of PatientAuthNotificationAcknowledgement from a dict
patient_auth_notification_acknowledgement_from_dict = PatientAuthNotificationAcknowledgement.from_dict(patient_auth_notification_acknowledgement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


