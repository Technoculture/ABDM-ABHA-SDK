# HidChangePasswordRequestPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_password** | **str** |  | 
**old_password** | **str** |  | 

## Example

```python
from abha.models.hid_change_password_request_payload import HidChangePasswordRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of HidChangePasswordRequestPayload from a JSON string
hid_change_password_request_payload_instance = HidChangePasswordRequestPayload.from_json(json)
# print the JSON string representation of the object
print(HidChangePasswordRequestPayload.to_json())

# convert the object into a dict
hid_change_password_request_payload_dict = hid_change_password_request_payload_instance.to_dict()
# create an instance of HidChangePasswordRequestPayload from a dict
hid_change_password_request_payload_from_dict = HidChangePasswordRequestPayload.from_dict(hid_change_password_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


