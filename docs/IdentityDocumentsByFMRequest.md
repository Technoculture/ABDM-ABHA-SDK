# IdentityDocumentsByFMRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**day_of_birth** | **str** |  | [optional] 
**district_code** | **str** |  | [optional] 
**document_number** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**mobile** | **str** |  | [optional] 
**month_of_birth** | **str** |  | [optional] 
**photo** | **bytearray** |  | [optional] 
**photo_back** | **bytearray** |  | [optional] 
**state_code** | **str** |  | [optional] 
**txn_id** | **str** |  | [optional] 
**year_of_birth** | **str** |  | [optional] 

## Example

```python
from abha.models.identity_documents_by_fm_request import IdentityDocumentsByFMRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityDocumentsByFMRequest from a JSON string
identity_documents_by_fm_request_instance = IdentityDocumentsByFMRequest.from_json(json)
# print the JSON string representation of the object
print(IdentityDocumentsByFMRequest.to_json())

# convert the object into a dict
identity_documents_by_fm_request_dict = identity_documents_by_fm_request_instance.to_dict()
# create an instance of IdentityDocumentsByFMRequest from a dict
identity_documents_by_fm_request_from_dict = IdentityDocumentsByFMRequest.from_dict(identity_documents_by_fm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


