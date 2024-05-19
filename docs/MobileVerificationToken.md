# MobileVerificationToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 

## Example

```python
from abha.models.mobile_verification_token import MobileVerificationToken

# TODO update the JSON string below
json = "{}"
# create an instance of MobileVerificationToken from a JSON string
mobile_verification_token_instance = MobileVerificationToken.from_json(json)
# print the JSON string representation of the object
print(MobileVerificationToken.to_json())

# convert the object into a dict
mobile_verification_token_dict = mobile_verification_token_instance.to_dict()
# create an instance of MobileVerificationToken from a dict
mobile_verification_token_from_dict = MobileVerificationToken.from_dict(mobile_verification_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


