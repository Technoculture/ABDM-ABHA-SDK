# PatientIdentificationRequestQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patient** | [**PatientIdentificationRequestQueryPatient**](PatientIdentificationRequestQueryPatient.md) |  | 
**requester** | [**PatientIdentificationRequestQueryRequester**](PatientIdentificationRequestQueryRequester.md) |  | 

## Example

```python
from abdm_gateway.models.patient_identification_request_query import PatientIdentificationRequestQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PatientIdentificationRequestQuery from a JSON string
patient_identification_request_query_instance = PatientIdentificationRequestQuery.from_json(json)
# print the JSON string representation of the object
print(PatientIdentificationRequestQuery.to_json())

# convert the object into a dict
patient_identification_request_query_dict = patient_identification_request_query_instance.to_dict()
# create an instance of PatientIdentificationRequestQuery from a dict
patient_identification_request_query_from_dict = PatientIdentificationRequestQuery.from_dict(patient_identification_request_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


