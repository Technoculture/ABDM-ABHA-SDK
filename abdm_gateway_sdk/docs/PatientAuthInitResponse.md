# PatientAuthInitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**auth** | [**PatientAuthInitResponseAuth**](PatientAuthInitResponseAuth.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**resp** | [**RequestReference**](RequestReference.md) |  | 

## Example

```python
from abdm_gateway.models.patient_auth_init_response import PatientAuthInitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthInitResponse from a JSON string
patient_auth_init_response_instance = PatientAuthInitResponse.from_json(json)
# print the JSON string representation of the object
print(PatientAuthInitResponse.to_json())

# convert the object into a dict
patient_auth_init_response_dict = patient_auth_init_response_instance.to_dict()
# create an instance of PatientAuthInitResponse from a dict
patient_auth_init_response_from_dict = PatientAuthInitResponse.from_dict(patient_auth_init_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


