# AssociatePricePlanRequest

Request to associate a price plan to an account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_plan_name** | **str** | Name of the price plan | 
**effective_from** | **date** | Date of effectiveness of the association. - Expected only if the account already has a price plan associated with it. - Date can only be startDate of any billing cycle of the currently associated price plan.  | [optional] 
**rate_card_override** | [**RateCard**](RateCard.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


