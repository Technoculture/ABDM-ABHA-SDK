# EmailVerificationOTPRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** | Valid Email Address of the Beneficiary. | [optional] 

## Example

```python
from abha.models.email_verification_otp_request import EmailVerificationOTPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailVerificationOTPRequest from a JSON string
email_verification_otp_request_instance = EmailVerificationOTPRequest.from_json(json)
# print the JSON string representation of the object
print(EmailVerificationOTPRequest.to_json())

# convert the object into a dict
email_verification_otp_request_dict = email_verification_otp_request_instance.to_dict()
# create an instance of EmailVerificationOTPRequest from a dict
email_verification_otp_request_from_dict = EmailVerificationOTPRequest.from_dict(email_verification_otp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


