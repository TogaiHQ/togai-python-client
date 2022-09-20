# UpdateUsageMeterRequest

Request to update usage meter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of usage meter * COUNTER - Count usage  * GAUGE - Not supported at the moment * TIMER - Not supported at the moment  | 
**aggregation** | **str** | Aggregation to be applied on usage meter result * COUNT - Counts number of events matching the usage meter * SUM - Sums up results of computation of all events matching usage meter  | 
**description** | **str** | Description of the event | [optional] 
**filters** | **str** | Filters to be applied on event before matching to usage meter in JSONLogic format (https://jsonlogic.com/)  | [optional] 
**computation** | **str** | Computation. Has no effect if aggregation is &#39;count&#39; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


