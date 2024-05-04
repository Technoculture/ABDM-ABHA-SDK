# CreateAccountWithPreVerifiedAadhaar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**health_id** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**profile_photo** | **str** | Encoded with Base 64 | [optional] 
**txn_id** | **str** | Based on UUID | [optional] 

## Example

```python
from abha.models.create_account_with_pre_verified_aadhaar import CreateAccountWithPreVerifiedAadhaar

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccountWithPreVerifiedAadhaar from a JSON string
create_account_with_pre_verified_aadhaar_instance = CreateAccountWithPreVerifiedAadhaar.from_json(json)
# print the JSON string representation of the object
print(CreateAccountWithPreVerifiedAadhaar.to_json())

# convert the object into a dict
create_account_with_pre_verified_aadhaar_dict = create_account_with_pre_verified_aadhaar_instance.to_dict()
# create an instance of CreateAccountWithPreVerifiedAadhaar from a dict
create_account_with_pre_verified_aadhaar_from_dict = CreateAccountWithPreVerifiedAadhaar.from_dict(create_account_with_pre_verified_aadhaar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


