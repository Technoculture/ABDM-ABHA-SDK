# SubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request. | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**subscription** | [**SubscriptionRequestSubscription**](SubscriptionRequestSubscription.md) |  | 

## Example

```python
from abdm_gateway.models.subscription_request import SubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionRequest from a JSON string
subscription_request_instance = SubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(SubscriptionRequest.to_json())

# convert the object into a dict
subscription_request_dict = subscription_request_instance.to_dict()
# create an instance of SubscriptionRequest from a dict
subscription_request_from_dict = SubscriptionRequest.from_dict(subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


