# SearchByMobileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gender** | **str** |  | [optional] 
**mobile** | **str** |  | 
**name** | **str** |  | [optional] 
**year_of_birth** | **str** |  | [optional] 

## Example

```python
from abha.models.search_by_mobile_request import SearchByMobileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchByMobileRequest from a JSON string
search_by_mobile_request_instance = SearchByMobileRequest.from_json(json)
# print the JSON string representation of the object
print(SearchByMobileRequest.to_json())

# convert the object into a dict
search_by_mobile_request_dict = search_by_mobile_request_instance.to_dict()
# create an instance of SearchByMobileRequest from a dict
search_by_mobile_request_from_dict = SearchByMobileRequest.from_dict(search_by_mobile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


