# CareContextDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patient_reference** | **str** | A patient identifier with which patient is registered in the facility/hospital | 
**care_context_reference** | **str** | An identifier of patient&#39;s care context created in HIP. A care context is a group of patient&#39;s health data (Not the actual health data) | 

## Example

```python
from abdm_gateway.models.care_context_definition import CareContextDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of CareContextDefinition from a JSON string
care_context_definition_instance = CareContextDefinition.from_json(json)
# print the JSON string representation of the object
print(CareContextDefinition.to_json())

# convert the object into a dict
care_context_definition_dict = care_context_definition_instance.to_dict()
# create an instance of CareContextDefinition from a dict
care_context_definition_from_dict = CareContextDefinition.from_dict(care_context_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


