# ConsentRequestStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**consent_request_id** | **str** |  | 

## Example

```python
from abdm_gateway.models.consent_request_status_request import ConsentRequestStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentRequestStatusRequest from a JSON string
consent_request_status_request_instance = ConsentRequestStatusRequest.from_json(json)
# print the JSON string representation of the object
print(ConsentRequestStatusRequest.to_json())

# convert the object into a dict
consent_request_status_request_dict = consent_request_status_request_instance.to_dict()
# create an instance of ConsentRequestStatusRequest from a dict
consent_request_status_request_from_dict = ConsentRequestStatusRequest.from_dict(consent_request_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


