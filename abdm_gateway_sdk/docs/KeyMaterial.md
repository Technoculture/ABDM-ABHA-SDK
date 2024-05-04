# KeyMaterial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto_alg** | **str** |  | 
**curve** | **str** |  | 
**dh_public_key** | [**KeyObject**](KeyObject.md) |  | 
**nonce** | **str** |  | 

## Example

```python
from abdm_gateway.models.key_material import KeyMaterial

# TODO update the JSON string below
json = "{}"
# create an instance of KeyMaterial from a JSON string
key_material_instance = KeyMaterial.from_json(json)
# print the JSON string representation of the object
print(KeyMaterial.to_json())

# convert the object into a dict
key_material_dict = key_material_instance.to_dict()
# create an instance of KeyMaterial from a dict
key_material_from_dict = KeyMaterial.from_dict(key_material_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


