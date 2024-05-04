# IdentityDocumentsByFMResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**auth_methods** | **List[str]** | Based on authMethods | [optional] 
**day_of_birth** | **str** |  | [optional] 
**district_code** | **str** |  | [optional] 
**document_number** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**health_id** | **str** |  | [optional] 
**health_id_number** | **str** |  | [optional] 
**kyc_verified** | **bool** |  | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**mobile** | **str** |  | [optional] 
**month_of_birth** | **str** |  | [optional] 
**photo** | **bytearray** |  | [optional] 
**state** | **str** |  | [optional] 
**state_code** | **str** |  | [optional] 
**state_name** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**verification_status** | **str** |  | [optional] 
**verification_type** | **str** |  | [optional] 
**year_of_birth** | **str** |  | [optional] 

## Example

```python
from abha.models.identity_documents_by_fm_response import IdentityDocumentsByFMResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityDocumentsByFMResponse from a JSON string
identity_documents_by_fm_response_instance = IdentityDocumentsByFMResponse.from_json(json)
# print the JSON string representation of the object
print(IdentityDocumentsByFMResponse.to_json())

# convert the object into a dict
identity_documents_by_fm_response_dict = identity_documents_by_fm_response_instance.to_dict()
# create an instance of IdentityDocumentsByFMResponse from a dict
identity_documents_by_fm_response_from_dict = IdentityDocumentsByFMResponse.from_dict(identity_documents_by_fm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


