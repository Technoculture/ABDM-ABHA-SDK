# ConsentRequestInitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**consent_request** | [**ConsentRequestInitResponseConsentRequest**](ConsentRequestInitResponseConsentRequest.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**resp** | [**RequestReference**](RequestReference.md) |  | 

## Example

```python
from abdm_gateway.models.consent_request_init_response import ConsentRequestInitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentRequestInitResponse from a JSON string
consent_request_init_response_instance = ConsentRequestInitResponse.from_json(json)
# print the JSON string representation of the object
print(ConsentRequestInitResponse.to_json())

# convert the object into a dict
consent_request_init_response_dict = consent_request_init_response_instance.to_dict()
# create an instance of ConsentRequestInitResponse from a dict
consent_request_init_response_from_dict = ConsentRequestInitResponse.from_dict(consent_request_init_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


