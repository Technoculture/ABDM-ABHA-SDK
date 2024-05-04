# HipDataNotificationRequestNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patient** | [**HipDataNotificationRequestNotificationPatient**](HipDataNotificationRequestNotificationPatient.md) |  | 
**care_context** | [**CareContextDefinition**](CareContextDefinition.md) |  | 
**hi_types** | [**List[HITypeEnum]**](HITypeEnum.md) | Type of health data that created in the care context | 
**var_date** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**hip** | [**HipDataNotificationRequestNotificationHip**](HipDataNotificationRequestNotificationHip.md) |  | 

## Example

```python
from abdm_gateway.models.hip_data_notification_request_notification import HipDataNotificationRequestNotification

# TODO update the JSON string below
json = "{}"
# create an instance of HipDataNotificationRequestNotification from a JSON string
hip_data_notification_request_notification_instance = HipDataNotificationRequestNotification.from_json(json)
# print the JSON string representation of the object
print(HipDataNotificationRequestNotification.to_json())

# convert the object into a dict
hip_data_notification_request_notification_dict = hip_data_notification_request_notification_instance.to_dict()
# create an instance of HipDataNotificationRequestNotification from a dict
hip_data_notification_request_notification_from_dict = HipDataNotificationRequestNotification.from_dict(hip_data_notification_request_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


