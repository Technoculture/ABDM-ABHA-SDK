# PatientCareContextLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | AccessToken fetched in the user auth process for the purpose specified | 
**patient** | [**PatientCareContextLinkPatient**](PatientCareContextLinkPatient.md) |  | 

## Example

```python
from abdm_gateway.models.patient_care_context_link import PatientCareContextLink

# TODO update the JSON string below
json = "{}"
# create an instance of PatientCareContextLink from a JSON string
patient_care_context_link_instance = PatientCareContextLink.from_json(json)
# print the JSON string representation of the object
print(PatientCareContextLink.to_json())

# convert the object into a dict
patient_care_context_link_dict = patient_care_context_link_instance.to_dict()
# create an instance of PatientCareContextLink from a dict
patient_care_context_link_from_dict = PatientCareContextLink.from_dict(patient_care_context_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


