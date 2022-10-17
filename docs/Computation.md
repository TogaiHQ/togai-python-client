# Computation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computation** | **str** | Computation to be applied on an event if it matches the matcher In case of a COUNT aggregation type, computation should be passed as &#39;1&#39;  | 
**id** | **str** | Optional identifier describing the matcher and computation pair | [optional] 
**matcher** | **str** | Condition to be applied on event. Upon matching it the corresponding computation will be considered for usage_meter unit calculation. The result of the matcher needs to be truthy (https://jsonlogic.com/truthy.html) in order to be considered as a match.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


