# AuthWithMobileTxnAndUserData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gender** | **str** |  | [optional] 
**health_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**txn_id** | **str** |  | [optional] 
**year_of_birth** | **str** |  | [optional] 

## Example

```python
from abha.models.auth_with_mobile_txn_and_user_data import AuthWithMobileTxnAndUserData

# TODO update the JSON string below
json = "{}"
# create an instance of AuthWithMobileTxnAndUserData from a JSON string
auth_with_mobile_txn_and_user_data_instance = AuthWithMobileTxnAndUserData.from_json(json)
# print the JSON string representation of the object
print(AuthWithMobileTxnAndUserData.to_json())

# convert the object into a dict
auth_with_mobile_txn_and_user_data_dict = auth_with_mobile_txn_and_user_data_instance.to_dict()
# create an instance of AuthWithMobileTxnAndUserData from a dict
auth_with_mobile_txn_and_user_data_from_dict = AuthWithMobileTxnAndUserData.from_dict(auth_with_mobile_txn_and_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


