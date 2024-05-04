# SessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**grant_type** | **str** |  | 
**refresh_token** | **str** |  | [optional] 

## Example

```python
from abdm_gateway.models.session_request import SessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SessionRequest from a JSON string
session_request_instance = SessionRequest.from_json(json)
# print the JSON string representation of the object
print(SessionRequest.to_json())

# convert the object into a dict
session_request_dict = session_request_instance.to_dict()
# create an instance of SessionRequest from a dict
session_request_from_dict = SessionRequest.from_dict(session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


