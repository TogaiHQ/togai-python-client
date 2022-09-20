# UsageMeter

Structure of usage meter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the usage meter | 
**type** | **str** | Type of usage meter | 
**aggregation** | **str** | Aggregation to be applied on usage meter result | 
**description** | **str** |  | [optional] 
**status** | **str** | Status of usage meter | [optional] 
**filters** | **str** | Filters to be applied on event before matching to usage meter in JSONLogic format (https://jsonlogic.com/)  | [optional] 
**computation** | **str** | Computation. Has no effect if aggregation is &#39;count&#39; | [optional] 
**created_at** | **datetime** |  | [optional] 
**last_activated_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


