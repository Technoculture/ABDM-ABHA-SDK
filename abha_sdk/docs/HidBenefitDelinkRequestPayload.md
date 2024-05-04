# HidBenefitDelinkRequestPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benefit_name** | **str** |  | 
**uid_token** | **str** | JWT Bearer Token | 

## Example

```python
from abha.models.hid_benefit_delink_request_payload import HidBenefitDelinkRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of HidBenefitDelinkRequestPayload from a JSON string
hid_benefit_delink_request_payload_instance = HidBenefitDelinkRequestPayload.from_json(json)
# print the JSON string representation of the object
print(HidBenefitDelinkRequestPayload.to_json())

# convert the object into a dict
hid_benefit_delink_request_payload_dict = hid_benefit_delink_request_payload_instance.to_dict()
# create an instance of HidBenefitDelinkRequestPayload from a dict
hid_benefit_delink_request_payload_from_dict = HidBenefitDelinkRequestPayload.from_dict(hid_benefit_delink_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


