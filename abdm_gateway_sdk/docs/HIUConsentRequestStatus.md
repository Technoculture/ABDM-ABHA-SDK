# HIUConsentRequestStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**consent_request** | [**HIUConsentRequestStatusConsentRequest**](HIUConsentRequestStatusConsentRequest.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**resp** | [**RequestReference**](RequestReference.md) |  | 

## Example

```python
from abdm_gateway.models.hiu_consent_request_status import HIUConsentRequestStatus

# TODO update the JSON string below
json = "{}"
# create an instance of HIUConsentRequestStatus from a JSON string
hiu_consent_request_status_instance = HIUConsentRequestStatus.from_json(json)
# print the JSON string representation of the object
print(HIUConsentRequestStatus.to_json())

# convert the object into a dict
hiu_consent_request_status_dict = hiu_consent_request_status_instance.to_dict()
# create an instance of HIUConsentRequestStatus from a dict
hiu_consent_request_status_from_dict = HIUConsentRequestStatus.from_dict(hiu_consent_request_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


