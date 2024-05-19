# ResendOTPRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method** | **str** | Based on authMethods | [optional] 
**txn_id** | **str** | Based on UUID | 

## Example

```python
from abha.models.resend_otp_request import ResendOTPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResendOTPRequest from a JSON string
resend_otp_request_instance = ResendOTPRequest.from_json(json)
# print the JSON string representation of the object
print(ResendOTPRequest.to_json())

# convert the object into a dict
resend_otp_request_dict = resend_otp_request_instance.to_dict()
# create an instance of ResendOTPRequest from a dict
resend_otp_request_from_dict = ResendOTPRequest.from_dict(resend_otp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


