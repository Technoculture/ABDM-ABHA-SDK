# PatientLinkResultPatient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_number** | **str** |  | 
**display** | **str** |  | 
**care_contexts** | [**List[CareContextRepresentation]**](CareContextRepresentation.md) |  | 

## Example

```python
from abdm_gateway.models.patient_link_result_patient import PatientLinkResultPatient

# TODO update the JSON string below
json = "{}"
# create an instance of PatientLinkResultPatient from a JSON string
patient_link_result_patient_instance = PatientLinkResultPatient.from_json(json)
# print the JSON string representation of the object
print(PatientLinkResultPatient.to_json())

# convert the object into a dict
patient_link_result_patient_dict = patient_link_result_patient_instance.to_dict()
# create an instance of PatientLinkResultPatient from a dict
patient_link_result_patient_from_dict = PatientLinkResultPatient.from_dict(patient_link_result_patient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


