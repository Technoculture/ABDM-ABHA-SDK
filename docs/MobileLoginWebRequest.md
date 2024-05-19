# MobileLoginWebRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_id** | **str** |  | [optional] 
**txn_id** | **str** |  | [optional] 

## Example

```python
from abha.models.mobile_login_web_request import MobileLoginWebRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MobileLoginWebRequest from a JSON string
mobile_login_web_request_instance = MobileLoginWebRequest.from_json(json)
# print the JSON string representation of the object
print(MobileLoginWebRequest.to_json())

# convert the object into a dict
mobile_login_web_request_dict = mobile_login_web_request_instance.to_dict()
# create an instance of MobileLoginWebRequest from a dict
mobile_login_web_request_from_dict = MobileLoginWebRequest.from_dict(mobile_login_web_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


