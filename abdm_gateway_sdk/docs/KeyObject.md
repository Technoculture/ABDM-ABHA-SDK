# KeyObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **datetime** |  | 
**parameters** | **str** |  | 
**key_value** | **str** |  | 

## Example

```python
from abdm_gateway.models.key_object import KeyObject

# TODO update the JSON string below
json = "{}"
# create an instance of KeyObject from a JSON string
key_object_instance = KeyObject.from_json(json)
# print the JSON string representation of the object
print(KeyObject.to_json())

# convert the object into a dict
key_object_dict = key_object_instance.to_dict()
# create an instance of KeyObject from a dict
key_object_from_dict = KeyObject.from_dict(key_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


