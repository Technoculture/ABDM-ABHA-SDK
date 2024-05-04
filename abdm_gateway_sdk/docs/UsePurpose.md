# UsePurpose


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**code** | **str** | From the fixed set, documented at refUri | 
**ref_uri** | **str** |  | [optional] 

## Example

```python
from abdm_gateway.models.use_purpose import UsePurpose

# TODO update the JSON string below
json = "{}"
# create an instance of UsePurpose from a JSON string
use_purpose_instance = UsePurpose.from_json(json)
# print the JSON string representation of the object
print(UsePurpose.to_json())

# convert the object into a dict
use_purpose_dict = use_purpose_instance.to_dict()
# create an instance of UsePurpose from a dict
use_purpose_from_dict = UsePurpose.from_dict(use_purpose_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


