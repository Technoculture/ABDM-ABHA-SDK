# MobileResendOTPRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**txn_id** | **str** | Based on UUID | 

## Example

```python
from abha.models.mobile_resend_otp_request import MobileResendOTPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MobileResendOTPRequest from a JSON string
mobile_resend_otp_request_instance = MobileResendOTPRequest.from_json(json)
# print the JSON string representation of the object
print(MobileResendOTPRequest.to_json())

# convert the object into a dict
mobile_resend_otp_request_dict = mobile_resend_otp_request_instance.to_dict()
# create an instance of MobileResendOTPRequest from a dict
mobile_resend_otp_request_from_dict = MobileResendOTPRequest.from_dict(mobile_resend_otp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


