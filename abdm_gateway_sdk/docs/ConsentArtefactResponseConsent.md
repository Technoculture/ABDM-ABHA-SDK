# ConsentArtefactResponseConsent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ConsentStatus**](ConsentStatus.md) |  | 
**consent_detail** | [**ConsentArtefactResponseConsentConsentDetail**](ConsentArtefactResponseConsentConsentDetail.md) |  | 
**signature** | **str** |  | 

## Example

```python
from abdm_gateway.models.consent_artefact_response_consent import ConsentArtefactResponseConsent

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentArtefactResponseConsent from a JSON string
consent_artefact_response_consent_instance = ConsentArtefactResponseConsent.from_json(json)
# print the JSON string representation of the object
print(ConsentArtefactResponseConsent.to_json())

# convert the object into a dict
consent_artefact_response_consent_dict = consent_artefact_response_consent_instance.to_dict()
# create an instance of ConsentArtefactResponseConsent from a dict
consent_artefact_response_consent_from_dict = ConsentArtefactResponseConsent.from_dict(consent_artefact_response_consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


