# HidUpdateMobiletRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_id_number** | **str** |  | 
**mobile** | **str** |  | 

## Example

```python
from abha.models.hid_update_mobilet_request import HidUpdateMobiletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HidUpdateMobiletRequest from a JSON string
hid_update_mobilet_request_instance = HidUpdateMobiletRequest.from_json(json)
# print the JSON string representation of the object
print(HidUpdateMobiletRequest.to_json())

# convert the object into a dict
hid_update_mobilet_request_dict = hid_update_mobilet_request_instance.to_dict()
# create an instance of HidUpdateMobiletRequest from a dict
hid_update_mobilet_request_from_dict = HidUpdateMobiletRequest.from_dict(hid_update_mobilet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


