# HidLinkedOtherProgramRequestPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benefit_id** | **str** |  | 
**benefit_name** | **str** |  | 
**state_code** | **str** |  | [optional] 
**user_token** | **str** | JWT Bearer Token | 
**validity** | **str** |  | [optional] 

## Example

```python
from abha.models.hid_linked_other_program_request_payload import HidLinkedOtherProgramRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of HidLinkedOtherProgramRequestPayload from a JSON string
hid_linked_other_program_request_payload_instance = HidLinkedOtherProgramRequestPayload.from_json(json)
# print the JSON string representation of the object
print(HidLinkedOtherProgramRequestPayload.to_json())

# convert the object into a dict
hid_linked_other_program_request_payload_dict = hid_linked_other_program_request_payload_instance.to_dict()
# create an instance of HidLinkedOtherProgramRequestPayload from a dict
hid_linked_other_program_request_payload_from_dict = HidLinkedOtherProgramRequestPayload.from_dict(hid_linked_other_program_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


