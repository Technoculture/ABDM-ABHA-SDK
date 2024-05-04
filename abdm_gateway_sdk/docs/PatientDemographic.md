# PatientDemographic

Demographic details are only required for demographic auth at this point. Demographic details must be same as registered

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**gender** | [**PatientGender**](PatientGender.md) |  | 
**date_of_birth** | **str** | date of birth in YYYY-MM-DD format. | 
**identifier** | [**AuthConfirmIdentifier**](AuthConfirmIdentifier.md) |  | [optional] 

## Example

```python
from abdm_gateway.models.patient_demographic import PatientDemographic

# TODO update the JSON string below
json = "{}"
# create an instance of PatientDemographic from a JSON string
patient_demographic_instance = PatientDemographic.from_json(json)
# print the JSON string representation of the object
print(PatientDemographic.to_json())

# convert the object into a dict
patient_demographic_dict = patient_demographic_instance.to_dict()
# create an instance of PatientDemographic from a dict
patient_demographic_from_dict = PatientDemographic.from_dict(patient_demographic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


