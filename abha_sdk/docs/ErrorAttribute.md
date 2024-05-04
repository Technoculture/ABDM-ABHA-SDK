# ErrorAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from abha.models.error_attribute import ErrorAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorAttribute from a JSON string
error_attribute_instance = ErrorAttribute.from_json(json)
# print the JSON string representation of the object
print(ErrorAttribute.to_json())

# convert the object into a dict
error_attribute_dict = error_attribute_instance.to_dict()
# create an instance of ErrorAttribute from a dict
error_attribute_from_dict = ErrorAttribute.from_dict(error_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


