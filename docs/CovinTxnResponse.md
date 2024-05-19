# CovinTxnResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mobile_number** | **str** |  | [optional] 
**txn_id** | **str** | Based on UUID | [optional] 

## Example

```python
from abha.models.covin_txn_response import CovinTxnResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CovinTxnResponse from a JSON string
covin_txn_response_instance = CovinTxnResponse.from_json(json)
# print the JSON string representation of the object
print(CovinTxnResponse.to_json())

# convert the object into a dict
covin_txn_response_dict = covin_txn_response_instance.to_dict()
# create an instance of CovinTxnResponse from a dict
covin_txn_response_from_dict = CovinTxnResponse.from_dict(covin_txn_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


