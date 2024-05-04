# SubscriptionPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** |  | 
**to** | **datetime** |  | 

## Example

```python
from abdm_gateway.models.subscription_period import SubscriptionPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPeriod from a JSON string
subscription_period_instance = SubscriptionPeriod.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPeriod.to_json())

# convert the object into a dict
subscription_period_dict = subscription_period_instance.to_dict()
# create an instance of SubscriptionPeriod from a dict
subscription_period_from_dict = SubscriptionPeriod.from_dict(subscription_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


