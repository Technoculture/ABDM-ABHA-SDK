# ConsentFetchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**consent_id** | **str** |  | 

## Example

```python
from abdm_gateway.models.consent_fetch_request import ConsentFetchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentFetchRequest from a JSON string
consent_fetch_request_instance = ConsentFetchRequest.from_json(json)
# print the JSON string representation of the object
print(ConsentFetchRequest.to_json())

# convert the object into a dict
consent_fetch_request_dict = consent_fetch_request_instance.to_dict()
# create an instance of ConsentFetchRequest from a dict
consent_fetch_request_from_dict = ConsentFetchRequest.from_dict(consent_fetch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


