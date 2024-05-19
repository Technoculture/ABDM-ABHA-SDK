# UserDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**auth_methods** | **List[str]** | Based on authMethods | [optional] 
**day_of_birth** | **str** |  | [optional] 
**district_code** | **str** |  | [optional] 
**district_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**email_verified** | **bool** |  | [optional] 
**first_name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**health_id** | **str** |  | [optional] 
**health_id_number** | **str** |  | [optional] 
**kyc_photo** | **str** | Encoded with Base 64 | [optional] 
**kyc_verified** | **bool** |  | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**mobile** | **str** |  | [optional] 
**month_of_birth** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 
**phr_address** | **List[str]** |  | [optional] 
**pincode** | **str** |  | [optional] 
**profile_photo** | **str** | Encoded with Base 64 | [optional] 
**state_code** | **str** |  | [optional] 
**state_name** | **str** |  | [optional] 
**sub_district_code** | **str** |  | [optional] 
**subdistrict_name** | **str** |  | [optional] 
**tags** | **Dict[str, str]** |  | [optional] 
**town_code** | **str** |  | [optional] 
**town_name** | **str** |  | [optional] 
**verification_status** | **str** |  | [optional] 
**verification_type** | **str** |  | [optional] 
**village_code** | **str** |  | [optional] 
**village_name** | **str** |  | [optional] 
**ward_code** | **str** |  | [optional] 
**ward_name** | **str** |  | [optional] 
**year_of_birth** | **str** |  | [optional] 

## Example

```python
from abha.models.user_dto import UserDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserDTO from a JSON string
user_dto_instance = UserDTO.from_json(json)
# print the JSON string representation of the object
print(UserDTO.to_json())

# convert the object into a dict
user_dto_dict = user_dto_instance.to_dict()
# create an instance of UserDTO from a dict
user_dto_from_dict = UserDTO.from_dict(user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


