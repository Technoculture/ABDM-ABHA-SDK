# ProfileShare3Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abha_address** | **str** |  | 
**abha_number** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**year_of_birth** | **int** |  | [optional] 
**address** | **str** |  | [optional] 
**district** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**intent** | [**ProfileShare3RequestIntent**](ProfileShare3RequestIntent.md) |  | 
**meta_data** | [**AbdmProfileShare1RequestMetaData**](AbdmProfileShare1RequestMetaData.md) |  | 

## Example

```python
from abha.models.profile_share3_request import ProfileShare3Request

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileShare3Request from a JSON string
profile_share3_request_instance = ProfileShare3Request.from_json(json)
# print the JSON string representation of the object
print(ProfileShare3Request.to_json())

# convert the object into a dict
profile_share3_request_dict = profile_share3_request_instance.to_dict()
# create an instance of ProfileShare3Request from a dict
profile_share3_request_from_dict = ProfileShare3Request.from_dict(profile_share3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


