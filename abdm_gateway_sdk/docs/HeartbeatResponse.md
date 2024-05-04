# HeartbeatResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 

## Example

```python
from abdm_gateway.models.heartbeat_response import HeartbeatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HeartbeatResponse from a JSON string
heartbeat_response_instance = HeartbeatResponse.from_json(json)
# print the JSON string representation of the object
print(HeartbeatResponse.to_json())

# convert the object into a dict
heartbeat_response_dict = heartbeat_response_instance.to_dict()
# create an instance of HeartbeatResponse from a dict
heartbeat_response_from_dict = HeartbeatResponse.from_dict(heartbeat_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


