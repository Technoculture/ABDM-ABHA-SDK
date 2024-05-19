# HidDelinkOtherProgrammeRequestPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benefit_id** | **str** |  | 
**health_id_number** | **str** |  | 

## Example

```python
from abha.models.hid_delink_other_programme_request_payload import HidDelinkOtherProgrammeRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of HidDelinkOtherProgrammeRequestPayload from a JSON string
hid_delink_other_programme_request_payload_instance = HidDelinkOtherProgrammeRequestPayload.from_json(json)
# print the JSON string representation of the object
print(HidDelinkOtherProgrammeRequestPayload.to_json())

# convert the object into a dict
hid_delink_other_programme_request_payload_dict = hid_delink_other_programme_request_payload_instance.to_dict()
# create an instance of HidDelinkOtherProgrammeRequestPayload from a dict
hid_delink_other_programme_request_payload_from_dict = HidDelinkOtherProgrammeRequestPayload.from_dict(hid_delink_other_programme_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


