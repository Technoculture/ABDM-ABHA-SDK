# PatientAuthRequester

identification of requester

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from abdm_gateway.models.patient_auth_requester import PatientAuthRequester

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAuthRequester from a JSON string
patient_auth_requester_instance = PatientAuthRequester.from_json(json)
# print the JSON string representation of the object
print(PatientAuthRequester.to_json())

# convert the object into a dict
patient_auth_requester_dict = patient_auth_requester_instance.to_dict()
# create an instance of PatientAuthRequester from a dict
patient_auth_requester_from_dict = PatientAuthRequester.from_dict(patient_auth_requester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


