# DistrictDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from abha.models.district_dto import DistrictDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictDTO from a JSON string
district_dto_instance = DistrictDTO.from_json(json)
# print the JSON string representation of the object
print(DistrictDTO.to_json())

# convert the object into a dict
district_dto_dict = district_dto_instance.to_dict()
# create an instance of DistrictDTO from a dict
district_dto_from_dict = DistrictDTO.from_dict(district_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


