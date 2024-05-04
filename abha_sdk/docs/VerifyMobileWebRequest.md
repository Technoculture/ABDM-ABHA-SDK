# VerifyMobileWebRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp** | **str** | Encrypted Mobile OTP. | 
**txn_id** | **str** | Based on UUID | 

## Example

```python
from abha.models.verify_mobile_web_request import VerifyMobileWebRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyMobileWebRequest from a JSON string
verify_mobile_web_request_instance = VerifyMobileWebRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyMobileWebRequest.to_json())

# convert the object into a dict
verify_mobile_web_request_dict = verify_mobile_web_request_instance.to_dict()
# create an instance of VerifyMobileWebRequest from a dict
verify_mobile_web_request_from_dict = VerifyMobileWebRequest.from_dict(verify_mobile_web_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


