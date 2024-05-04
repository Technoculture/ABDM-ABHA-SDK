# ServiceProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**ServiceRole**](ServiceRole.md) |  | [optional] 
**endpoints** | [**List[Endpoint]**](Endpoint.md) |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from abdm_gateway.models.service_profile_response import ServiceProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileResponse from a JSON string
service_profile_response_instance = ServiceProfileResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileResponse.to_json())

# convert the object into a dict
service_profile_response_dict = service_profile_response_instance.to_dict()
# create an instance of ServiceProfileResponse from a dict
service_profile_response_from_dict = ServiceProfileResponse.from_dict(service_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


