# PatientAuthConfirmRequestCredential

note, demographic details are only required for demographic auth at this point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_code** | **str** |  | [optional] 
**demographic** | [**PatientDemographic**](PatientDemographic.md) |  | [optional] 

## Example

```python
from abdm_gateway.models.patient_auth_confirm_request_credential import PatientAuthConfirmRequestCredential

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthConfirmRequestCredential from a JSON string
patient_auth_confirm_request_credential_instance = PatientAuthConfirmRequestCredential.from_json(json)
# print the JSON string representation of the object
print(PatientAuthConfirmRequestCredential.to_json())

# convert the object into a dict
patient_auth_confirm_request_credential_dict = patient_auth_confirm_request_credential_instance.to_dict()
# create an instance of PatientAuthConfirmRequestCredential from a dict
patient_auth_confirm_request_credential_from_dict = PatientAuthConfirmRequestCredential.from_dict(patient_auth_confirm_request_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


