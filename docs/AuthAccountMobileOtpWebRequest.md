# AuthAccountMobileOtpWebRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp** | **str** | Encrypted Mobile OTP. | 
**txn_id** | **str** | Based on UUID | 

## Example

```python
from abha.models.auth_account_mobile_otp_web_request import AuthAccountMobileOtpWebRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthAccountMobileOtpWebRequest from a JSON string
auth_account_mobile_otp_web_request_instance = AuthAccountMobileOtpWebRequest.from_json(json)
# print the JSON string representation of the object
print(AuthAccountMobileOtpWebRequest.to_json())

# convert the object into a dict
auth_account_mobile_otp_web_request_dict = auth_account_mobile_otp_web_request_instance.to_dict()
# create an instance of AuthAccountMobileOtpWebRequest from a dict
auth_account_mobile_otp_web_request_from_dict = AuthAccountMobileOtpWebRequest.from_dict(auth_account_mobile_otp_web_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


