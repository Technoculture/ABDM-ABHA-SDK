# VerifyIdentityDocumentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_birth** | **str** |  | [optional] 
**document_number** | **str** |  | 
**document_type** | **str** |  | 
**first_name** | **str** |  | 
**gender** | **str** |  | 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**month_of_birth** | **str** |  | [optional] 
**year_of_birth** | **str** |  | 

## Example

```python
from abha.models.verify_identity_documents_request import VerifyIdentityDocumentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyIdentityDocumentsRequest from a JSON string
verify_identity_documents_request_instance = VerifyIdentityDocumentsRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyIdentityDocumentsRequest.to_json())

# convert the object into a dict
verify_identity_documents_request_dict = verify_identity_documents_request_instance.to_dict()
# create an instance of VerifyIdentityDocumentsRequest from a dict
verify_identity_documents_request_from_dict = VerifyIdentityDocumentsRequest.from_dict(verify_identity_documents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


