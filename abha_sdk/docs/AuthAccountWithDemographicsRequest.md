# AuthAccountWithDemographicsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gender** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**txn_id** | **str** |  | [optional] 
**year_of_birth** | **str** |  | [optional] 

## Example

```python
from abha.models.auth_account_with_demographics_request import AuthAccountWithDemographicsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthAccountWithDemographicsRequest from a JSON string
auth_account_with_demographics_request_instance = AuthAccountWithDemographicsRequest.from_json(json)
# print the JSON string representation of the object
print(AuthAccountWithDemographicsRequest.to_json())

# convert the object into a dict
auth_account_with_demographics_request_dict = auth_account_with_demographics_request_instance.to_dict()
# create an instance of AuthAccountWithDemographicsRequest from a dict
auth_account_with_demographics_request_from_dict = AuthAccountWithDemographicsRequest.from_dict(auth_account_with_demographics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


