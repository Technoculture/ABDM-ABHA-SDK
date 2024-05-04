# LinkConfirmationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** |  | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**confirmation** | [**LinkConfirmationRequestConfirmation**](LinkConfirmationRequestConfirmation.md) |  | 

## Example

```python
from abdm_gateway.models.link_confirmation_request import LinkConfirmationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkConfirmationRequest from a JSON string
link_confirmation_request_instance = LinkConfirmationRequest.from_json(json)
# print the JSON string representation of the object
print(LinkConfirmationRequest.to_json())

# convert the object into a dict
link_confirmation_request_dict = link_confirmation_request_instance.to_dict()
# create an instance of LinkConfirmationRequest from a dict
link_confirmation_request_from_dict = LinkConfirmationRequest.from_dict(link_confirmation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


