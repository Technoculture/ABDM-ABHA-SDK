# HIUSubscriptionRequestReceipt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**subscription_request** | [**ConsentRequestInitResponseConsentRequest**](ConsentRequestInitResponseConsentRequest.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**resp** | [**RequestReference**](RequestReference.md) |  | 

## Example

```python
from abdm_gateway.models.hiu_subscription_request_receipt import HIUSubscriptionRequestReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of HIUSubscriptionRequestReceipt from a JSON string
hiu_subscription_request_receipt_instance = HIUSubscriptionRequestReceipt.from_json(json)
# print the JSON string representation of the object
print(HIUSubscriptionRequestReceipt.to_json())

# convert the object into a dict
hiu_subscription_request_receipt_dict = hiu_subscription_request_receipt_instance.to_dict()
# create an instance of HIUSubscriptionRequestReceipt from a dict
hiu_subscription_request_receipt_from_dict = HIUSubscriptionRequestReceipt.from_dict(hiu_subscription_request_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


