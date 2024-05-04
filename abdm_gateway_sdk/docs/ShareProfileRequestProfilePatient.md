# ShareProfileRequestProfilePatient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_id** | **str** |  | 
**health_id_number** | **str** |  | 
**name** | **str** |  | 
**gender** | [**PatientGender**](PatientGender.md) |  | 
**address** | [**PatientAddress**](PatientAddress.md) |  | [optional] 
**year_of_birth** | **int** |  | 
**day_of_birth** | **int** |  | [optional] 
**month_of_birth** | **int** |  | [optional] 
**identifiers** | [**List[Identifier]**](Identifier.md) |  | [optional] 

## Example

```python
from abdm_gateway.models.share_profile_request_profile_patient import ShareProfileRequestProfilePatient

# TODO update the JSON string below
json = "{}"
# create an instance of ShareProfileRequestProfilePatient from a JSON string
share_profile_request_profile_patient_instance = ShareProfileRequestProfilePatient.from_json(json)
# print the JSON string representation of the object
print(ShareProfileRequestProfilePatient.to_json())

# convert the object into a dict
share_profile_request_profile_patient_dict = share_profile_request_profile_patient_instance.to_dict()
# create an instance of ShareProfileRequestProfilePatient from a dict
share_profile_request_profile_patient_from_dict = ShareProfileRequestProfilePatient.from_dict(share_profile_request_profile_patient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


