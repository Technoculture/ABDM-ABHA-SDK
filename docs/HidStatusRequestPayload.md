# HidStatusRequestPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_id_number** | **str** |  | [optional] 

## Example

```python
from abha.models.hid_status_request_payload import HidStatusRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of HidStatusRequestPayload from a JSON string
hid_status_request_payload_instance = HidStatusRequestPayload.from_json(json)
# print the JSON string representation of the object
print(HidStatusRequestPayload.to_json())

# convert the object into a dict
hid_status_request_payload_dict = hid_status_request_payload_instance.to_dict()
# create an instance of HidStatusRequestPayload from a dict
hid_status_request_payload_from_dict = HidStatusRequestPayload.from_dict(hid_status_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


