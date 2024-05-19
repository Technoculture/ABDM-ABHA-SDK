# JwtRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_id_number** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from abha.models.jwt_request import JwtRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JwtRequest from a JSON string
jwt_request_instance = JwtRequest.from_json(json)
# print the JSON string representation of the object
print(JwtRequest.to_json())

# convert the object into a dict
jwt_request_dict = jwt_request_instance.to_dict()
# create an instance of JwtRequest from a dict
jwt_request_from_dict = JwtRequest.from_dict(jwt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


