# PatientAuthNotificationAuth

depending on the purpose of auth, as specified in /auth/init, the response may include the following    1. LINK - only returns **accessToken**   2. KYC - only returns **patient**   3. KYC_AND_LINK - returns both **accessToken** and **patient** 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | transaction id for auth session | 
**status** | **str** |  | 
**access_token** | **str** | access token for initialization of subsequent action. | [optional] 
**validity** | [**AccessTokenValidity**](AccessTokenValidity.md) |  | [optional] 
**patient** | [**PatientDemographicResponse**](PatientDemographicResponse.md) |  | [optional] 

## Example

```python
from abdm_gateway.models.patient_auth_notification_auth import PatientAuthNotificationAuth

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthNotificationAuth from a JSON string
patient_auth_notification_auth_instance = PatientAuthNotificationAuth.from_json(json)
# print the JSON string representation of the object
print(PatientAuthNotificationAuth.to_json())

# convert the object into a dict
patient_auth_notification_auth_dict = patient_auth_notification_auth_instance.to_dict()
# create an instance of PatientAuthNotificationAuth from a dict
patient_auth_notification_auth_from_dict = PatientAuthNotificationAuth.from_dict(patient_auth_notification_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


