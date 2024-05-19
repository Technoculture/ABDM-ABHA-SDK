# HidUpdateAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**day_of_birth** | **str** |  | [optional] 
**district_code** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**health_id** | **str** |  | [optional] 
**health_id_number** | **str** |  | 
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
from abha.models.hid_update_account_request import HidUpdateAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HidUpdateAccountRequest from a JSON string
hid_update_account_request_instance = HidUpdateAccountRequest.from_json(json)
# print the JSON string representation of the object
print(HidUpdateAccountRequest.to_json())

# convert the object into a dict
hid_update_account_request_dict = hid_update_account_request_instance.to_dict()
# create an instance of HidUpdateAccountRequest from a dict
hid_update_account_request_from_dict = HidUpdateAccountRequest.from_dict(hid_update_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


