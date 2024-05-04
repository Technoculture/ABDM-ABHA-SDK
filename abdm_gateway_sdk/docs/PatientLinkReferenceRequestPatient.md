# PatientLinkReferenceRequestPatient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of patient at consent manager | 
**reference_number** | **str** |  | 
**care_contexts** | [**List[CareContext]**](CareContext.md) |  | 

## Example

```python
from abdm_gateway.models.patient_link_reference_request_patient import PatientLinkReferenceRequestPatient

# TODO update the JSON string below
json = "{}"
# create an instance of PatientLinkReferenceRequestPatient from a JSON string
patient_link_reference_request_patient_instance = PatientLinkReferenceRequestPatient.from_json(json)
# print the JSON string representation of the object
print(PatientLinkReferenceRequestPatient.to_json())

# convert the object into a dict
patient_link_reference_request_patient_dict = patient_link_reference_request_patient_instance.to_dict()
# create an instance of PatientLinkReferenceRequestPatient from a dict
patient_link_reference_request_patient_from_dict = PatientLinkReferenceRequestPatient.from_dict(patient_link_reference_request_patient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


