# BenefitDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benefit_id** | **str** |  | [optional] 
**benefit_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**linkage_date** | **datetime** |  | [optional] 
**program_name** | **str** |  | [optional] 
**validity** | **date** |  | [optional] 

## Example

```python
from abha.models.benefit_dto import BenefitDTO

# TODO update the JSON string below
json = "{}"
# create an instance of BenefitDTO from a JSON string
benefit_dto_instance = BenefitDTO.from_json(json)
# print the JSON string representation of the object
print(BenefitDTO.to_json())

# convert the object into a dict
benefit_dto_dict = benefit_dto_instance.to_dict()
# create an instance of BenefitDTO from a dict
benefit_dto_from_dict = BenefitDTO.from_dict(benefit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


