# HealthFacilityAuthenticationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hfr_uid** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from abha.models.health_facility_authentication_request import HealthFacilityAuthenticationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HealthFacilityAuthenticationRequest from a JSON string
health_facility_authentication_request_instance = HealthFacilityAuthenticationRequest.from_json(json)
# print the JSON string representation of the object
print(HealthFacilityAuthenticationRequest.to_json())

# convert the object into a dict
health_facility_authentication_request_dict = health_facility_authentication_request_instance.to_dict()
# create an instance of HealthFacilityAuthenticationRequest from a dict
health_facility_authentication_request_from_dict = HealthFacilityAuthenticationRequest.from_dict(health_facility_authentication_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


