# OrganizationRepresentation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 

## Example

```python
from abdm_gateway.models.organization_representation import OrganizationRepresentation

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationRepresentation from a JSON string
organization_representation_instance = OrganizationRepresentation.from_json(json)
# print the JSON string representation of the object
print(OrganizationRepresentation.to_json())

# convert the object into a dict
organization_representation_dict = organization_representation_instance.to_dict()
# create an instance of OrganizationRepresentation from a dict
organization_representation_from_dict = OrganizationRepresentation.from_dict(organization_representation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


