# MobileNumberNewRequestPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_mobile_number** | **str** | New Mobile Number. | [optional] 

## Example

```python
from abha.models.mobile_number_new_request_payload import MobileNumberNewRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of MobileNumberNewRequestPayload from a JSON string
mobile_number_new_request_payload_instance = MobileNumberNewRequestPayload.from_json(json)
# print the JSON string representation of the object
print(MobileNumberNewRequestPayload.to_json())

# convert the object into a dict
mobile_number_new_request_payload_dict = mobile_number_new_request_payload_instance.to_dict()
# create an instance of MobileNumberNewRequestPayload from a dict
mobile_number_new_request_payload_from_dict = MobileNumberNewRequestPayload.from_dict(mobile_number_new_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


