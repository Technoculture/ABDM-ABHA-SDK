# HidOtpRequestPaylaod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_password** | **str** |  | 
**otp** | **str** |  | 
**txn_id** | **str** | Based on UUID | 

## Example

```python
from abha.models.hid_otp_request_paylaod import HidOtpRequestPaylaod

# TODO update the JSON string below
json = "{}"
# create an instance of HidOtpRequestPaylaod from a JSON string
hid_otp_request_paylaod_instance = HidOtpRequestPaylaod.from_json(json)
# print the JSON string representation of the object
print(HidOtpRequestPaylaod.to_json())

# convert the object into a dict
hid_otp_request_paylaod_dict = hid_otp_request_paylaod_instance.to_dict()
# create an instance of HidOtpRequestPaylaod from a dict
hid_otp_request_paylaod_from_dict = HidOtpRequestPaylaod.from_dict(hid_otp_request_paylaod_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


