# PatientIdentificationRequestQueryPatient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from abdm_gateway.models.patient_identification_request_query_patient import PatientIdentificationRequestQueryPatient

# TODO update the JSON string below
json = "{}"
# create an instance of PatientIdentificationRequestQueryPatient from a JSON string
patient_identification_request_query_patient_instance = PatientIdentificationRequestQueryPatient.from_json(json)
# print the JSON string representation of the object
print(PatientIdentificationRequestQueryPatient.to_json())

# convert the object into a dict
patient_identification_request_query_patient_dict = patient_identification_request_query_patient_instance.to_dict()
# create an instance of PatientIdentificationRequestQueryPatient from a dict
patient_identification_request_query_patient_from_dict = PatientIdentificationRequestQueryPatient.from_dict(patient_identification_request_query_patient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


