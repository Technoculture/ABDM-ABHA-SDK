# CreateHealthIdWithPreVerified200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_methods** | **List[str]** | Based on authMethods | [optional] 
**day_of_birth** | **str** |  | [optional] 
**district_code** | **str** |  | [optional] 
**district_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**health_id** | **str** |  | [optional] 
**health_id_number** | **str** |  | [optional] 
**kyc_photo** | **str** | Encoded with Base 64 | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**mobile** | **str** |  | [optional] 
**month_of_birth** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 
**profile_photo** | **str** | Encoded with Base 64 | [optional] 
**refresh_token** | **str** | JWT Bearer Token | [optional] 
**state_code** | **str** |  | [optional] 
**state_name** | **str** |  | [optional] 
**tags** | **Dict[str, str]** |  | [optional] 
**token** | **str** | JWT Bearer Token | [optional] 
**year_of_birth** | **str** |  | [optional] 

## Example

```python
from abha.models.create_health_id_with_pre_verified200_response import CreateHealthIdWithPreVerified200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHealthIdWithPreVerified200Response from a JSON string
create_health_id_with_pre_verified200_response_instance = CreateHealthIdWithPreVerified200Response.from_json(json)
# print the JSON string representation of the object
print(CreateHealthIdWithPreVerified200Response.to_json())

# convert the object into a dict
create_health_id_with_pre_verified200_response_dict = create_health_id_with_pre_verified200_response_instance.to_dict()
# create an instance of CreateHealthIdWithPreVerified200Response from a dict
create_health_id_with_pre_verified200_response_from_dict = CreateHealthIdWithPreVerified200Response.from_dict(create_health_id_with_pre_verified200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


