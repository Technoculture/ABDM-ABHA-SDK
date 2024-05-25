# ProfileShare2RequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledgement** | [**ProfileShare2RequestOneOfAcknowledgement**](ProfileShare2RequestOneOfAcknowledgement.md) |  | [optional] 
**response** | [**ProfileShare2RequestOneOfResponse**](ProfileShare2RequestOneOfResponse.md) |  | 

## Example

```python
from abha.models.profile_share2_request_one_of import ProfileShare2RequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileShare2RequestOneOf from a JSON string
profile_share2_request_one_of_instance = ProfileShare2RequestOneOf.from_json(json)
# print the JSON string representation of the object
print(ProfileShare2RequestOneOf.to_json())

# convert the object into a dict
profile_share2_request_one_of_dict = profile_share2_request_one_of_instance.to_dict()
# create an instance of ProfileShare2RequestOneOf from a dict
profile_share2_request_one_of_from_dict = ProfileShare2RequestOneOf.from_dict(profile_share2_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


