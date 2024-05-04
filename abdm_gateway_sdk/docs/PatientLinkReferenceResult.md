# PatientLinkReferenceResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**transaction_id** | **str** |  | 
**link** | [**PatientLinkReferenceResultLink**](PatientLinkReferenceResultLink.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**resp** | [**RequestReference**](RequestReference.md) |  | 

## Example

```python
from abdm_gateway.models.patient_link_reference_result import PatientLinkReferenceResult

# TODO update the JSON string below
json = "{}"
# create an instance of PatientLinkReferenceResult from a JSON string
patient_link_reference_result_instance = PatientLinkReferenceResult.from_json(json)
# print the JSON string representation of the object
print(PatientLinkReferenceResult.to_json())

# convert the object into a dict
patient_link_reference_result_dict = patient_link_reference_result_instance.to_dict()
# create an instance of PatientLinkReferenceResult from a dict
patient_link_reference_result_from_dict = PatientLinkReferenceResult.from_dict(patient_link_reference_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


