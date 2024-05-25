# LinkToken1Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abha_address** | **str** |  | [optional] 
**link_token** | **str** |  | 
**response** | [**ProfileShare2RequestOneOfResponse**](ProfileShare2RequestOneOfResponse.md) |  | 
**error** | [**LinkToken1RequestOneOf3Error**](LinkToken1RequestOneOf3Error.md) |  | 

## Example

```python
from abha.models.link_token1_request import LinkToken1Request

# TODO update the JSON string below
json = "{}"
# create an instance of LinkToken1Request from a JSON string
link_token1_request_instance = LinkToken1Request.from_json(json)
# print the JSON string representation of the object
print(LinkToken1Request.to_json())

# convert the object into a dict
link_token1_request_dict = link_token1_request_instance.to_dict()
# create an instance of LinkToken1Request from a dict
link_token1_request_from_dict = LinkToken1Request.from_dict(link_token1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


