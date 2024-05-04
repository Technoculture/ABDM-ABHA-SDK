# HealthFacilityAuthenticationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_password** | **bool** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from abha.models.health_facility_authentication_response import HealthFacilityAuthenticationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HealthFacilityAuthenticationResponse from a JSON string
health_facility_authentication_response_instance = HealthFacilityAuthenticationResponse.from_json(json)
# print the JSON string representation of the object
print(HealthFacilityAuthenticationResponse.to_json())

# convert the object into a dict
health_facility_authentication_response_dict = health_facility_authentication_response_instance.to_dict()
# create an instance of HealthFacilityAuthenticationResponse from a dict
health_facility_authentication_response_from_dict = HealthFacilityAuthenticationResponse.from_dict(health_facility_authentication_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


