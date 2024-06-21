# AuthAadharInitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method** | **str** |  | 
**healthid** | **str** |  | 

## Example

```python
from abha.models.auth_aadhar_init_request import AuthAadharInitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthAadharInitRequest from a JSON string
auth_aadhar_init_request_instance = AuthAadharInitRequest.from_json(json)
# print the JSON string representation of the object
print(AuthAadharInitRequest.to_json())

# convert the object into a dict
auth_aadhar_init_request_dict = auth_aadhar_init_request_instance.to_dict()
# create an instance of AuthAadharInitRequest from a dict
auth_aadhar_init_request_from_dict = AuthAadharInitRequest.from_dict(auth_aadhar_init_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


