# VerifyIdentityDocumentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[FieldResponse]**](FieldResponse.md) |  | [optional] 
**matched** | **bool** |  | [optional] 

## Example

```python
from abha.models.verify_identity_documents_response import VerifyIdentityDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyIdentityDocumentsResponse from a JSON string
verify_identity_documents_response_instance = VerifyIdentityDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print(VerifyIdentityDocumentsResponse.to_json())

# convert the object into a dict
verify_identity_documents_response_dict = verify_identity_documents_response_instance.to_dict()
# create an instance of VerifyIdentityDocumentsResponse from a dict
verify_identity_documents_response_from_dict = VerifyIdentityDocumentsResponse.from_dict(verify_identity_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


