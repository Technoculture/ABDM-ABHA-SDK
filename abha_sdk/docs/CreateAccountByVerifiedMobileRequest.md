# CreateAccountByVerifiedMobileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**day_of_birth** | **str** |  | [optional] 
**district_code** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**gender** | **str** |  | 
**health_id** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**month_of_birth** | **str** |  | [optional] 
**name** | **str** |  | 
**password** | **str** |  | [optional] 
**pincode** | **int** |  | [optional] 
**profile_photo** | **str** | Encoded with Base 64 | [optional] 
**state_code** | **str** |  | [optional] 
**subdistrict_code** | **str** |  | [optional] 
**token** | **str** | JWT Bearer Token | 
**town_code** | **str** |  | [optional] 
**txn_id** | **str** | Based on UUID | 
**village_code** | **str** |  | [optional] 
**ward_code** | **str** |  | [optional] 
**year_of_birth** | **str** |  | 

## Example

```python
from abha.models.create_account_by_verified_mobile_request import CreateAccountByVerifiedMobileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccountByVerifiedMobileRequest from a JSON string
create_account_by_verified_mobile_request_instance = CreateAccountByVerifiedMobileRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAccountByVerifiedMobileRequest.to_json())

# convert the object into a dict
create_account_by_verified_mobile_request_dict = create_account_by_verified_mobile_request_instance.to_dict()
# create an instance of CreateAccountByVerifiedMobileRequest from a dict
create_account_by_verified_mobile_request_from_dict = CreateAccountByVerifiedMobileRequest.from_dict(create_account_by_verified_mobile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


