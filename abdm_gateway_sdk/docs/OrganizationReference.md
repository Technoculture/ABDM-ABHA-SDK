# OrganizationReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 

## Example

```python
from abdm_gateway.models.organization_reference import OrganizationReference

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationReference from a JSON string
organization_reference_instance = OrganizationReference.from_json(json)
# print the JSON string representation of the object
print(OrganizationReference.to_json())

# convert the object into a dict
organization_reference_dict = organization_reference_instance.to_dict()
# create an instance of OrganizationReference from a dict
organization_reference_from_dict = OrganizationReference.from_dict(organization_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


