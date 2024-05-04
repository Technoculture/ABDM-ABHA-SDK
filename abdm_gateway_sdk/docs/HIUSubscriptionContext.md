# HIUSubscriptionContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hip** | [**OrganizationRepresentation**](OrganizationRepresentation.md) |  | [optional] 
**categories** | [**List[SubscriptionCategory]**](SubscriptionCategory.md) |  | 
**period** | [**SubscriptionPeriod**](SubscriptionPeriod.md) |  | 

## Example

```python
from abdm_gateway.models.hiu_subscription_context import HIUSubscriptionContext

# TODO update the JSON string below
json = "{}"
# create an instance of HIUSubscriptionContext from a JSON string
hiu_subscription_context_instance = HIUSubscriptionContext.from_json(json)
# print the JSON string representation of the object
print(HIUSubscriptionContext.to_json())

# convert the object into a dict
hiu_subscription_context_dict = hiu_subscription_context_instance.to_dict()
# create an instance of HIUSubscriptionContext from a dict
hiu_subscription_context_from_dict = HIUSubscriptionContext.from_dict(hiu_subscription_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


