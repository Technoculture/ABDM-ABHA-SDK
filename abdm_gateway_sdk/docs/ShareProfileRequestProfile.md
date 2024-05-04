# ShareProfileRequestProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hip_code** | **str** | additional details about HIP retrieved after scanning QR. | [optional] 
**patient** | [**ShareProfileRequestProfilePatient**](ShareProfileRequestProfilePatient.md) |  | [optional] 

## Example

```python
from abdm_gateway.models.share_profile_request_profile import ShareProfileRequestProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ShareProfileRequestProfile from a JSON string
share_profile_request_profile_instance = ShareProfileRequestProfile.from_json(json)
# print the JSON string representation of the object
print(ShareProfileRequestProfile.to_json())

# convert the object into a dict
share_profile_request_profile_dict = share_profile_request_profile_instance.to_dict()
# create an instance of ShareProfileRequestProfile from a dict
share_profile_request_profile_from_dict = ShareProfileRequestProfile.from_dict(share_profile_request_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


