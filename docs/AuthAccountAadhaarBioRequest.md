# AuthAccountAadhaarBioRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** |  | [optional] 
**bio_type** | **str** |  | [optional] 
**pid** | **str** |  | [optional] 
**txn_id** | **str** |  | [optional] 

## Example

```python
from abha.models.auth_account_aadhaar_bio_request import AuthAccountAadhaarBioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthAccountAadhaarBioRequest from a JSON string
auth_account_aadhaar_bio_request_instance = AuthAccountAadhaarBioRequest.from_json(json)
# print the JSON string representation of the object
print(AuthAccountAadhaarBioRequest.to_json())

# convert the object into a dict
auth_account_aadhaar_bio_request_dict = auth_account_aadhaar_bio_request_instance.to_dict()
# create an instance of AuthAccountAadhaarBioRequest from a dict
auth_account_aadhaar_bio_request_from_dict = AuthAccountAadhaarBioRequest.from_dict(auth_account_aadhaar_bio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


