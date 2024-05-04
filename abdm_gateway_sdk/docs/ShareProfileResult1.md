# ShareProfileResult1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**acknowledgement** | [**ShareProfileAcknowledgement1**](ShareProfileAcknowledgement1.md) |  | 
**error** | [**Error**](Error.md) |  | [optional] 
**resp** | [**RequestReference**](RequestReference.md) |  | 

## Example

```python
from abdm_gateway.models.share_profile_result1 import ShareProfileResult1

# TODO update the JSON string below
json = "{}"
# create an instance of ShareProfileResult1 from a JSON string
share_profile_result1_instance = ShareProfileResult1.from_json(json)
# print the JSON string representation of the object
print(ShareProfileResult1.to_json())

# convert the object into a dict
share_profile_result1_dict = share_profile_result1_instance.to_dict()
# create an instance of ShareProfileResult1 from a dict
share_profile_result1_from_dict = ShareProfileResult1.from_dict(share_profile_result1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


