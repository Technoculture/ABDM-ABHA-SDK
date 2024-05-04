# HIPHIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** |  | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**transaction_id** | **str** |  | 
**hi_request** | [**HIRequestHiRequest**](HIRequestHiRequest.md) |  | 

## Example

```python
from abdm_gateway.models.hiphi_request import HIPHIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HIPHIRequest from a JSON string
hiphi_request_instance = HIPHIRequest.from_json(json)
# print the JSON string representation of the object
print(HIPHIRequest.to_json())

# convert the object into a dict
hiphi_request_dict = hiphi_request_instance.to_dict()
# create an instance of HIPHIRequest from a dict
hiphi_request_from_dict = HIPHIRequest.from_dict(hiphi_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


