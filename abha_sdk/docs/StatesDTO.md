# StatesDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**districts** | [**List[DistrictDTO]**](DistrictDTO.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from abha.models.states_dto import StatesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of StatesDTO from a JSON string
states_dto_instance = StatesDTO.from_json(json)
# print the JSON string representation of the object
print(StatesDTO.to_json())

# convert the object into a dict
states_dto_dict = states_dto_instance.to_dict()
# create an instance of StatesDTO from a dict
states_dto_from_dict = StatesDTO.from_dict(states_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


