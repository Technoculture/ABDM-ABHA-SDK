# HidBenefitLinkedResponsePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benefit_name** | **str** |  | [optional] 
**health_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from abha.models.hid_benefit_linked_response_payload import HidBenefitLinkedResponsePayload

# TODO update the JSON string below
json = "{}"
# create an instance of HidBenefitLinkedResponsePayload from a JSON string
hid_benefit_linked_response_payload_instance = HidBenefitLinkedResponsePayload.from_json(json)
# print the JSON string representation of the object
print(HidBenefitLinkedResponsePayload.to_json())

# convert the object into a dict
hid_benefit_linked_response_payload_dict = hid_benefit_linked_response_payload_instance.to_dict()
# create an instance of HidBenefitLinkedResponsePayload from a dict
hid_benefit_linked_response_payload_from_dict = HidBenefitLinkedResponsePayload.from_dict(hid_benefit_linked_response_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


