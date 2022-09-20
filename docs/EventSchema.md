# EventSchema

Structure of an event schema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the event. Must be unique for an organization. | 
**version** | **int** | Version of event schema | 
**attributes** | [**[EventAttributeSchema]**](EventAttributeSchema.md) |  | 
**description** | **str** | Description of the event | [optional] 
**status** | **str** | Status of event schema * DRAFT - Schema is in draft state  * ACTIVE - Schema is currently active  * INACTIVE - Schema is currently inactive * ARCHIVED - Older version of event schema  | [optional] 
**dimensions** | [**[DimensionsSchema]**](DimensionsSchema.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


