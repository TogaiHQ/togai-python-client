# EventSchemaListData


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
**associated_usage_meters** | **[str]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


