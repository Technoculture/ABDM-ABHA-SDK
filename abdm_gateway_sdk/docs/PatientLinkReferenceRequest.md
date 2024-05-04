# PatientLinkReferenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** |  | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**transaction_id** | **str** |  | 
**patient** | [**PatientLinkReferenceRequestPatient**](PatientLinkReferenceRequestPatient.md) |  | 

## Example

```python
from abdm_gateway.models.patient_link_reference_request import PatientLinkReferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatientLinkReferenceRequest from a JSON string
patient_link_reference_request_instance = PatientLinkReferenceRequest.from_json(json)
# print the JSON string representation of the object
print(PatientLinkReferenceRequest.to_json())

# convert the object into a dict
patient_link_reference_request_dict = patient_link_reference_request_instance.to_dict()
# create an instance of PatientLinkReferenceRequest from a dict
patient_link_reference_request_from_dict = PatientLinkReferenceRequest.from_dict(patient_link_reference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


