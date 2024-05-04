# PatientDemographicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | PHR Identifier of patient at consent manager | 
**name** | **str** |  | 
**gender** | [**PatientGender**](PatientGender.md) |  | 
**year_of_birth** | **int** |  | 
**address** | [**PatientAddress**](PatientAddress.md) |  | [optional] 
**identifiers** | [**List[Identifier]**](Identifier.md) |  | [optional] 

## Example

```python
from abdm_gateway.models.patient_demographic_response import PatientDemographicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatientDemographicResponse from a JSON string
patient_demographic_response_instance = PatientDemographicResponse.from_json(json)
# print the JSON string representation of the object
print(PatientDemographicResponse.to_json())

# convert the object into a dict
patient_demographic_response_dict = patient_demographic_response_instance.to_dict()
# create an instance of PatientDemographicResponse from a dict
patient_demographic_response_from_dict = PatientDemographicResponse.from_dict(patient_demographic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


