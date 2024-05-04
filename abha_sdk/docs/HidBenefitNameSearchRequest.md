# HidBenefitNameSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benefit_id** | **str** |  | [optional] 
**health_id** | **str** |  | [optional] 

## Example

```python
from abha.models.hid_benefit_name_search_request import HidBenefitNameSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HidBenefitNameSearchRequest from a JSON string
hid_benefit_name_search_request_instance = HidBenefitNameSearchRequest.from_json(json)
# print the JSON string representation of the object
print(HidBenefitNameSearchRequest.to_json())

# convert the object into a dict
hid_benefit_name_search_request_dict = hid_benefit_name_search_request_instance.to_dict()
# create an instance of HidBenefitNameSearchRequest from a dict
hid_benefit_name_search_request_from_dict = HidBenefitNameSearchRequest.from_dict(hid_benefit_name_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


