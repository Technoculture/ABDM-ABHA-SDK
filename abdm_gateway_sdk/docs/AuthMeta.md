# AuthMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hint** | **str** |  | [optional] 
**expiry** | **str** |  | [optional] 

## Example

```python
from abdm_gateway.models.auth_meta import AuthMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMeta from a JSON string
auth_meta_instance = AuthMeta.from_json(json)
# print the JSON string representation of the object
print(AuthMeta.to_json())

# convert the object into a dict
auth_meta_dict = auth_meta_instance.to_dict()
# create an instance of AuthMeta from a dict
auth_meta_from_dict = AuthMeta.from_dict(auth_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


