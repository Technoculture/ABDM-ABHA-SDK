# PatientIdentificationRequestQueryRequester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from abdm_gateway.models.patient_identification_request_query_requester import PatientIdentificationRequestQueryRequester

# TODO update the JSON string below
json = "{}"
# create an instance of PatientIdentificationRequestQueryRequester from a JSON string
patient_identification_request_query_requester_instance = PatientIdentificationRequestQueryRequester.from_json(json)
# print the JSON string representation of the object
print(PatientIdentificationRequestQueryRequester.to_json())

# convert the object into a dict
patient_identification_request_query_requester_dict = patient_identification_request_query_requester_instance.to_dict()
# create an instance of PatientIdentificationRequestQueryRequester from a dict
patient_identification_request_query_requester_from_dict = PatientIdentificationRequestQueryRequester.from_dict(patient_identification_request_query_requester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


