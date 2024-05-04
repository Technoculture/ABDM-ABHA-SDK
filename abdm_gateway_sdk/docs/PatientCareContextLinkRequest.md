# PatientCareContextLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**link** | [**PatientCareContextLink**](PatientCareContextLink.md) |  | 

## Example

```python
from abdm_gateway.models.patient_care_context_link_request import PatientCareContextLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatientCareContextLinkRequest from a JSON string
patient_care_context_link_request_instance = PatientCareContextLinkRequest.from_json(json)
# print the JSON string representation of the object
print(PatientCareContextLinkRequest.to_json())

# convert the object into a dict
patient_care_context_link_request_dict = patient_care_context_link_request_instance.to_dict()
# create an instance of PatientCareContextLinkRequest from a dict
patient_care_context_link_request_from_dict = PatientCareContextLinkRequest.from_dict(patient_care_context_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


