# SearchResponseSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_methods** | **List[str]** |  | [optional] 
**health_id** | **str** |  | [optional] 
**health_id_number** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from abha.models.search_response_single import SearchResponseSingle

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponseSingle from a JSON string
search_response_single_instance = SearchResponseSingle.from_json(json)
# print the JSON string representation of the object
print(SearchResponseSingle.to_json())

# convert the object into a dict
search_response_single_dict = search_response_single_instance.to_dict()
# create an instance of SearchResponseSingle from a dict
search_response_single_from_dict = SearchResponseSingle.from_dict(search_response_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


