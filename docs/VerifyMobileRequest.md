# VerifyMobileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp** | **str** |  | 
**txn_id** | **str** | Based on UUID | 

## Example

```python
from abha.models.verify_mobile_request import VerifyMobileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyMobileRequest from a JSON string
verify_mobile_request_instance = VerifyMobileRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyMobileRequest.to_json())

# convert the object into a dict
verify_mobile_request_dict = verify_mobile_request_instance.to_dict()
# create an instance of VerifyMobileRequest from a dict
verify_mobile_request_from_dict = VerifyMobileRequest.from_dict(verify_mobile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


