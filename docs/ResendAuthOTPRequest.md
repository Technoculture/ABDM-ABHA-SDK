# ResendAuthOTPRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method** | **str** |  | 
**txn_id** | **str** | Based on UUID | 

## Example

```python
from abha.models.resend_auth_otp_request import ResendAuthOTPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResendAuthOTPRequest from a JSON string
resend_auth_otp_request_instance = ResendAuthOTPRequest.from_json(json)
# print the JSON string representation of the object
print(ResendAuthOTPRequest.to_json())

# convert the object into a dict
resend_auth_otp_request_dict = resend_auth_otp_request_instance.to_dict()
# create an instance of ResendAuthOTPRequest from a dict
resend_auth_otp_request_from_dict = ResendAuthOTPRequest.from_dict(resend_auth_otp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


