# CreateAccountWithAadhaarOtp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**mobile** | **str** |  | [optional] 
**otp** | **str** |  | 
**password** | **str** |  | [optional] 
**profile_photo** | **str** | Encoded with Base 64 | [optional] 
**txn_id** | **str** | Based on UUID | 
**username** | **str** |  | [optional] 

## Example

```python
from abha.models.create_account_with_aadhaar_otp import CreateAccountWithAadhaarOtp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccountWithAadhaarOtp from a JSON string
create_account_with_aadhaar_otp_instance = CreateAccountWithAadhaarOtp.from_json(json)
# print the JSON string representation of the object
print(CreateAccountWithAadhaarOtp.to_json())

# convert the object into a dict
create_account_with_aadhaar_otp_dict = create_account_with_aadhaar_otp_instance.to_dict()
# create an instance of CreateAccountWithAadhaarOtp from a dict
create_account_with_aadhaar_otp_from_dict = CreateAccountWithAadhaarOtp.from_dict(create_account_with_aadhaar_otp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


