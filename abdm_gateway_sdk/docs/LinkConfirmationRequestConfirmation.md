# LinkConfirmationRequestConfirmation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_ref_number** | **str** |  | 
**token** | **str** |  | 

## Example

```python
from abdm_gateway.models.link_confirmation_request_confirmation import LinkConfirmationRequestConfirmation

# TODO update the JSON string below
json = "{}"
# create an instance of LinkConfirmationRequestConfirmation from a JSON string
link_confirmation_request_confirmation_instance = LinkConfirmationRequestConfirmation.from_json(json)
# print the JSON string representation of the object
print(LinkConfirmationRequestConfirmation.to_json())

# convert the object into a dict
link_confirmation_request_confirmation_dict = link_confirmation_request_confirmation_instance.to_dict()
# create an instance of LinkConfirmationRequestConfirmation from a dict
link_confirmation_request_confirmation_from_dict = LinkConfirmationRequestConfirmation.from_dict(link_confirmation_request_confirmation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


