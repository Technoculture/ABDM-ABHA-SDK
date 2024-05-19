# HealthFacilityRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hfr_uid** | **str** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from abha.models.health_facility_role_request import HealthFacilityRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HealthFacilityRoleRequest from a JSON string
health_facility_role_request_instance = HealthFacilityRoleRequest.from_json(json)
# print the JSON string representation of the object
print(HealthFacilityRoleRequest.to_json())

# convert the object into a dict
health_facility_role_request_dict = health_facility_role_request_instance.to_dict()
# create an instance of HealthFacilityRoleRequest from a dict
health_facility_role_request_from_dict = HealthFacilityRoleRequest.from_dict(health_facility_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


