# PatientIdentificationResponsePatient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from abdm_gateway.models.patient_identification_response_patient import PatientIdentificationResponsePatient

# TODO update the JSON string below
json = "{}"
# create an instance of PatientIdentificationResponsePatient from a JSON string
patient_identification_response_patient_instance = PatientIdentificationResponsePatient.from_json(json)
# print the JSON string representation of the object
print(PatientIdentificationResponsePatient.to_json())

# convert the object into a dict
patient_identification_response_patient_dict = patient_identification_response_patient_instance.to_dict()
# create an instance of PatientIdentificationResponsePatient from a dict
patient_identification_response_patient_from_dict = PatientIdentificationResponsePatient.from_dict(patient_identification_response_patient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


