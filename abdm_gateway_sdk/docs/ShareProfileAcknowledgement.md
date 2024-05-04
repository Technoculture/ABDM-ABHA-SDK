# ShareProfileAcknowledgement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**health_id** | **str** |  | 

## Example

```python
from abdm_gateway.models.share_profile_acknowledgement import ShareProfileAcknowledgement

# TODO update the JSON string below
json = "{}"
# create an instance of ShareProfileAcknowledgement from a JSON string
share_profile_acknowledgement_instance = ShareProfileAcknowledgement.from_json(json)
# print the JSON string representation of the object
print(ShareProfileAcknowledgement.to_json())

# convert the object into a dict
share_profile_acknowledgement_dict = share_profile_acknowledgement_instance.to_dict()
# create an instance of ShareProfileAcknowledgement from a dict
share_profile_acknowledgement_from_dict = ShareProfileAcknowledgement.from_dict(share_profile_acknowledgement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


