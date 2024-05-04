# PatientAuthInitResponseAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 
**mode** | [**AuthenticationMode**](AuthenticationMode.md) |  | 
**meta** | [**AuthMeta**](AuthMeta.md) |  | [optional] 

## Example

```python
from abdm_gateway.models.patient_auth_init_response_auth import PatientAuthInitResponseAuth

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthInitResponseAuth from a JSON string
patient_auth_init_response_auth_instance = PatientAuthInitResponseAuth.from_json(json)
# print the JSON string representation of the object
print(PatientAuthInitResponseAuth.to_json())

# convert the object into a dict
patient_auth_init_response_auth_dict = patient_auth_init_response_auth_instance.to_dict()
# create an instance of PatientAuthInitResponseAuth from a dict
patient_auth_init_response_auth_from_dict = PatientAuthInitResponseAuth.from_dict(patient_auth_init_response_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


