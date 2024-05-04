# CertificateOrKeyGetSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e** | **str** |  | [optional] 
**kid** | **str** |  | [optional] 
**kty** | **str** |  | [optional] 
**n** | **str** |  | [optional] 
**use** | **str** |  | [optional] 
**x5c** | **List[str]** |  | [optional] 
**x5t** | **str** |  | [optional] 
**x5t_s256** | **str** |  | [optional] 
**alg** | **str** |  | [optional] 

## Example

```python
from abdm_gateway.models.certificate_or_key_get_schema import CertificateOrKeyGetSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateOrKeyGetSchema from a JSON string
certificate_or_key_get_schema_instance = CertificateOrKeyGetSchema.from_json(json)
# print the JSON string representation of the object
print(CertificateOrKeyGetSchema.to_json())

# convert the object into a dict
certificate_or_key_get_schema_dict = certificate_or_key_get_schema_instance.to_dict()
# create an instance of CertificateOrKeyGetSchema from a dict
certificate_or_key_get_schema_from_dict = CertificateOrKeyGetSchema.from_dict(certificate_or_key_get_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


