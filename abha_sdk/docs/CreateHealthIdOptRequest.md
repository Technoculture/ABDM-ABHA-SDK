# CreateHealthIdOptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_generated_benefit_id** | **bool** |  | [optional] 
**benefit_id** | **str** |  | [optional] 
**benefit_name** | **str** |  | 
**consent_health_id** | **bool** |  | [optional] 
**mobile_number** | **str** |  | [optional] 
**otp** | **str** |  | 
**txn_id** | **str** | Based on UUID | 
**validity** | **str** |  | [optional] 

## Example

```python
from abha.models.create_health_id_opt_request import CreateHealthIdOptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHealthIdOptRequest from a JSON string
create_health_id_opt_request_instance = CreateHealthIdOptRequest.from_json(json)
# print the JSON string representation of the object
print(CreateHealthIdOptRequest.to_json())

# convert the object into a dict
create_health_id_opt_request_dict = create_health_id_opt_request_instance.to_dict()
# create an instance of CreateHealthIdOptRequest from a dict
create_health_id_opt_request_from_dict = CreateHealthIdOptRequest.from_dict(create_health_id_opt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


