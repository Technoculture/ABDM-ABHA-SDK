# ProfileShare2Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledgement** | [**ProfileShare2RequestOneOfAcknowledgement**](ProfileShare2RequestOneOfAcknowledgement.md) |  | [optional] 
**response** | [**ProfileShare2RequestOneOfResponse**](ProfileShare2RequestOneOfResponse.md) |  | 

## Example

```python
from abha.models.profile_share2_request import ProfileShare2Request

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileShare2Request from a JSON string
profile_share2_request_instance = ProfileShare2Request.from_json(json)
# print the JSON string representation of the object
print(ProfileShare2Request.to_json())

# convert the object into a dict
profile_share2_request_dict = profile_share2_request_instance.to_dict()
# create an instance of ProfileShare2Request from a dict
profile_share2_request_from_dict = ProfileShare2Request.from_dict(profile_share2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


