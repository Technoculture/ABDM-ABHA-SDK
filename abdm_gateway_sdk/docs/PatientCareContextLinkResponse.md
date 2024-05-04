# PatientCareContextLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**acknowledgement** | [**PatientCareContextLinkResponseAcknowledgement**](PatientCareContextLinkResponseAcknowledgement.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**resp** | [**RequestReference**](RequestReference.md) |  | 

## Example

```python
from abdm_gateway.models.patient_care_context_link_response import PatientCareContextLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatientCareContextLinkResponse from a JSON string
patient_care_context_link_response_instance = PatientCareContextLinkResponse.from_json(json)
# print the JSON string representation of the object
print(PatientCareContextLinkResponse.to_json())

# convert the object into a dict
patient_care_context_link_response_dict = patient_care_context_link_response_instance.to_dict()
# create an instance of PatientCareContextLinkResponse from a dict
patient_care_context_link_response_from_dict = PatientCareContextLinkResponse.from_dict(patient_care_context_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


