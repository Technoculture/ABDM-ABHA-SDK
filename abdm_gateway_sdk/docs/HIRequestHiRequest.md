# HIRequestHiRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent** | [**Consent**](Consent.md) |  | 
**date_range** | [**DateRange**](DateRange.md) |  | 
**data_push_url** | **str** |  | 
**key_material** | [**KeyMaterial**](KeyMaterial.md) |  | 

## Example

```python
from abdm_gateway.models.hi_request_hi_request import HIRequestHiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HIRequestHiRequest from a JSON string
hi_request_hi_request_instance = HIRequestHiRequest.from_json(json)
# print the JSON string representation of the object
print(HIRequestHiRequest.to_json())

# convert the object into a dict
hi_request_hi_request_dict = hi_request_hi_request_instance.to_dict()
# create an instance of HIRequestHiRequest from a dict
hi_request_hi_request_from_dict = HIRequestHiRequest.from_dict(hi_request_hi_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


