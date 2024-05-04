# AuthInitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method** | **str** |  | [optional] 
**healthid** | **str** |  | [optional] 

## Example

```python
from abha.models.auth_init_request import AuthInitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthInitRequest from a JSON string
auth_init_request_instance = AuthInitRequest.from_json(json)
# print the JSON string representation of the object
print(AuthInitRequest.to_json())

# convert the object into a dict
auth_init_request_dict = auth_init_request_instance.to_dict()
# create an instance of AuthInitRequest from a dict
auth_init_request_from_dict = AuthInitRequest.from_dict(auth_init_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


