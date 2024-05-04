# SubscriptionRequestSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | [**UsePurpose**](UsePurpose.md) |  | 
**patient** | [**ConsentManagerPatientID**](ConsentManagerPatientID.md) |  | 
**hiu** | [**OrganizationRepresentation**](OrganizationRepresentation.md) |  | 
**hips** | [**List[OrganizationRepresentation]**](OrganizationRepresentation.md) |  | [optional] 
**categories** | [**List[SubscriptionCategory]**](SubscriptionCategory.md) |  | 
**period** | [**SubscriptionPeriod**](SubscriptionPeriod.md) |  | 

## Example

```python
from abdm_gateway.models.subscription_request_subscription import SubscriptionRequestSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionRequestSubscription from a JSON string
subscription_request_subscription_instance = SubscriptionRequestSubscription.from_json(json)
# print the JSON string representation of the object
print(SubscriptionRequestSubscription.to_json())

# convert the object into a dict
subscription_request_subscription_dict = subscription_request_subscription_instance.to_dict()
# create an instance of SubscriptionRequestSubscription from a dict
subscription_request_subscription_from_dict = SubscriptionRequestSubscription.from_dict(subscription_request_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


