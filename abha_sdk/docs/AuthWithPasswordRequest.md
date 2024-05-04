# AuthWithPasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**txn_id** | **str** |  | [optional] 

## Example

```python
from abha.models.auth_with_password_request import AuthWithPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthWithPasswordRequest from a JSON string
auth_with_password_request_instance = AuthWithPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(AuthWithPasswordRequest.to_json())

# convert the object into a dict
auth_with_password_request_dict = auth_with_password_request_instance.to_dict()
# create an instance of AuthWithPasswordRequest from a dict
auth_with_password_request_from_dict = AuthWithPasswordRequest.from_dict(auth_with_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


