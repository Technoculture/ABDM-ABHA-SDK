# HIPConsentNotificationNotificationConsentDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**consent_id** | **str** |  | 
**created_at** | **datetime** |  | 
**patient** | [**ConsentManagerPatientID**](ConsentManagerPatientID.md) |  | 
**care_contexts** | [**List[HIPConsentNotificationNotificationConsentDetailCareContextsInner]**](HIPConsentNotificationNotificationConsentDetailCareContextsInner.md) |  | 
**purpose** | [**UsePurpose**](UsePurpose.md) |  | 
**hip** | [**HIPConsentNotificationNotificationConsentDetailHip**](HIPConsentNotificationNotificationConsentDetailHip.md) |  | 
**consent_manager** | [**HIPConsentNotificationNotificationConsentDetailConsentManager**](HIPConsentNotificationNotificationConsentDetailConsentManager.md) |  | 
**hi_types** | [**List[HITypeEnum]**](HITypeEnum.md) |  | 
**permission** | [**Permission**](Permission.md) |  | 

## Example

```python
from abdm_gateway.models.hip_consent_notification_notification_consent_detail import HIPConsentNotificationNotificationConsentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of HIPConsentNotificationNotificationConsentDetail from a JSON string
hip_consent_notification_notification_consent_detail_instance = HIPConsentNotificationNotificationConsentDetail.from_json(json)
# print the JSON string representation of the object
print(HIPConsentNotificationNotificationConsentDetail.to_json())

# convert the object into a dict
hip_consent_notification_notification_consent_detail_dict = hip_consent_notification_notification_consent_detail_instance.to_dict()
# create an instance of HIPConsentNotificationNotificationConsentDetail from a dict
hip_consent_notification_notification_consent_detail_from_dict = HIPConsentNotificationNotificationConsentDetail.from_dict(hip_consent_notification_notification_consent_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


