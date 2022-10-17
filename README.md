# togai-client
[Togai](https://www.togai.com/) is an end to end pricing infrastructure that enable you with metering, aggregating, pricing and billing for your application.

This is an official Typescript client library for using [Togai APIs](https://docs.togai.com/reference/createcustomer).

- API version: 1.0
- Package version: 1.0.0
For more information, please visit [https://docs.togai.com](https://docs.togai.com)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

```sh
pip install togai-client
```
(you may need to run `pip` with root permission: `sudo pip install togai-client`)

Then import the package:
```python
import togai_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import togai_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:
You will need a API_TOKEN to use the API. You can get one from your Togai Account

```python

import time
import togai_client
from pprint import pprint
from togai_client.api import accounts_api
from togai_client.model.account import Account
from togai_client.model.account_paginated_response import AccountPaginatedResponse
from togai_client.model.add_account_aliases_request import AddAccountAliasesRequest
from togai_client.model.associate_price_plan_request import AssociatePricePlanRequest
from togai_client.model.associate_price_plan_response import AssociatePricePlanResponse
from togai_client.model.base_success_response import BaseSuccessResponse
from togai_client.model.create_account_request import CreateAccountRequest
from togai_client.model.error_response import ErrorResponse
from togai_client.model.remove_account_aliases_request import RemoveAccountAliasesRequest
from togai_client.model.update_account_request import UpdateAccountRequest
# Defining the host is optional and defaults to https://sandbox-api.togai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = togai_client.Configuration(
    host = "https://sandbox-api.togai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Bearer <credential>): bearerAuth
configuration = togai_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)


# Enter a context with an instance of the API client
with togai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounts_api.AccountsApi(api_client)
    customer_id =  # str | 
    account_id =  # str | 
    add_account_aliases_request = AddAccountAliasesRequest(
        aliases=[
            "aliases_example",
        ],
    ) # AddAccountAliasesRequest | Payload to add aliases to account

    try:
        # Add Aliases to account
        api_response = api_instance.add_aliases(customer_id, account_id, add_account_aliases_request)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling AccountsApi->add_aliases: %s\n" % e)
```

For a detailed step by step guide for a sample ingestion and metering at [examples](examples)

## Documentation for API Endpoints

All URIs are relative to *https://sandbox-api.togai.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**add_aliases**](docs/AccountsApi.md#add_aliases) | **POST** /customers/{customer_id}/accounts/{account_id}/add_aliases | Add Aliases to account
*AccountsApi* | [**associate_price_plan**](docs/AccountsApi.md#associate_price_plan) | **POST** /customers/{customer_id}/accounts/{account_id}/price_plans | Associate a plan to an account
*AccountsApi* | [**create_account**](docs/AccountsApi.md#create_account) | **POST** /customers/{customer_id}/accounts | Create an account
*AccountsApi* | [**delete_account**](docs/AccountsApi.md#delete_account) | **DELETE** /customers/{customer_id}/accounts/{account_id} | Delete an account
*AccountsApi* | [**get_account**](docs/AccountsApi.md#get_account) | **GET** /customers/{customer_id}/accounts/{account_id} | Get an account
*AccountsApi* | [**get_accounts**](docs/AccountsApi.md#get_accounts) | **GET** /customers/{customer_id}/accounts | List accounts of customer
*AccountsApi* | [**remove_aliases**](docs/AccountsApi.md#remove_aliases) | **POST** /customers/{customer_id}/accounts/{account_id}/remove_aliases | Remove Aliases to account
*AccountsApi* | [**update_account**](docs/AccountsApi.md#update_account) | **PATCH** /customers/{customer_id}/accounts/{account_id} | Update an account
*CustomersApi* | [**create_customer**](docs/CustomersApi.md#create_customer) | **POST** /customers | Create a customer
*CustomersApi* | [**delete_customer**](docs/CustomersApi.md#delete_customer) | **DELETE** /customers/{customer_id} | Delete a customer
*CustomersApi* | [**get_customer**](docs/CustomersApi.md#get_customer) | **GET** /customers/{customer_id} | Get a customer
*CustomersApi* | [**get_customers**](docs/CustomersApi.md#get_customers) | **GET** /customers | List customers
*CustomersApi* | [**update_customer**](docs/CustomersApi.md#update_customer) | **PATCH** /customers/{customer_id} | Update a customer
*EventIngestionApi* | [**ingest**](docs/EventIngestionApi.md#ingest) | **POST** /ingest | Ingest events to Togai
*EventIngestionApi* | [**ingest_batch**](docs/EventIngestionApi.md#ingest_batch) | **POST** /ingestBatch | Ingest events to Togai in batch
*EventManagementApi* | [**get_events**](docs/EventManagementApi.md#get_events) | **GET** /events | Get usage events from Togai
*EventManagementApi* | [**get_single_event**](docs/EventManagementApi.md#get_single_event) | **GET** /events/{event_id} | Get the usage event given event id.
*EventSchemasApi* | [**activate_event_schema**](docs/EventSchemasApi.md#activate_event_schema) | **POST** /event_schema/{event_schema_name}/activate | Activate an event schema
*EventSchemasApi* | [**create_event_schema**](docs/EventSchemasApi.md#create_event_schema) | **POST** /event_schema | Create an event schema
*EventSchemasApi* | [**deactivate_event_schema**](docs/EventSchemasApi.md#deactivate_event_schema) | **POST** /event_schema/{event_schema_name}/deactivate | Deactivate an event schema
*EventSchemasApi* | [**delete_event_schema**](docs/EventSchemasApi.md#delete_event_schema) | **DELETE** /event_schema/{event_schema_name} | Delete an event schema
*EventSchemasApi* | [**get_event_schema**](docs/EventSchemasApi.md#get_event_schema) | **GET** /event_schema/{event_schema_name} | Get an event schema
*EventSchemasApi* | [**list_event_schema_versions**](docs/EventSchemasApi.md#list_event_schema_versions) | **GET** /event_schema/{event_schema_name}/versions | List all event schema versions
*EventSchemasApi* | [**list_event_schemas**](docs/EventSchemasApi.md#list_event_schemas) | **GET** /event_schema | List event schemas
*EventSchemasApi* | [**update_event_schema**](docs/EventSchemasApi.md#update_event_schema) | **PATCH** /event_schema/{event_schema_name} | Update an event schema
*MetricsApi* | [**get_metrics**](docs/MetricsApi.md#get_metrics) | **POST** /metrics | Get togai metrics.
*PricePlansApi* | [**activate_price_plan**](docs/PricePlansApi.md#activate_price_plan) | **POST** /price_plans/{price_plan_name}/activate | Activate a price plan
*PricePlansApi* | [**create_price_plan**](docs/PricePlansApi.md#create_price_plan) | **POST** /price_plans | Create a price plan
*PricePlansApi* | [**get_price_plan**](docs/PricePlansApi.md#get_price_plan) | **GET** /price_plans/{price_plan_name} | Get a price plan
*PricePlansApi* | [**get_price_plans**](docs/PricePlansApi.md#get_price_plans) | **GET** /price_plans | List price plans
*PricePlansApi* | [**update_price_plan**](docs/PricePlansApi.md#update_price_plan) | **PATCH** /price_plans/{price_plan_name} | Update a price plan
*UsageMetersApi* | [**activate_usage_meter**](docs/UsageMetersApi.md#activate_usage_meter) | **POST** /event_schema/{event_schema_name}/usage_meters/{usage_meter_name}/activate | Activate usage meter
*UsageMetersApi* | [**create_usage_meter**](docs/UsageMetersApi.md#create_usage_meter) | **POST** /event_schema/{event_schema_name}/usage_meters | Create an usage meter
*UsageMetersApi* | [**deactivate_usage_meter**](docs/UsageMetersApi.md#deactivate_usage_meter) | **POST** /event_schema/{event_schema_name}/usage_meters/{usage_meter_name}/deactivate | Deactivate usage meter
*UsageMetersApi* | [**delete_usage_meter**](docs/UsageMetersApi.md#delete_usage_meter) | **DELETE** /usage_meter/{usage_meter_name} | Delete an Usage Meter
*UsageMetersApi* | [**get_usage_meter**](docs/UsageMetersApi.md#get_usage_meter) | **GET** /event_schema/{event_schema_name}/usage_meters/{usage_meter_name} | Get usage meter
*UsageMetersApi* | [**get_usage_meters_for_event_schema**](docs/UsageMetersApi.md#get_usage_meters_for_event_schema) | **GET** /event_schema/{event_schema_name}/usage_meters | List usage meters for event schema
*UsageMetersApi* | [**update_usage_meter**](docs/UsageMetersApi.md#update_usage_meter) | **PATCH** /event_schema/{event_schema_name}/usage_meters/{usage_meter_name} | Update an usage meter


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountAliases](docs/AccountAliases.md)
 - [AccountPaginatedResponse](docs/AccountPaginatedResponse.md)
 - [AddAccountAliasesRequest](docs/AddAccountAliasesRequest.md)
 - [AssociatePricePlanRequest](docs/AssociatePricePlanRequest.md)
 - [AssociatePricePlanResponse](docs/AssociatePricePlanResponse.md)
 - [BaseSuccessResponse](docs/BaseSuccessResponse.md)
 - [BundleStrategy](docs/BundleStrategy.md)
 - [BundleStrategyUsageMetersValue](docs/BundleStrategyUsageMetersValue.md)
 - [Computation](docs/Computation.md)
 - [CreateAccountRequest](docs/CreateAccountRequest.md)
 - [CreateCustomerRequest](docs/CreateCustomerRequest.md)
 - [CreateCustomerResponse](docs/CreateCustomerResponse.md)
 - [CreateEventSchemaRequest](docs/CreateEventSchemaRequest.md)
 - [CreatePricePlanRequest](docs/CreatePricePlanRequest.md)
 - [CreateUsageMeterRequest](docs/CreateUsageMeterRequest.md)
 - [Customer](docs/Customer.md)
 - [CustomerPaginatedResponse](docs/CustomerPaginatedResponse.md)
 - [Dimensions](docs/Dimensions.md)
 - [DimensionsSchema](docs/DimensionsSchema.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Event](docs/Event.md)
 - [EventAttribute](docs/EventAttribute.md)
 - [EventAttributeSchema](docs/EventAttributeSchema.md)
 - [EventPipelineInfo](docs/EventPipelineInfo.md)
 - [EventPipelineInfoAccount](docs/EventPipelineInfoAccount.md)
 - [EventPipelineInfoCustomer](docs/EventPipelineInfoCustomer.md)
 - [EventPipelineInfoEventSchema](docs/EventPipelineInfoEventSchema.md)
 - [EventPipelineInfoPricePlansInner](docs/EventPipelineInfoPricePlansInner.md)
 - [EventPipelineInfoUsageMetersInner](docs/EventPipelineInfoUsageMetersInner.md)
 - [EventSchema](docs/EventSchema.md)
 - [EventSchemaListData](docs/EventSchemaListData.md)
 - [EventSchemaListDataAllOf](docs/EventSchemaListDataAllOf.md)
 - [EventSchemaListPaginatedResponse](docs/EventSchemaListPaginatedResponse.md)
 - [EventSchemaVersionsResponse](docs/EventSchemaVersionsResponse.md)
 - [EventWithStatus](docs/EventWithStatus.md)
 - [EventWithStatusAndEventPipelineInfo](docs/EventWithStatusAndEventPipelineInfo.md)
 - [EventWithStatusAndEventPipelineInfoAllOf](docs/EventWithStatusAndEventPipelineInfoAllOf.md)
 - [GetEventResponse](docs/GetEventResponse.md)
 - [GetEventsResponse](docs/GetEventsResponse.md)
 - [GetMetricsRequest](docs/GetMetricsRequest.md)
 - [GetMetricsResponse](docs/GetMetricsResponse.md)
 - [IngestBatchEventRequest](docs/IngestBatchEventRequest.md)
 - [IngestBatchEventResponse](docs/IngestBatchEventResponse.md)
 - [IngestError](docs/IngestError.md)
 - [IngestEventRequest](docs/IngestEventRequest.md)
 - [IngestEventResponse](docs/IngestEventResponse.md)
 - [IngestionStatus](docs/IngestionStatus.md)
 - [MetricDataPoints](docs/MetricDataPoints.md)
 - [MetricDataPointsGroupedBy](docs/MetricDataPointsGroupedBy.md)
 - [MetricName](docs/MetricName.md)
 - [MetricQuery](docs/MetricQuery.md)
 - [MetricQueryFilterEntry](docs/MetricQueryFilterEntry.md)
 - [MetricQueryResponse](docs/MetricQueryResponse.md)
 - [PaginationOptions](docs/PaginationOptions.md)
 - [PlanOverride](docs/PlanOverride.md)
 - [PricePlan](docs/PricePlan.md)
 - [PricePlanListData](docs/PricePlanListData.md)
 - [PricePlanPaginatedResponse](docs/PricePlanPaginatedResponse.md)
 - [PricingCycle](docs/PricingCycle.md)
 - [PricingCycleStartOffset](docs/PricingCycleStartOffset.md)
 - [PricingSchedule](docs/PricingSchedule.md)
 - [RateCard](docs/RateCard.md)
 - [RateCardBundle](docs/RateCardBundle.md)
 - [RateCardUsage](docs/RateCardUsage.md)
 - [RateCardUsageValue](docs/RateCardUsageValue.md)
 - [RemoveAccountAliasesRequest](docs/RemoveAccountAliasesRequest.md)
 - [SignupRequest](docs/SignupRequest.md)
 - [SignupResponse](docs/SignupResponse.md)
 - [StatusResponse](docs/StatusResponse.md)
 - [StatusResponseHeaders](docs/StatusResponseHeaders.md)
 - [UpdateAccountRequest](docs/UpdateAccountRequest.md)
 - [UpdateCustomerRequest](docs/UpdateCustomerRequest.md)
 - [UpdateEventSchemaRequest](docs/UpdateEventSchemaRequest.md)
 - [UpdatePricePlanRequest](docs/UpdatePricePlanRequest.md)
 - [UpdateUsageMeterRequest](docs/UpdateUsageMeterRequest.md)
 - [UsageMeter](docs/UsageMeter.md)
 - [UsageMeterPaginatedResponse](docs/UsageMeterPaginatedResponse.md)
 - [UsageStrategy](docs/UsageStrategy.md)
 - [UserDetails](docs/UserDetails.md)


## Documentation For Authorization


## apiKeyAuth

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header


## bearerAuth

- **Type**: Bearer authentication (Bearer <credential>)


## Author

engg@togai.com


