# AuthConfirmIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AuthConfirmIdentifierType**](AuthConfirmIdentifierType.md) |  | 
**value** | **str** |  | 

## Example

```python
from abdm_gateway.models.auth_confirm_identifier import AuthConfirmIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of AuthConfirmIdentifier from a JSON string
auth_confirm_identifier_instance = AuthConfirmIdentifier.from_json(json)
# print the JSON string representation of the object
print(AuthConfirmIdentifier.to_json())

# convert the object into a dict
auth_confirm_identifier_dict = auth_confirm_identifier_instance.to_dict()
# create an instance of AuthConfirmIdentifier from a dict
auth_confirm_identifier_from_dict = AuthConfirmIdentifier.from_dict(auth_confirm_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


