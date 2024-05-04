# ShareProfileRequest1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request. | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**intent** | [**ShareProfileRequest1Intent**](ShareProfileRequest1Intent.md) |  | 
**location** | [**Location**](Location.md) |  | 
**profile** | [**ShareProfileRequest1Profile**](ShareProfileRequest1Profile.md) |  | 

## Example

```python
from abdm_gateway.models.share_profile_request1 import ShareProfileRequest1

# TODO update the JSON string below
json = "{}"
# create an instance of ShareProfileRequest1 from a JSON string
share_profile_request1_instance = ShareProfileRequest1.from_json(json)
# print the JSON string representation of the object
print(ShareProfileRequest1.to_json())

# convert the object into a dict
share_profile_request1_dict = share_profile_request1_instance.to_dict()
# create an instance of ShareProfileRequest1 from a dict
share_profile_request1_from_dict = ShareProfileRequest1.from_dict(share_profile_request1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


