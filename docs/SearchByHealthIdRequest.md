# SearchByHealthIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_id** | **str** |  | 

## Example

```python
from abha.models.search_by_health_id_request import SearchByHealthIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchByHealthIdRequest from a JSON string
search_by_health_id_request_instance = SearchByHealthIdRequest.from_json(json)
# print the JSON string representation of the object
print(SearchByHealthIdRequest.to_json())

# convert the object into a dict
search_by_health_id_request_dict = search_by_health_id_request_instance.to_dict()
# create an instance of SearchByHealthIdRequest from a dict
search_by_health_id_request_from_dict = SearchByHealthIdRequest.from_dict(search_by_health_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


