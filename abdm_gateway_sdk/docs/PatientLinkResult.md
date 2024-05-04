# PatientLinkResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**patient** | [**PatientLinkResultPatient**](PatientLinkResultPatient.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**resp** | [**RequestReference**](RequestReference.md) |  | 

## Example

```python
from abdm_gateway.models.patient_link_result import PatientLinkResult

# TODO update the JSON string below
json = "{}"
# create an instance of PatientLinkResult from a JSON string
patient_link_result_instance = PatientLinkResult.from_json(json)
# print the JSON string representation of the object
print(PatientLinkResult.to_json())

# convert the object into a dict
patient_link_result_dict = patient_link_result_instance.to_dict()
# create an instance of PatientLinkResult from a dict
patient_link_result_from_dict = PatientLinkResult.from_dict(patient_link_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


