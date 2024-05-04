# Requester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**identifier** | [**RequesterIdentifier**](RequesterIdentifier.md) |  | [optional] 

## Example

```python
from abdm_gateway.models.requester import Requester

# TODO update the JSON string below
json = "{}"
# create an instance of Requester from a JSON string
requester_instance = Requester.from_json(json)
# print the JSON string representation of the object
print(Requester.to_json())

# convert the object into a dict
requester_dict = requester_instance.to_dict()
# create an instance of Requester from a dict
requester_from_dict = Requester.from_dict(requester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


