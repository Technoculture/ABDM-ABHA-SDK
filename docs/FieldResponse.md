# FieldResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**matched** | **bool** |  | [optional] 

## Example

```python
from abha.models.field_response import FieldResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FieldResponse from a JSON string
field_response_instance = FieldResponse.from_json(json)
# print the JSON string representation of the object
print(FieldResponse.to_json())

# convert the object into a dict
field_response_dict = field_response_instance.to_dict()
# create an instance of FieldResponse from a dict
field_response_from_dict = FieldResponse.from_dict(field_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


