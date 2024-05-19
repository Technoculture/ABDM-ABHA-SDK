# AuthAccountAadhaarOTPRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp** | **str** |  | 
**txn_id** | **str** | Based on UUID | 

## Example

```python
from abha.models.auth_account_aadhaar_otp_request import AuthAccountAadhaarOTPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthAccountAadhaarOTPRequest from a JSON string
auth_account_aadhaar_otp_request_instance = AuthAccountAadhaarOTPRequest.from_json(json)
# print the JSON string representation of the object
print(AuthAccountAadhaarOTPRequest.to_json())

# convert the object into a dict
auth_account_aadhaar_otp_request_dict = auth_account_aadhaar_otp_request_instance.to_dict()
# create an instance of AuthAccountAadhaarOTPRequest from a dict
auth_account_aadhaar_otp_request_from_dict = AuthAccountAadhaarOTPRequest.from_dict(auth_account_aadhaar_otp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


