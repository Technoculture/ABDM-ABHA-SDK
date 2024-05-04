# ShareProfileRequest1Profile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hip_code** | **str** | additional details about HIP retrieved after scanning QR. | [optional] 
**patient** | [**ShareProfileRequestProfilePatient**](ShareProfileRequestProfilePatient.md) |  | 

## Example

```python
from abdm_gateway.models.share_profile_request1_profile import ShareProfileRequest1Profile

# TODO update the JSON string below
json = "{}"
# create an instance of ShareProfileRequest1Profile from a JSON string
share_profile_request1_profile_instance = ShareProfileRequest1Profile.from_json(json)
# print the JSON string representation of the object
print(ShareProfileRequest1Profile.to_json())

# convert the object into a dict
share_profile_request1_profile_dict = share_profile_request1_profile_instance.to_dict()
# create an instance of ShareProfileRequest1Profile from a dict
share_profile_request1_profile_from_dict = ShareProfileRequest1Profile.from_dict(share_profile_request1_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


