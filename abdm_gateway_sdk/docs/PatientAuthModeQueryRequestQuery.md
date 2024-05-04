# PatientAuthModeQueryRequestQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**purpose** | [**PatientAuthPurpose**](PatientAuthPurpose.md) |  | 
**requester** | [**PatientAuthModeQueryRequestQueryRequester**](PatientAuthModeQueryRequestQueryRequester.md) |  | 

## Example

```python
from abdm_gateway.models.patient_auth_mode_query_request_query import PatientAuthModeQueryRequestQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthModeQueryRequestQuery from a JSON string
patient_auth_mode_query_request_query_instance = PatientAuthModeQueryRequestQuery.from_json(json)
# print the JSON string representation of the object
print(PatientAuthModeQueryRequestQuery.to_json())

# convert the object into a dict
patient_auth_mode_query_request_query_dict = patient_auth_mode_query_request_query_instance.to_dict()
# create an instance of PatientAuthModeQueryRequestQuery from a dict
patient_auth_mode_query_request_query_from_dict = PatientAuthModeQueryRequestQuery.from_dict(patient_auth_mode_query_request_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


