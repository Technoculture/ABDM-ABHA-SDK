# AccessTokenValidity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | [**PatientAuthPurpose**](PatientAuthPurpose.md) |  | 
**requester** | [**PatientAuthRequester**](PatientAuthRequester.md) |  | 
**expiry** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**limit** | **int** | number of times, the token can be used | 

## Example

```python
from abdm_gateway.models.access_token_validity import AccessTokenValidity

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenValidity from a JSON string
access_token_validity_instance = AccessTokenValidity.from_json(json)
# print the JSON string representation of the object
print(AccessTokenValidity.to_json())

# convert the object into a dict
access_token_validity_dict = access_token_validity_instance.to_dict()
# create an instance of AccessTokenValidity from a dict
access_token_validity_from_dict = AccessTokenValidity.from_dict(access_token_validity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


