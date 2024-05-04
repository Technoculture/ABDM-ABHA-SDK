# HIUHealthInformationRequestResponseHiRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 
**session_status** | **str** |  | 

## Example

```python
from abdm_gateway.models.hiu_health_information_request_response_hi_request import HIUHealthInformationRequestResponseHiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HIUHealthInformationRequestResponseHiRequest from a JSON string
hiu_health_information_request_response_hi_request_instance = HIUHealthInformationRequestResponseHiRequest.from_json(json)
# print the JSON string representation of the object
print(HIUHealthInformationRequestResponseHiRequest.to_json())

# convert the object into a dict
hiu_health_information_request_response_hi_request_dict = hiu_health_information_request_response_hi_request_instance.to_dict()
# create an instance of HIUHealthInformationRequestResponseHiRequest from a dict
hiu_health_information_request_response_hi_request_from_dict = HIUHealthInformationRequestResponseHiRequest.from_dict(hiu_health_information_request_response_hi_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


