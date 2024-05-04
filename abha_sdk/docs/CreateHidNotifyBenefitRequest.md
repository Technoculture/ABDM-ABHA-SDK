# CreateHidNotifyBenefitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aadhar_number_or_uid_token** | **str** | JWT Bearer Token | 
**auto_generated_benefit_id** | **bool** |  | [optional] 
**benefit_id** | **str** |  | [optional] 
**benefit_name** | **str** |  | 
**consent_health_id** | **bool** |  | [optional] 
**date_of_birth** | **str** |  | 
**gender** | **str** |  | 
**mobile_number** | **str** |  | [optional] 
**name** | **str** |  | 
**state_code** | **str** |  | 
**validity** | **str** |  | [optional] 

## Example

```python
from abha.models.create_hid_notify_benefit_request import CreateHidNotifyBenefitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHidNotifyBenefitRequest from a JSON string
create_hid_notify_benefit_request_instance = CreateHidNotifyBenefitRequest.from_json(json)
# print the JSON string representation of the object
print(CreateHidNotifyBenefitRequest.to_json())

# convert the object into a dict
create_hid_notify_benefit_request_dict = create_hid_notify_benefit_request_instance.to_dict()
# create an instance of CreateHidNotifyBenefitRequest from a dict
create_hid_notify_benefit_request_from_dict = CreateHidNotifyBenefitRequest.from_dict(create_hid_notify_benefit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


