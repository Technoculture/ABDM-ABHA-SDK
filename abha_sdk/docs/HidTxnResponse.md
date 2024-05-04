# HidTxnResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mobile_number** | **str** |  | [optional] 
**txn_id** | **str** | Based on UUID | [optional] 

## Example

```python
from abha.models.hid_txn_response import HidTxnResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HidTxnResponse from a JSON string
hid_txn_response_instance = HidTxnResponse.from_json(json)
# print the JSON string representation of the object
print(HidTxnResponse.to_json())

# convert the object into a dict
hid_txn_response_dict = hid_txn_response_instance.to_dict()
# create an instance of HidTxnResponse from a dict
hid_txn_response_from_dict = HidTxnResponse.from_dict(hid_txn_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


