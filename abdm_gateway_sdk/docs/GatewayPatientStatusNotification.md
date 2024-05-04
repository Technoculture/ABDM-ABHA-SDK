# GatewayPatientStatusNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**acknowledgment** | [**PatientAuthNotificationAcknowledgementAcknowledgement**](PatientAuthNotificationAcknowledgementAcknowledgement.md) |  | 
**error** | [**Error**](Error.md) |  | [optional] 
**resp** | [**RequestReference**](RequestReference.md) |  | [optional] 

## Example

```python
from abdm_gateway.models.gateway_patient_status_notification import GatewayPatientStatusNotification

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayPatientStatusNotification from a JSON string
gateway_patient_status_notification_instance = GatewayPatientStatusNotification.from_json(json)
# print the JSON string representation of the object
print(GatewayPatientStatusNotification.to_json())

# convert the object into a dict
gateway_patient_status_notification_dict = gateway_patient_status_notification_instance.to_dict()
# create an instance of GatewayPatientStatusNotification from a dict
gateway_patient_status_notification_from_dict = GatewayPatientStatusNotification.from_dict(gateway_patient_status_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


