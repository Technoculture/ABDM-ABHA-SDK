# GenerateMobileOTPForTxnRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mobile** | **str** |  | 
**txn_id** | **str** | Based on UUID | 

## Example

```python
from abha.models.generate_mobile_otp_for_txn_request import GenerateMobileOTPForTxnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateMobileOTPForTxnRequest from a JSON string
generate_mobile_otp_for_txn_request_instance = GenerateMobileOTPForTxnRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateMobileOTPForTxnRequest.to_json())

# convert the object into a dict
generate_mobile_otp_for_txn_request_dict = generate_mobile_otp_for_txn_request_instance.to_dict()
# create an instance of GenerateMobileOTPForTxnRequest from a dict
generate_mobile_otp_for_txn_request_from_dict = GenerateMobileOTPForTxnRequest.from_dict(generate_mobile_otp_for_txn_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


