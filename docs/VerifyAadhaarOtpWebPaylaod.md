# VerifyAadhaarOtpWebPaylaod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp** | **str** | Encrypted Mobile OTP. | 
**txn_id** | **str** | Based on UUID | 

## Example

```python
from abha.models.verify_aadhaar_otp_web_paylaod import VerifyAadhaarOtpWebPaylaod

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyAadhaarOtpWebPaylaod from a JSON string
verify_aadhaar_otp_web_paylaod_instance = VerifyAadhaarOtpWebPaylaod.from_json(json)
# print the JSON string representation of the object
print(VerifyAadhaarOtpWebPaylaod.to_json())

# convert the object into a dict
verify_aadhaar_otp_web_paylaod_dict = verify_aadhaar_otp_web_paylaod_instance.to_dict()
# create an instance of VerifyAadhaarOtpWebPaylaod from a dict
verify_aadhaar_otp_web_paylaod_from_dict = VerifyAadhaarOtpWebPaylaod.from_dict(verify_aadhaar_otp_web_paylaod_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


