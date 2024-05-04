# PatientIdentificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**query** | [**PatientIdentificationRequestQuery**](PatientIdentificationRequestQuery.md) |  | 

## Example

```python
from abdm_gateway.models.patient_identification_request import PatientIdentificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatientIdentificationRequest from a JSON string
patient_identification_request_instance = PatientIdentificationRequest.from_json(json)
# print the JSON string representation of the object
print(PatientIdentificationRequest.to_json())

# convert the object into a dict
patient_identification_request_dict = patient_identification_request_instance.to_dict()
# create an instance of PatientIdentificationRequest from a dict
patient_identification_request_from_dict = PatientIdentificationRequest.from_dict(patient_identification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


