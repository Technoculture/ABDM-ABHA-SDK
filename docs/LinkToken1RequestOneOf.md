# LinkToken1RequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abha_address** | **str** |  | [optional] 
**link_token** | **str** |  | 
**response** | [**ProfileShare2RequestOneOfResponse**](ProfileShare2RequestOneOfResponse.md) |  | 

## Example

```python
from abha.models.link_token1_request_one_of import LinkToken1RequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of LinkToken1RequestOneOf from a JSON string
link_token1_request_one_of_instance = LinkToken1RequestOneOf.from_json(json)
# print the JSON string representation of the object
print(LinkToken1RequestOneOf.to_json())

# convert the object into a dict
link_token1_request_one_of_dict = link_token1_request_one_of_instance.to_dict()
# create an instance of LinkToken1RequestOneOf from a dict
link_token1_request_one_of_from_dict = LinkToken1RequestOneOf.from_dict(link_token1_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


