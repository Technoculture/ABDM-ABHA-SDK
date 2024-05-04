# AuthMobileOTPRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**healthid** | **str** |  | [optional] 

## Example

```python
from abha.models.auth_mobile_otp_request import AuthMobileOTPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMobileOTPRequest from a JSON string
auth_mobile_otp_request_instance = AuthMobileOTPRequest.from_json(json)
# print the JSON string representation of the object
print(AuthMobileOTPRequest.to_json())

# convert the object into a dict
auth_mobile_otp_request_dict = auth_mobile_otp_request_instance.to_dict()
# create an instance of AuthMobileOTPRequest from a dict
auth_mobile_otp_request_from_dict = AuthMobileOTPRequest.from_dict(auth_mobile_otp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


