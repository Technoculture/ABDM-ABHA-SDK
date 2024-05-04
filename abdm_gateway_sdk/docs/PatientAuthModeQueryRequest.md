# PatientAuthModeQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**query** | [**PatientAuthModeQueryRequestQuery**](PatientAuthModeQueryRequestQuery.md) |  | 

## Example

```python
from abdm_gateway.models.patient_auth_mode_query_request import PatientAuthModeQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthModeQueryRequest from a JSON string
patient_auth_mode_query_request_instance = PatientAuthModeQueryRequest.from_json(json)
# print the JSON string representation of the object
print(PatientAuthModeQueryRequest.to_json())

# convert the object into a dict
patient_auth_mode_query_request_dict = patient_auth_mode_query_request_instance.to_dict()
# create an instance of PatientAuthModeQueryRequest from a dict
patient_auth_mode_query_request_from_dict = PatientAuthModeQueryRequest.from_dict(patient_auth_mode_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


