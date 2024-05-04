# VerifyAadhaarOtp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp** | **str** |  | 
**txn_id** | **str** | Based on UUID | 

## Example

```python
from abha.models.verify_aadhaar_otp import VerifyAadhaarOtp

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyAadhaarOtp from a JSON string
verify_aadhaar_otp_instance = VerifyAadhaarOtp.from_json(json)
# print the JSON string representation of the object
print(VerifyAadhaarOtp.to_json())

# convert the object into a dict
verify_aadhaar_otp_dict = verify_aadhaar_otp_instance.to_dict()
# create an instance of VerifyAadhaarOtp from a dict
verify_aadhaar_otp_from_dict = VerifyAadhaarOtp.from_dict(verify_aadhaar_otp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


