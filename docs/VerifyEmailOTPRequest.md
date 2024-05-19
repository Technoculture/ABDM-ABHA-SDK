# VerifyEmailOTPRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypted_otp** | **str** | OTP recevied over the Email. OTP in the encrypted form. | [optional] 
**txn_id** | **str** | Transaction ID | 

## Example

```python
from abha.models.verify_email_otp_request import VerifyEmailOTPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyEmailOTPRequest from a JSON string
verify_email_otp_request_instance = VerifyEmailOTPRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyEmailOTPRequest.to_json())

# convert the object into a dict
verify_email_otp_request_dict = verify_email_otp_request_instance.to_dict()
# create an instance of VerifyEmailOTPRequest from a dict
verify_email_otp_request_from_dict = VerifyEmailOTPRequest.from_dict(verify_email_otp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


