# HealthFacilityShareProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Error**](Error.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from abha.models.health_facility_share_profile_response import HealthFacilityShareProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HealthFacilityShareProfileResponse from a JSON string
health_facility_share_profile_response_instance = HealthFacilityShareProfileResponse.from_json(json)
# print the JSON string representation of the object
print(HealthFacilityShareProfileResponse.to_json())

# convert the object into a dict
health_facility_share_profile_response_dict = health_facility_share_profile_response_instance.to_dict()
# create an instance of HealthFacilityShareProfileResponse from a dict
health_facility_share_profile_response_from_dict = HealthFacilityShareProfileResponse.from_dict(health_facility_share_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


