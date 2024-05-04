# SearchPayLoadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from abha.models.search_pay_load_response import SearchPayLoadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchPayLoadResponse from a JSON string
search_pay_load_response_instance = SearchPayLoadResponse.from_json(json)
# print the JSON string representation of the object
print(SearchPayLoadResponse.to_json())

# convert the object into a dict
search_pay_load_response_dict = search_pay_load_response_instance.to_dict()
# create an instance of SearchPayLoadResponse from a dict
search_pay_load_response_from_dict = SearchPayLoadResponse.from_dict(search_pay_load_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


