# ShareProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request. | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**profile** | [**ShareProfileRequestProfile**](ShareProfileRequestProfile.md) |  | 

## Example

```python
from abdm_gateway.models.share_profile_request import ShareProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShareProfileRequest from a JSON string
share_profile_request_instance = ShareProfileRequest.from_json(json)
# print the JSON string representation of the object
print(ShareProfileRequest.to_json())

# convert the object into a dict
share_profile_request_dict = share_profile_request_instance.to_dict()
# create an instance of ShareProfileRequest from a dict
share_profile_request_from_dict = ShareProfileRequest.from_dict(share_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


