# PatientCareContextLinkPatient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_number** | **str** | patient reference id at HIP | 
**display** | **str** |  | 
**care_contexts** | [**List[CareContextRepresentation]**](CareContextRepresentation.md) |  | 

## Example

```python
from abdm_gateway.models.patient_care_context_link_patient import PatientCareContextLinkPatient

# TODO update the JSON string below
json = "{}"
# create an instance of PatientCareContextLinkPatient from a JSON string
patient_care_context_link_patient_instance = PatientCareContextLinkPatient.from_json(json)
# print the JSON string representation of the object
print(PatientCareContextLinkPatient.to_json())

# convert the object into a dict
patient_care_context_link_patient_dict = patient_care_context_link_patient_instance.to_dict()
# create an instance of PatientCareContextLinkPatient from a dict
patient_care_context_link_patient_from_dict = PatientCareContextLinkPatient.from_dict(patient_care_context_link_patient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


