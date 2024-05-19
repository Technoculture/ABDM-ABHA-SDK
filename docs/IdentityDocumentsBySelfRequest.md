# IdentityDocumentsBySelfRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**day_of_birth** | **str** |  | [optional] 
**district_code** | **str** |  | 
**document_number** | **str** | The number of the document | 
**document_type** | **str** | Type of the document | 
**first_name** | **str** |  | 
**gender** | **str** |  | 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**mobile** | **str** |  | 
**month_of_birth** | **str** |  | [optional] 
**photo** | **bytearray** | Encoded with Base 64 | [optional] 
**photo_back** | **bytearray** | Encoded with Base 64 | [optional] 
**state_code** | **str** |  | 
**txn_id** | **str** | Based on UUID | 
**year_of_birth** | **str** |  | 

## Example

```python
from abha.models.identity_documents_by_self_request import IdentityDocumentsBySelfRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityDocumentsBySelfRequest from a JSON string
identity_documents_by_self_request_instance = IdentityDocumentsBySelfRequest.from_json(json)
# print the JSON string representation of the object
print(IdentityDocumentsBySelfRequest.to_json())

# convert the object into a dict
identity_documents_by_self_request_dict = identity_documents_by_self_request_instance.to_dict()
# create an instance of IdentityDocumentsBySelfRequest from a dict
identity_documents_by_self_request_from_dict = IdentityDocumentsBySelfRequest.from_dict(identity_documents_by_self_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


