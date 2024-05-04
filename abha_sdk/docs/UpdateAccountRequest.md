# UpdateAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**day_of_birth** | **str** |  | [optional] 
**district_code** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**health_id** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**month_of_birth** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**pincode** | **int** |  | [optional] 
**profile_photo** | **str** | Encoded with Base 64 | [optional] 
**state_code** | **str** |  | [optional] 
**subdistrict_code** | **str** |  | [optional] 
**town_code** | **str** |  | [optional] 
**village_code** | **str** |  | [optional] 
**ward_code** | **str** |  | [optional] 
**year_of_birth** | **str** |  | [optional] 

## Example

```python
from abha.models.update_account_request import UpdateAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAccountRequest from a JSON string
update_account_request_instance = UpdateAccountRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAccountRequest.to_json())

# convert the object into a dict
update_account_request_dict = update_account_request_instance.to_dict()
# create an instance of UpdateAccountRequest from a dict
update_account_request_from_dict = UpdateAccountRequest.from_dict(update_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


