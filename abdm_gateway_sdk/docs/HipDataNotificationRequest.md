# HipDataNotificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**notification** | [**HipDataNotificationRequestNotification**](HipDataNotificationRequestNotification.md) |  | 

## Example

```python
from abdm_gateway.models.hip_data_notification_request import HipDataNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HipDataNotificationRequest from a JSON string
hip_data_notification_request_instance = HipDataNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(HipDataNotificationRequest.to_json())

# convert the object into a dict
hip_data_notification_request_dict = hip_data_notification_request_instance.to_dict()
# create an instance of HipDataNotificationRequest from a dict
hip_data_notification_request_from_dict = HipDataNotificationRequest.from_dict(hip_data_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


