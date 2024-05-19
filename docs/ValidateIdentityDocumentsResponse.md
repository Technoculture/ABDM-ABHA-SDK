# ValidateIdentityDocumentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**enrolment_number** | **str** |  | [optional] 
**health_id_number** | **str** |  | [optional] 
**jwt_response** | [**JwtResponse**](JwtResponse.md) |  | [optional] 
**verification** | [**VerifyIdentityDocumentsResponse**](VerifyIdentityDocumentsResponse.md) |  | [optional] 

## Example

```python
from abha.models.validate_identity_documents_response import ValidateIdentityDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateIdentityDocumentsResponse from a JSON string
validate_identity_documents_response_instance = ValidateIdentityDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateIdentityDocumentsResponse.to_json())

# convert the object into a dict
validate_identity_documents_response_dict = validate_identity_documents_response_instance.to_dict()
# create an instance of ValidateIdentityDocumentsResponse from a dict
validate_identity_documents_response_from_dict = ValidateIdentityDocumentsResponse.from_dict(validate_identity_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


