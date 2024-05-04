# FetchDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_birth** | **str** |  | [optional] 
**dob** | **str** |  | [optional] 
**document_number** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**month_of_birth** | **str** |  | [optional] 
**year_of_birth** | **str** |  | [optional] 

## Example

```python
from abha.models.fetch_document_request import FetchDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FetchDocumentRequest from a JSON string
fetch_document_request_instance = FetchDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(FetchDocumentRequest.to_json())

# convert the object into a dict
fetch_document_request_dict = fetch_document_request_instance.to_dict()
# create an instance of FetchDocumentRequest from a dict
fetch_document_request_from_dict = FetchDocumentRequest.from_dict(fetch_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


