# CreateHidMobileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_generated_benefit_id** | **bool** |  | [optional] 
**benefit_doc_type** | **str** |  | [optional] 
**benefit_id** | **str** |  | [optional] 
**benefit_name** | **str** |  | 
**consent_health_id** | **bool** |  | [optional] 
**date_of_birth** | **str** |  | 
**doc_number** | **str** |  | 
**file_type** | **str** |  | 
**gender** | **str** |  | 
**name** | **str** |  | 
**otp** | **str** |  | 
**txn_id** | **str** | Based on UUID | 
**uploaded_doc** | **str** | Encoded with Base 64 | 
**validity** | **str** |  | [optional] 

## Example

```python
from abha.models.create_hid_mobile_request import CreateHidMobileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHidMobileRequest from a JSON string
create_hid_mobile_request_instance = CreateHidMobileRequest.from_json(json)
# print the JSON string representation of the object
print(CreateHidMobileRequest.to_json())

# convert the object into a dict
create_hid_mobile_request_dict = create_hid_mobile_request_instance.to_dict()
# create an instance of CreateHidMobileRequest from a dict
create_hid_mobile_request_from_dict = CreateHidMobileRequest.from_dict(create_hid_mobile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


