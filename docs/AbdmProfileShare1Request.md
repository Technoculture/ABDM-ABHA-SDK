# AbdmProfileShare1Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intent** | [**AbdmProfileShare1RequestIntent**](AbdmProfileShare1RequestIntent.md) |  | 
**meta_data** | [**AbdmProfileShare1RequestMetaData**](AbdmProfileShare1RequestMetaData.md) |  | [optional] 

## Example

```python
from abha.models.abdm_profile_share1_request import AbdmProfileShare1Request

# TODO update the JSON string below
json = "{}"
# create an instance of AbdmProfileShare1Request from a JSON string
abdm_profile_share1_request_instance = AbdmProfileShare1Request.from_json(json)
# print the JSON string representation of the object
print(AbdmProfileShare1Request.to_json())

# convert the object into a dict
abdm_profile_share1_request_dict = abdm_profile_share1_request_instance.to_dict()
# create an instance of AbdmProfileShare1Request from a dict
abdm_profile_share1_request_from_dict = AbdmProfileShare1Request.from_dict(abdm_profile_share1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


