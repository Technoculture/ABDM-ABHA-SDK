# HidBenefitLinkedRequestPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benefit_id** | **str** |  | 
**benefit_name** | **str** |  | 
**state_code** | **str** |  | [optional] 
**uid_token** | **str** | JWT Bearer Token | 
**validity** | **str** |  | [optional] 

## Example

```python
from abha.models.hid_benefit_linked_request_payload import HidBenefitLinkedRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of HidBenefitLinkedRequestPayload from a JSON string
hid_benefit_linked_request_payload_instance = HidBenefitLinkedRequestPayload.from_json(json)
# print the JSON string representation of the object
print(HidBenefitLinkedRequestPayload.to_json())

# convert the object into a dict
hid_benefit_linked_request_payload_dict = hid_benefit_linked_request_payload_instance.to_dict()
# create an instance of HidBenefitLinkedRequestPayload from a dict
hid_benefit_linked_request_payload_from_dict = HidBenefitLinkedRequestPayload.from_dict(hid_benefit_linked_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


