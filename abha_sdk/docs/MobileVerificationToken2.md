# MobileVerificationToken2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**txnid** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**mobile_linked_hid** | [**MobileVerificationToken2MobileLinkedHid**](MobileVerificationToken2MobileLinkedHid.md) |  | [optional] 

## Example

```python
from abha.models.mobile_verification_token2 import MobileVerificationToken2

# TODO update the JSON string below
json = "{}"
# create an instance of MobileVerificationToken2 from a JSON string
mobile_verification_token2_instance = MobileVerificationToken2.from_json(json)
# print the JSON string representation of the object
print(MobileVerificationToken2.to_json())

# convert the object into a dict
mobile_verification_token2_dict = mobile_verification_token2_instance.to_dict()
# create an instance of MobileVerificationToken2 from a dict
mobile_verification_token2_from_dict = MobileVerificationToken2.from_dict(mobile_verification_token2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


