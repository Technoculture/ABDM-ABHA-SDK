# FetchDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **str** |  | [optional] 
**dob** | **str** |  | [optional] 
**document_number** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**month** | **str** |  | [optional] 
**permanent_address** | **str** |  | [optional] 
**temp_address** | **str** |  | [optional] 
**year** | **str** |  | [optional] 

## Example

```python
from abha.models.fetch_document_response import FetchDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FetchDocumentResponse from a JSON string
fetch_document_response_instance = FetchDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(FetchDocumentResponse.to_json())

# convert the object into a dict
fetch_document_response_dict = fetch_document_response_instance.to_dict()
# create an instance of FetchDocumentResponse from a dict
fetch_document_response_from_dict = FetchDocumentResponse.from_dict(fetch_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


