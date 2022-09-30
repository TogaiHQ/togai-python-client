# AssociatePricePlanRequest

Request to associate a price plan to an account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_plan_name** | **str** | Name of the price plan | 
**effective_from** | **date** | Date of effectiveness of the association. - Expected only if the account already has a price plan associated with it.  | [optional] 
**effective_until** | **date** | Date until which the association must be effective. - Expected only if effectiveFrom is present.  | [optional] 
**rate_card_override** | [**RateCard**](RateCard.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


