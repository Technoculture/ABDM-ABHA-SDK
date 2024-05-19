# RetrieveHealthIdPayloadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_id** | **str** |  | [optional] 
**health_id_number** | **str** |  | [optional] 

## Example

```python
from abha.models.retrieve_health_id_payload_response import RetrieveHealthIdPayloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveHealthIdPayloadResponse from a JSON string
retrieve_health_id_payload_response_instance = RetrieveHealthIdPayloadResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveHealthIdPayloadResponse.to_json())

# convert the object into a dict
retrieve_health_id_payload_response_dict = retrieve_health_id_payload_response_instance.to_dict()
# create an instance of RetrieveHealthIdPayloadResponse from a dict
retrieve_health_id_payload_response_from_dict = RetrieveHealthIdPayloadResponse.from_dict(retrieve_health_id_payload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


