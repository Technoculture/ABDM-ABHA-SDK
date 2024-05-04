# PermissionFrequency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** |  | [optional] 
**value** | **int** |  | [optional] 
**repeats** | **int** |  | [optional] 

## Example

```python
from abdm_gateway.models.permission_frequency import PermissionFrequency

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionFrequency from a JSON string
permission_frequency_instance = PermissionFrequency.from_json(json)
# print the JSON string representation of the object
print(PermissionFrequency.to_json())

# convert the object into a dict
permission_frequency_dict = permission_frequency_instance.to_dict()
# create an instance of PermissionFrequency from a dict
permission_frequency_from_dict = PermissionFrequency.from_dict(permission_frequency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


