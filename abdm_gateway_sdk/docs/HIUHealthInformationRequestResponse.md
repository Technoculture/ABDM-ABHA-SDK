# HIUHealthInformationRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** |  | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**hi_request** | [**HIUHealthInformationRequestResponseHiRequest**](HIUHealthInformationRequestResponseHiRequest.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**resp** | [**RequestReference**](RequestReference.md) |  | 

## Example

```python
from abdm_gateway.models.hiu_health_information_request_response import HIUHealthInformationRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HIUHealthInformationRequestResponse from a JSON string
hiu_health_information_request_response_instance = HIUHealthInformationRequestResponse.from_json(json)
# print the JSON string representation of the object
print(HIUHealthInformationRequestResponse.to_json())

# convert the object into a dict
hiu_health_information_request_response_dict = hiu_health_information_request_response_instance.to_dict()
# create an instance of HIUHealthInformationRequestResponse from a dict
hiu_health_information_request_response_from_dict = HIUHealthInformationRequestResponse.from_dict(hiu_health_information_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


