# ChangeStatusByOtpAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method** | **str** | Based on authMethods | 
**otp** | **str** | Encrypted Mobile OTP. | [optional] 
**password** | **str** |  | [optional] 
**reactivation_date** | **str** |  | [optional] 
**reasons** | **List[str]** |  | [optional] 
**txn_id** | **str** | Based on UUID | [optional] 

## Example

```python
from abha.models.change_status_by_otp_account_request import ChangeStatusByOtpAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeStatusByOtpAccountRequest from a JSON string
change_status_by_otp_account_request_instance = ChangeStatusByOtpAccountRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeStatusByOtpAccountRequest.to_json())

# convert the object into a dict
change_status_by_otp_account_request_dict = change_status_by_otp_account_request_instance.to_dict()
# create an instance of ChangeStatusByOtpAccountRequest from a dict
change_status_by_otp_account_request_from_dict = ChangeStatusByOtpAccountRequest.from_dict(change_status_by_otp_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


