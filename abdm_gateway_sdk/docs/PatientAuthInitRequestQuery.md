# PatientAuthInitRequestQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id  of the patient understood by the CM | 
**purpose** | [**PatientAuthPurpose**](PatientAuthPurpose.md) |  | 
**auth_mode** | [**AuthenticationMode**](AuthenticationMode.md) |  | [optional] 
**requester** | [**PatientAuthRequester**](PatientAuthRequester.md) |  | 

## Example

```python
from abdm_gateway.models.patient_auth_init_request_query import PatientAuthInitRequestQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthInitRequestQuery from a JSON string
patient_auth_init_request_query_instance = PatientAuthInitRequestQuery.from_json(json)
# print the JSON string representation of the object
print(PatientAuthInitRequestQuery.to_json())

# convert the object into a dict
patient_auth_init_request_query_dict = patient_auth_init_request_query_instance.to_dict()
# create an instance of PatientAuthInitRequestQuery from a dict
patient_auth_init_request_query_from_dict = PatientAuthInitRequestQuery.from_dict(patient_auth_init_request_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


