# ConsentAcknowledgement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**consent_id** | **str** |  | 

## Example

```python
from abdm_gateway.models.consent_acknowledgement import ConsentAcknowledgement

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentAcknowledgement from a JSON string
consent_acknowledgement_instance = ConsentAcknowledgement.from_json(json)
# print the JSON string representation of the object
print(ConsentAcknowledgement.to_json())

# convert the object into a dict
consent_acknowledgement_dict = consent_acknowledgement_instance.to_dict()
# create an instance of ConsentAcknowledgement from a dict
consent_acknowledgement_from_dict = ConsentAcknowledgement.from_dict(consent_acknowledgement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


