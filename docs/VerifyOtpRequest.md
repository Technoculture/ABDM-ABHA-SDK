# VerifyOtpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp** | **str** |  | 
**txn_id** | **str** | Based on UUID | 

## Example

```python
from abha.models.verify_otp_request import VerifyOtpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyOtpRequest from a JSON string
verify_otp_request_instance = VerifyOtpRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyOtpRequest.to_json())

# convert the object into a dict
verify_otp_request_dict = verify_otp_request_instance.to_dict()
# create an instance of VerifyOtpRequest from a dict
verify_otp_request_from_dict = VerifyOtpRequest.from_dict(verify_otp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


