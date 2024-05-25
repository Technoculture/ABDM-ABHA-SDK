# AbdmLinkToken1Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abha_number** | **float** | it can be null if abhaAddress is exist | [optional] 
**abha_address** | **str** | it can be null if abhaNumber is exist | [optional] 
**name** | **str** |  | 
**gender** | **str** |  | 
**year_of_birth** | **float** |  | 

## Example

```python
from abha.models.abdm_link_token1_request import AbdmLinkToken1Request

# TODO update the JSON string below
json = "{}"
# create an instance of AbdmLinkToken1Request from a JSON string
abdm_link_token1_request_instance = AbdmLinkToken1Request.from_json(json)
# print the JSON string representation of the object
print(AbdmLinkToken1Request.to_json())

# convert the object into a dict
abdm_link_token1_request_dict = abdm_link_token1_request_instance.to_dict()
# create an instance of AbdmLinkToken1Request from a dict
abdm_link_token1_request_from_dict = AbdmLinkToken1Request.from_dict(abdm_link_token1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


