# MetricQueryFilterEntry

 | Metric Name | FilterEntry Name |    Allowed groupBy fields    |      Default Values      |                 Allowed Values                  | |-------------|------------------|------------------------------|--------------------------|-------------------------------------------------| | EVENTS      | ACCOUNT_ID       | ACCOUNT_ID, EVENT_STATUS     | None                     | *\\<one or more valid accounts IDs>              | | EVENTS      | CUSTOMER_ID      | ACCOUNT_ID, EVENT_STATUS     | None                     | *\\<at most one valid customer ID>               | | EVENTS      | EVENT_STATUS     | ACCOUNT_ID, EVENT_STATUS     | [PROCESSED, UNPROCESSED] | oneOrMoreOf PROCESSED, UNPROCESSED, IN_PROGRESS | | USAGE       | ACCOUNT_ID       | ACCOUNT_ID, USAGE_METER_NAME | None                     | *\\<one or more valid accounts ID>               | | USAGE       | CUSTOMER_ID      | ACCOUNT_ID, USAGE_METER_NAME | None                     | *\\<at most one valid customer ID>               | | USAGE       | USAGE_METER_NAME | ACCOUNT_ID, USAGE_METER_NAME | None                     | *\\<one or more valid usage meter name>          | | REVENUE     | ACCOUNT_ID       | ACCOUNT_ID, USAGE_METER_NAME | None                     | *\\<one or more valid accounts ID>               | | REVENUE     | CUSTOMER_ID      | ACCOUNT_ID, USAGE_METER_NAME | None                     | *\\<at most one valid customer ID>               | | REVENUE     | USAGE_METER_NAME | ACCOUNT_ID, USAGE_METER_NAME | None                     | *\\<one or more valid usage meter name>          | | EVENTS      | ORGANIZATION_ID  | ACCOUNT_ID, USAGE_METER_NAME | <From auth token>        |                                                 | | USAGE       | ORGANIZATION_ID  | ACCOUNT_ID, USAGE_METER_NAME | <From auth token>        |                                                 | | REVENUE     | ORGANIZATION_ID  | ACCOUNT_ID, USAGE_METER_NAME | <From auth token>        |                                                 | 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | 
**field_values** | **[str]** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


