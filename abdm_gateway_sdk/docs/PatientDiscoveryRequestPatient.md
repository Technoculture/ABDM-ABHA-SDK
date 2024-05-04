# PatientDiscoveryRequestPatient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of patient at consent manager | 
**verified_identifiers** | [**List[Identifier]**](Identifier.md) |  | 
**unverified_identifiers** | [**List[Identifier]**](Identifier.md) |  | [optional] 
**name** | **str** |  | 
**gender** | [**PatientGender**](PatientGender.md) |  | 
**year_of_birth** | **int** |  | 

## Example

```python
from abdm_gateway.models.patient_discovery_request_patient import PatientDiscoveryRequestPatient

# TODO update the JSON string below
json = "{}"
# create an instance of PatientDiscoveryRequestPatient from a JSON string
patient_discovery_request_patient_instance = PatientDiscoveryRequestPatient.from_json(json)
# print the JSON string representation of the object
print(PatientDiscoveryRequestPatient.to_json())

# convert the object into a dict
patient_discovery_request_patient_dict = patient_discovery_request_patient_instance.to_dict()
# create an instance of PatientDiscoveryRequestPatient from a dict
patient_discovery_request_patient_from_dict = PatientDiscoveryRequestPatient.from_dict(patient_discovery_request_patient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


