# HIPHealthInformationRequestAcknowledgement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**hi_request** | [**HIPHealthInformationRequestAcknowledgementHiRequest**](HIPHealthInformationRequestAcknowledgementHiRequest.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**resp** | [**RequestReference**](RequestReference.md) |  | 

## Example

```python
from abdm_gateway.models.hip_health_information_request_acknowledgement import HIPHealthInformationRequestAcknowledgement

# TODO update the JSON string below
json = "{}"
# create an instance of HIPHealthInformationRequestAcknowledgement from a JSON string
hip_health_information_request_acknowledgement_instance = HIPHealthInformationRequestAcknowledgement.from_json(json)
# print the JSON string representation of the object
print(HIPHealthInformationRequestAcknowledgement.to_json())

# convert the object into a dict
hip_health_information_request_acknowledgement_dict = hip_health_information_request_acknowledgement_instance.to_dict()
# create an instance of HIPHealthInformationRequestAcknowledgement from a dict
hip_health_information_request_acknowledgement_from_dict = HIPHealthInformationRequestAcknowledgement.from_dict(hip_health_information_request_acknowledgement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


