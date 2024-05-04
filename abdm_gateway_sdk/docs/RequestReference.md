# RequestReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | the requestId that was passed | 

## Example

```python
from abdm_gateway.models.request_reference import RequestReference

# TODO update the JSON string below
json = "{}"
# create an instance of RequestReference from a JSON string
request_reference_instance = RequestReference.from_json(json)
# print the JSON string representation of the object
print(RequestReference.to_json())

# convert the object into a dict
request_reference_dict = request_reference_instance.to_dict()
# create an instance of RequestReference from a dict
request_reference_from_dict = RequestReference.from_dict(request_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


