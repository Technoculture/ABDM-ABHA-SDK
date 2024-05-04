# PermissionDateRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** |  | [optional] 
**to** | **datetime** |  | [optional] 

## Example

```python
from abdm_gateway.models.permission_date_range import PermissionDateRange

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionDateRange from a JSON string
permission_date_range_instance = PermissionDateRange.from_json(json)
# print the JSON string representation of the object
print(PermissionDateRange.to_json())

# convert the object into a dict
permission_date_range_dict = permission_date_range_instance.to_dict()
# create an instance of PermissionDateRange from a dict
permission_date_range_from_dict = PermissionDateRange.from_dict(permission_date_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


