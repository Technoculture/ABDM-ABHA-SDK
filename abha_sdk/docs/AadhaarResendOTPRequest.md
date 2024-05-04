# AadhaarResendOTPRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**txn_id** | **str** | Based on UUID | 

## Example

```python
from abha.models.aadhaar_resend_otp_request import AadhaarResendOTPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AadhaarResendOTPRequest from a JSON string
aadhaar_resend_otp_request_instance = AadhaarResendOTPRequest.from_json(json)
# print the JSON string representation of the object
print(AadhaarResendOTPRequest.to_json())

# convert the object into a dict
aadhaar_resend_otp_request_dict = aadhaar_resend_otp_request_instance.to_dict()
# create an instance of AadhaarResendOTPRequest from a dict
aadhaar_resend_otp_request_from_dict = AadhaarResendOTPRequest.from_dict(aadhaar_resend_otp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


