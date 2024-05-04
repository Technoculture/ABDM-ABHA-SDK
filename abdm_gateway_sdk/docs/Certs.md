# Certs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[CertificateOrKeyGetSchema]**](CertificateOrKeyGetSchema.md) |  | [optional] 

## Example

```python
from abdm_gateway.models.certs import Certs

# TODO update the JSON string below
json = "{}"
# create an instance of Certs from a JSON string
certs_instance = Certs.from_json(json)
# print the JSON string representation of the object
print(Certs.to_json())

# convert the object into a dict
certs_dict = certs_instance.to_dict()
# create an instance of Certs from a dict
certs_from_dict = Certs.from_dict(certs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


