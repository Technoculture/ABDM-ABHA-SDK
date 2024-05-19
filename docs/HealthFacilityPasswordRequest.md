# HealthFacilityPasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hfr_uid** | **str** |  | [optional] 

## Example

```python
from abha.models.health_facility_password_request import HealthFacilityPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HealthFacilityPasswordRequest from a JSON string
health_facility_password_request_instance = HealthFacilityPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(HealthFacilityPasswordRequest.to_json())

# convert the object into a dict
health_facility_password_request_dict = health_facility_password_request_instance.to_dict()
# create an instance of HealthFacilityPasswordRequest from a dict
health_facility_password_request_from_dict = HealthFacilityPasswordRequest.from_dict(health_facility_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


