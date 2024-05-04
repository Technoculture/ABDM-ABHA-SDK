# PatientAuthModeQueryResponseAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | [**PatientAuthPurpose**](PatientAuthPurpose.md) |  | 
**modes** | [**List[AuthenticationMode]**](AuthenticationMode.md) |  | 

## Example

```python
from abdm_gateway.models.patient_auth_mode_query_response_auth import PatientAuthModeQueryResponseAuth

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthModeQueryResponseAuth from a JSON string
patient_auth_mode_query_response_auth_instance = PatientAuthModeQueryResponseAuth.from_json(json)
# print the JSON string representation of the object
print(PatientAuthModeQueryResponseAuth.to_json())

# convert the object into a dict
patient_auth_mode_query_response_auth_dict = patient_auth_mode_query_response_auth_instance.to_dict()
# create an instance of PatientAuthModeQueryResponseAuth from a dict
patient_auth_mode_query_response_auth_from_dict = PatientAuthModeQueryResponseAuth.from_dict(patient_auth_mode_query_response_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


