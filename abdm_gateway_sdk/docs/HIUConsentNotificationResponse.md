# HIUConsentNotificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**acknowledgement** | [**List[ConsentAcknowledgement]**](ConsentAcknowledgement.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**resp** | [**RequestReference**](RequestReference.md) |  | 

## Example

```python
from abdm_gateway.models.hiu_consent_notification_response import HIUConsentNotificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HIUConsentNotificationResponse from a JSON string
hiu_consent_notification_response_instance = HIUConsentNotificationResponse.from_json(json)
# print the JSON string representation of the object
print(HIUConsentNotificationResponse.to_json())

# convert the object into a dict
hiu_consent_notification_response_dict = hiu_consent_notification_response_instance.to_dict()
# create an instance of HIUConsentNotificationResponse from a dict
hiu_consent_notification_response_from_dict = HIUConsentNotificationResponse.from_dict(hiu_consent_notification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


