# HIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** |  | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**hi_request** | [**HIRequestHiRequest**](HIRequestHiRequest.md) |  | 

## Example

```python
from abdm_gateway.models.hi_request import HIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HIRequest from a JSON string
hi_request_instance = HIRequest.from_json(json)
# print the JSON string representation of the object
print(HIRequest.to_json())

# convert the object into a dict
hi_request_dict = hi_request_instance.to_dict()
# create an instance of HIRequest from a dict
hi_request_from_dict = HIRequest.from_dict(hi_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


