# HealthFacilityChangedPasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hfr_uid** | **str** |  | [optional] 
**new_password** | **str** |  | [optional] 
**old_password** | **str** |  | [optional] 

## Example

```python
from abha.models.health_facility_changed_password_request import HealthFacilityChangedPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HealthFacilityChangedPasswordRequest from a JSON string
health_facility_changed_password_request_instance = HealthFacilityChangedPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(HealthFacilityChangedPasswordRequest.to_json())

# convert the object into a dict
health_facility_changed_password_request_dict = health_facility_changed_password_request_instance.to_dict()
# create an instance of HealthFacilityChangedPasswordRequest from a dict
health_facility_changed_password_request_from_dict = HealthFacilityChangedPasswordRequest.from_dict(health_facility_changed_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


