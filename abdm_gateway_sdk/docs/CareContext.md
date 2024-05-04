# CareContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_number** | **str** |  | 

## Example

```python
from abdm_gateway.models.care_context import CareContext

# TODO update the JSON string below
json = "{}"
# create an instance of CareContext from a JSON string
care_context_instance = CareContext.from_json(json)
# print the JSON string representation of the object
print(CareContext.to_json())

# convert the object into a dict
care_context_dict = care_context_instance.to_dict()
# create an instance of CareContext from a dict
care_context_from_dict = CareContext.from_dict(care_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


