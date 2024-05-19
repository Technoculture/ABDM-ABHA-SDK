# HidBenefitSearchResponsePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benefit_id** | **str** |  | [optional] 
**benefit_name** | **str** |  | [optional] 
**health_id_number** | **str** |  | [optional] 
**state_code** | **str** |  | [optional] 

## Example

```python
from abha.models.hid_benefit_search_response_payload import HidBenefitSearchResponsePayload

# TODO update the JSON string below
json = "{}"
# create an instance of HidBenefitSearchResponsePayload from a JSON string
hid_benefit_search_response_payload_instance = HidBenefitSearchResponsePayload.from_json(json)
# print the JSON string representation of the object
print(HidBenefitSearchResponsePayload.to_json())

# convert the object into a dict
hid_benefit_search_response_payload_dict = hid_benefit_search_response_payload_instance.to_dict()
# create an instance of HidBenefitSearchResponsePayload from a dict
hid_benefit_search_response_payload_from_dict = HidBenefitSearchResponsePayload.from_dict(hid_benefit_search_response_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


