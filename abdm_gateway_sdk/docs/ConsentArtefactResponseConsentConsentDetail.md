# ConsentArtefactResponseConsentConsentDetail


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
**hiu** | [**ConsentRequestConsentHiu**](ConsentRequestConsentHiu.md) |  | 
**consent_manager** | [**ConsentArtefactResponseConsentConsentDetailConsentManager**](ConsentArtefactResponseConsentConsentDetailConsentManager.md) |  | 
**requester** | [**Requester**](Requester.md) |  | [optional] 
**hi_types** | [**List[HITypeEnum]**](HITypeEnum.md) |  | 
**permission** | [**Permission**](Permission.md) |  | 

## Example

```python
from abdm_gateway.models.consent_artefact_response_consent_consent_detail import ConsentArtefactResponseConsentConsentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentArtefactResponseConsentConsentDetail from a JSON string
consent_artefact_response_consent_consent_detail_instance = ConsentArtefactResponseConsentConsentDetail.from_json(json)
# print the JSON string representation of the object
print(ConsentArtefactResponseConsentConsentDetail.to_json())

# convert the object into a dict
consent_artefact_response_consent_consent_detail_dict = consent_artefact_response_consent_consent_detail_instance.to_dict()
# create an instance of ConsentArtefactResponseConsentConsentDetail from a dict
consent_artefact_response_consent_consent_detail_from_dict = ConsentArtefactResponseConsentConsentDetail.from_dict(consent_artefact_response_consent_consent_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


