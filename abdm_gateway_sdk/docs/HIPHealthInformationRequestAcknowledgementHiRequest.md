# HIPHealthInformationRequestAcknowledgementHiRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 
**session_status** | **str** |  | 

## Example

```python
from abdm_gateway.models.hip_health_information_request_acknowledgement_hi_request import HIPHealthInformationRequestAcknowledgementHiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HIPHealthInformationRequestAcknowledgementHiRequest from a JSON string
hip_health_information_request_acknowledgement_hi_request_instance = HIPHealthInformationRequestAcknowledgementHiRequest.from_json(json)
# print the JSON string representation of the object
print(HIPHealthInformationRequestAcknowledgementHiRequest.to_json())

# convert the object into a dict
hip_health_information_request_acknowledgement_hi_request_dict = hip_health_information_request_acknowledgement_hi_request_instance.to_dict()
# create an instance of HIPHealthInformationRequestAcknowledgementHiRequest from a dict
hip_health_information_request_acknowledgement_hi_request_from_dict = HIPHealthInformationRequestAcknowledgementHiRequest.from_dict(hip_health_information_request_acknowledgement_hi_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


