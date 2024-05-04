# OpenIdConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jwks_uri** | **str** |  | [optional] 

## Example

```python
from abdm_gateway.models.open_id_configuration import OpenIdConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIdConfiguration from a JSON string
open_id_configuration_instance = OpenIdConfiguration.from_json(json)
# print the JSON string representation of the object
print(OpenIdConfiguration.to_json())

# convert the object into a dict
open_id_configuration_dict = open_id_configuration_instance.to_dict()
# create an instance of OpenIdConfiguration from a dict
open_id_configuration_from_dict = OpenIdConfiguration.from_dict(open_id_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


