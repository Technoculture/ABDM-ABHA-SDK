# PatientAuthInitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**query** | [**PatientAuthInitRequestQuery**](PatientAuthInitRequestQuery.md) |  | 

## Example

```python
from abdm_gateway.models.patient_auth_init_request import PatientAuthInitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthInitRequest from a JSON string
patient_auth_init_request_instance = PatientAuthInitRequest.from_json(json)
# print the JSON string representation of the object
print(PatientAuthInitRequest.to_json())

# convert the object into a dict
patient_auth_init_request_dict = patient_auth_init_request_instance.to_dict()
# create an instance of PatientAuthInitRequest from a dict
patient_auth_init_request_from_dict = PatientAuthInitRequest.from_dict(patient_auth_init_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


