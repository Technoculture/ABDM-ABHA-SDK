# RetriveHealthIdMobilePayLoad


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_birth** | **str** |  | [optional] 
**first_name** | **str** |  | 
**gender** | **str** |  | 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**month_of_birth** | **str** |  | [optional] 
**name** | **str** |  | 
**otp** | **str** |  | 
**status** | **str** |  | [optional] 
**txn_id** | **str** | Based on UUID | 
**year_of_birth** | **str** |  | 

## Example

```python
from abha.models.retrive_health_id_mobile_pay_load import RetriveHealthIdMobilePayLoad

# TODO update the JSON string below
json = "{}"
# create an instance of RetriveHealthIdMobilePayLoad from a JSON string
retrive_health_id_mobile_pay_load_instance = RetriveHealthIdMobilePayLoad.from_json(json)
# print the JSON string representation of the object
print(RetriveHealthIdMobilePayLoad.to_json())

# convert the object into a dict
retrive_health_id_mobile_pay_load_dict = retrive_health_id_mobile_pay_load_instance.to_dict()
# create an instance of RetriveHealthIdMobilePayLoad from a dict
retrive_health_id_mobile_pay_load_from_dict = RetriveHealthIdMobilePayLoad.from_dict(retrive_health_id_mobile_pay_load_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


