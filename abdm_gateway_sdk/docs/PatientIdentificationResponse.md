# PatientIdentificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**patient** | [**PatientIdentificationResponsePatient**](PatientIdentificationResponsePatient.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**resp** | [**RequestReference**](RequestReference.md) |  | 

## Example

```python
from abdm_gateway.models.patient_identification_response import PatientIdentificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatientIdentificationResponse from a JSON string
patient_identification_response_instance = PatientIdentificationResponse.from_json(json)
# print the JSON string representation of the object
print(PatientIdentificationResponse.to_json())

# convert the object into a dict
patient_identification_response_dict = patient_identification_response_instance.to_dict()
# create an instance of PatientIdentificationResponse from a dict
patient_identification_response_from_dict = PatientIdentificationResponse.from_dict(patient_identification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


